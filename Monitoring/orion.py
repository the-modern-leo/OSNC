import datetime
from builtins import str
from builtins import object
from collections import namedtuple
import logging, json, traceback, re, time, threading
import xml.etree.ElementTree as ET
import orionsdk # requires package installation via pip
from . import settings
from dateutil import parser
from auth import Orionapi

class Orion(object):
    """
    This manages inventory attributes of the NOC's physical devices, such as
    asset tags, location, capital, department, etc. as well as SNMP/ICMP
    monitoring of each device through Solarwinds Orion. This supports viewing,
    adding, removing, and updating devices, as well as supporting some
    prediction methods for new entries.

    This uses the SolarWinds SWQL/SWIS, through its REST interface.

    Args:
        server (str): IP or hostname of the Orion server.
        username (str): Username of the API user.
        password (str): Password of the API user.
    """
    def __init__(self, server, username, password):
        # set up swis access
        self.swis = orionsdk.SwisClient(server, username, password)
        self.id_callback = None
        self.save_discovery_callback = None
        self.get_saved_switches_callback = None

    SwitchData = namedtuple('SwitchData', ['uri', 'id', 'ip', 'name',
            'dns_name', 'location', 'model', 'snmp_version', 'ios_version',
            'contact', 'barcode', 'proptag'])
    VlanData = namedtuple('VlanData', ['name', 'switchid', 'uri'])
    xmlnamespaces = {
        "main": "http://schemas.solarwinds.com/2008/Orion",
        "discovery": ("http://schemas.datacontract.org/2004/07/" +
                      "SolarWinds.Orion.Core.Models.Discovery")
    }

    class OrionObjectException(Exception):
        """
        This exception is raised when there is a problem accessing an Monitoring
        object (i.e. it does not exist or is invalid).
        """
        pass

    def register_callbacks(self, id_func, disc_func, get_func):
        """
        Register SwitchConfig callback functions for discovering SNMPv3-
        enabled switches.

        Args:
            id_func (func): ID callback function.
            disc_func (func): Save discovery function.
            get_func (func): Get saved switches function.
        """
        self.id_callback = id_func
        self.save_discovery_callback = disc_func
        self.get_saved_switches_callback = get_func

        # now that get_saved_switches_callback is defined, reschedule
        # discoveries
        self.reschedule_saved_discoveries()

    def _parse_results(self, result):
        """
        Internal function: get actual data from the SWIS response string, or
        throw an error if one is encountered.

        Args:
            result (dict): Response dictionary from Orion's SWIS.

        Returns:
            str: The response string if available.

        Raises:
            OrionObjectException: Caused if response string is unavailable.
        """
        if result.get('results', None) is None:
            raise self.OrionObjectException("Error querying node: "+str(result))
        elif not result['results']:
            raise self.OrionObjectException("Node does not exist")
        elif len(result['results']) == 0:
            return None

        return result['results']

    def _get_uri(self, nodeid):
        """
        Get the Solarwinds URI from the Node ID.

        Args:
            nodeid (int): Node ID.

        Returns:
            str: The Node URI.
        """
        results = self.swis.query("SELECT Uri FROM Orion.Nodes WHERE NodeID=" + str(nodeid))
        return self._parse_results(results)[0]['Uri']

    def _get_engine(self, is_clinical=False):
        """
        Discover and choose polling engines to use for a new discovered
        device. This will select polling engines from Orion based on settings -
        if a polling type has multiple servers, this will check the Orion
        pollers and assign it to the least-used one. This returns the polling
        engine ID if successful.

        Args:
            is_clinical (bool): Optional - Determines if the device should be
                discovered by a Clinical engine or a Campus one.

        Returns:
            int: The (load-balanced) Engine ID.
        """
        if is_clinical:
            engines = settings.CLINICALENGINES
        else:
            engines = settings.CAMPUSENGINES

        if len(engines) == 1:
            servers = "'" + engines[0] + "'"
        else:
            servers = "'"
            for serv in engines:
                servers += serv + "', '"

            servers += "'"

        query = ("SELECT (EngineID, ServerName, Nodes) FROM Orion.Engines "
                 "WHERE ServerName IN (" + servers + ")")
        result = self._parse_results(self.swis.query(query))
        sorted_list = sorted(result, key=lambda k: k['Nodes'])
        return sorted_list[0]['EngineID']

    def get_dev_info(self):
        """
        Fetches development status.

        Returns:
            str: Returns "Production" if url is sys.utah.edu, returns
            "Development" otherwise.
        """
        return ("Production" if "sys.utah.edu" in self.swis.url
                else "Development")

    def get_switch(self, ip=None, proptag=None, barcode=None, dns_name=None):
        """
        Get switch information by either IP, property tag, or barcode. This will
        return switch information. Note that all arguments are optional;
        however, at least one must be used to filter results.

        Args:
            ip (str): Optional - IP address of the switch.
            proptag (str): Optional - Property tag of the switch.
            barcode (str): Optional - Barcode of the switch.
            dns_name (str): Optional - DNS/hostname.

        Returns:
            Orion.SwitchData: An object with the most relevant switch returned.

        Raises:
            ValueError: Caused when no information is given.
        """
        result = ""
        query = ("SELECT (Uri, NodeID, IP, DNS, NodeName, Location, Contact," \
                 "IOSVersion, MachineType, SNMPVersion) FROM Orion.Nodes ")
        if ip:
            ip = ip.split('/')[0] # get rid of CIDR just in case
            result = self.swis.query(query + f"WHERE IP='{ip}'")
        elif proptag or barcode:
            result = self.swis.query(query + "WHERE Location LIKE '%" +
                    str(proptag if proptag else barcode) + "%'")
        elif dns_name:
            result = self.swis.query(query + "WHERE DNS LIKE '%" +
                    dns_name + "%'")
        else:
            raise ValueError("no information given")

        result = self._parse_results(result)[0]

        contact = result['Contact'].split(' ')
        barcode, proptag = contact[0], contact[-1]
        return self.SwitchData(result['Uri'], result['NodeID'], result['IP'],
                result['NodeName'], result['DNS'], result['Location'],
                result['MachineType'],result['SNMPVersion'],
                result['IOSVersion'], contact, barcode, proptag)

    def get_vlans(self, switch_id):
        """
        Get switch VLAN information (name and ID) by Node ID. If the Node ID is
        not available (but IP, DNS name, etc. is), run get_switch() before using
        this function.

        Args:
            switch_id (str): Node ID of the device.

        Returns:
            dict: Contains VLAN IDs as keys and VlanData objects as objects.
        """
        result = ""
        query = "SELECT (VlanId, VlanName, Uri) FROM Orion.NodeVlans "

        result = self.swis.query(query + "WHERE NodeID = " + str(switch_id))
        result = self._parse_results(result)

        vlans = {}
        for vlan in result:
            if vlan['VlanId'] != 1: # don't care about default vlan
                vlans[vlan['VlanId']] = self.VlanData(vlan['VlanName'],
                        switch_id, vlan['Uri'])

        return vlans

    def force_poll(self, switch_id):
        """
        Force Orion to poll a node by ID.  This does not wait for a response
        or status/error code.

        Args:
            switch_id (str): Node ID of the device.

        Returns:
            str: The return string of the SWIS invoke command.
        """
        return self.swis.invoke('Orion.Nodes', 'PollNow', 'N:' + str(switch_id))

    def change_switch_data(self, ip=None, dbid=None, item=None, value=None):
        """
        Change a Node name by IP. If a database/Node ID is given, search with
        that instead.

        Args:
            ip (str): Optional - IP address of the device. If this  is left as
                None, dbid must be defined.
            dbid (int): Optional - Node ID of the device. If this is left as
                None, ip must be defined.
            item (str): Optional - Item/property name to change.
            value (str): Optional - Value the property should be changed to.

        Raises:
            ValueError: Caused if not enough arguments are provided.
        """
        if (not ip and not dbid) or not item or not value:
            raise ValueError("not enough information given")
        elif ip and not dbid:
            dbid = self.get_switch(ip).id

        # get URI
        uri = self._get_uri(dbid)

        # add node properties
        props = { item: value }
        if 'NodeName' in item:
            props['DNS'] = value
        if item in [settings.CPROPNAMES['barcode'],
                settings.CPROPNAMES['proptag']]:
            uri = uri + '/CustomProperties'

        self.swis.update(uri, **props)

    def discover_snmpv3_switch(self, ip, is_clinical=False, dbid=None):
        """
        Discover and add an SNMPv3 switch to Orion.

        This only requires the IP of the switch, but does require that the
        device be up and communicating. If successful, this will return the
        discovery ID to poll for progress.

        Args:
            ip (str): IP Address of the device.
            is_clinical (bool): Optional - Determines whether to use Campus or
                Clinical SNMP credentials.
            dbid (int): Optional - Node ID that will be passed to id_callback.

        Returns:
            str: A discovery ID if available.
        """
        logging.info("Starting SNMPv3 discovery for " + str(ip) + "...")
        if is_clinical:
            ro_cred_id = settings.CLINICALCREDENTIALROID
        else:
            ro_cred_id = settings.CAMPUSCREDENTIALROID
        bulklist = {
            'BulkList': [{'Address': ip}],
            'Credentials': [{'CredentialID': ro_cred_id, 'Order': 1}],
            'WmiRetriesCount': 0,
            'WmiRetryIntervalMiliseconds': 1000
        }

        # generate a core plugin config
        coreconfig = self.swis.invoke('Orion.Discovery',
                                      'CreateCorePluginConfiguration', bulklist)
        engineid = self._get_engine(is_clinical)
        logging.debug("Chosen engine id: " + str(engineid))
        discoveryProfile = {
            'Name': 'Engineer script discovery',
            'EngineID': engineid,
            'JobTimeoutSeconds': 3600,
            'SearchTimeoutMiliseconds': 5000,
            'SnmpTimeoutMiliseconds': 5000,
            'SnmpRetries': 2,
            'RepeatIntervalMiliseconds': 1800,
            'SnmpPort': 161,
            'HopCount': 0,
            'PreferredSnmpVersion': 'SNMP3',
            'DisableIcmp': False,
            'AllowDuplicateNodes': False,
            'IsAutoImport': True,
            'IsHidden': True,
            'PluginConfigurations': [{'PluginConfigurationItem': coreconfig}]
        }

        result = self.swis.invoke('Orion.Discovery', 'StartDiscovery',
                                  discoveryProfile)
        if dbid and self.id_callback is not None:
            self.id_callback(result, dbid)
        return result

    def get_discovery_progress(self, discoveryid):
        """
        Get the discovery progress of a particular discovery ID.

        Args:
            discoveryid (dict): Discovery ID of a particular job.

        Returns:
            bool: True if the discovery is complete, False otherwise.

        Raises:
            OrionObjectException: Caused if there are issues communicating with
                Orion.
        """
        result = self.swis.invoke('Orion.Discovery', 'GetDiscoveryProgress',
                                  discoveryid)
        if isinstance(result, dict):
            logging.error(result)
            raise self.OrionObjectException("Error communicating with Orion")
        try:
            root = ET.fromstring(result)
            status=root.findall("main:Status", namespaces=self.xmlnamespaces)[0]

            if 'Status' in status.tag:
                phase = status.findall("discovery:Phase",
                                       namespaces=self.xmlnamespaces)[0]
                if ('Inventory' in phase.text or 'Unknown' in phase.text
                    or 'Detection' in phase.text):
                    return False

            return True
        except IndexError as e:
            traceback.print_exc()
            return False
        except UnicodeEncodeError:
            return False
        except Exception as e:
            traceback.print_exc()
            return False

    def add_custom_properties(self, nodeid, building_name, tier):
        """
        Add custom properties to a particular switch. This includes all building
        data, notification/alert tier, routing node, etc. This will
        automatically generate/retrieve service date, asset and property tags,
        and serial number. This will also add the SNMPv3 RW string credentials,
        since this is not added during the discovery process. To add custom
        properties to a device with an IP address, use
        add_custom_properties_by_ip() instead.

        Args:
            nodeid (int): Node ID of the device.
            building_name (str): Building name that the device is located in.
            tier (int): Notification tier that the device should alert for.

        Raises:
            OrionObjectException: Caused if switch is not discovered properly or
                if properties are added unsucessfully.
        """
        logging.info("Adding custom properties for node " + str(nodeid))
        # get URI
        uri = self._get_uri(nodeid)

        # get some switch information - refer to /assets/hostname-format.md
        switchdata = self.swis.read(uri)

        if not switchdata.get('SysName', ''):
            raise self.OrionObjectException("Switch not discovered properly")

        barcode = switchdata['Contact'].split(' ')[0]
        proptag = switchdata['Contact'].split(' ')[1]

        locationdata = switchdata['SysName'].split('-')
        building_number = locationdata[1]
        if building_number.isdigit(): # research park building
            offset = 1
        else:
            offset = 0
            building_number = re.findall(r'\d+', building_number)[0]
        building_abbr = re.sub(building_number, '', locationdata[1 + offset])
        room_number = locationdata[2 + offset].split('.')[0]
        distribution_node = locationdata[-1].split('.')[0]

        # ignore buildings that have their own routers
        if str(distribution_node).lower() == "self":
            distribution_node = ""
        else:
            distribution_node = str(distribution_node).upper()

        props = {
            settings.CPROPNAMES['barcode']: barcode,
            settings.CPROPNAMES['proptag']: proptag,
            settings.CPROPNAMES['role']: 'EDGE',
            settings.CPROPNAMES['department']: 'UIT NOC',
            settings.CPROPNAMES['bldgname']: building_name.replace('-', ''),
            settings.CPROPNAMES['bldgnumber']: building_number,
            settings.CPROPNAMES['roomnumber']: room_number,
            settings.CPROPNAMES['tier']: "Tier " + str(tier),
            settings.CPROPNAMES['distnode']: distribution_node,
        }

        self.swis.update(uri + '/CustomProperties', **props)

        results = self.swis.read(uri + '/CustomProperties')
        if not results or not results[settings.CPROPNAMES['bldgnumber']]:
            logging.error(results)
            raise self.OrionObjectException("Properties not added successfully")

        try:
            # get RO snmp id - is this campus or clinical credentials?
            results = self.swis.query("SELECT SettingValue FROM " +
                    "Orion.NodeSettings WHERE NodeID=" + str(int(nodeid)) +
                    " AND SettingName='ROSNMPCredentialID'")

            ro_cred = results['results'][0]['SettingValue']
            rw_cred = (settings.CAMPUSCREDENTIALRWID
                    if int(ro_cred) == settings.CAMPUSCREDENTIALROID
                    else settings.CLINICALCREDENTIALRWID)
            snmpprops = {
                'NodeID': nodeid,
                'SettingName': 'RWSNMPCredentialID',
                'SettingValue': str(rw_cred),
            }
            self.swis.create("Orion.NodeSettings", **snmpprops)

            # check results
            results = self.swis.query("SELECT SettingValue FROM " +
                    "Orion.NodeSettings WHERE NodeID=" + str(int(nodeid)) +
                    " AND SettingName='RWSNMPCredentialID'")
            if not results or not results['results']:
                raise self.OrionObjectException("SNMPv3 RW credentials not " +
                        "added successfully")
        except:
            traceback.print_exc()
            raise

        logging.info("Custom properties added successfully for " + str(nodeid))

    def add_custom_properties_by_ip(self, ip, building_name, tier):
        """
        Wrapper for add_custom_properties() - this accepts an IP instead of
        a node ID.

        Args:
            ip (str): IP Address of the device.
            building_name (str): Building name the device is located in.
            tier (int): Notification tier that the device should alert for.
        """
        nodeid = self.get_switch(ip).id
        return self.add_custom_properties(nodeid, building_name, tier)

    def schedule_snmpv3_discovery(self, date, ip, isclinical, tier, bldg_name,
            dbid, prop_delay=180):
        """
        Schedule an SNMPv3 discovery for a particular switch. Once this is done,
        two threads will be created to call an external discovery function and
        add custom properties to the Orion node (if discovery is successful).

        Args:
            date (int): Date to schedule the discovery. Note that the date
                format is an integer (seconds since Unix epoch).
            switchdata (Orion.SwitchData): Namedtuple for the discovered switch.
            dbid (int): Database ID to pass to the callback function. (defined
                with register_discovery_callback() ).
            prop_delay (int): Optional - Custom properties delay, since custom
                properties can only be entered if the switch is registered in
                Orion. Default is 180 seconds.

        Raises:
            ValueError: Caused by date being in the past.
        """
        ip = ip.split('/')[0]
        # make sure date is in the future
        if(date < int(time.time())):
            raise ValueError("Date is in the past")

        # Schedule the actual SNMPv3 discovery
        t_disc = threading.Timer((date - int(time.time())),
                self.discover_snmpv3_switch,
                (ip, isclinical, dbid))
        t_disc.name = 'snmp3discovery_' + ip
        t_disc.start()

        # Schedule custom properties - the switch must be in Orion first
        t_cp = threading.Timer((date - int(time.time()) + prop_delay),
                self.add_custom_properties_by_ip, (ip, bldg_name, tier))
        t_cp.name = 'snmp3props_' + ip
        t_cp.start()

        if self.save_discovery_callback is not None:
            self.save_discovery_callback(date, dbid)

    def schedule_maintiance_window(self, ip, starttime, endtime):
        """
        sets the switch to unmanaged for the window of time.
        Args:
            date (int): Date to schedule the discovery. Note that the date
                format is an integer (seconds since Unix epoch).
            switchdata (Orion.SwitchData): Namedtuple for the discovered switch.
            dbid (int): Database ID to pass to the callback function. (defined
                with register_discovery_callback() ).
            prop_delay (int): Optional - Custom properties delay, since custom
                properties can only be entered if the switch is registered in
                Orion. Default is 180 seconds.

        Raises:
            ValueError: Caused by date being in the past.
        """

        dbid = self.get_switch(ip)

        # get URI
        uri = self._get_uri(dbid.id)

        props = {'UnManageFrom': starttime,
                 'UnManageUntil':endtime}

        self.swis.update(uri, **props)

    def reschedule_saved_discoveries(self):
        """
        Reschedule any discoveries that were saved.
        """
        if self.get_saved_switches_callback is None:
            return # skip rescheduling, can't get switch information

        switchlist = self.get_saved_switches_callback()
        for switch in switchlist:
            if not isinstance(switch.schedule, (int, float)):
                continue
            elif time.time() > switch.schedule:
                continue # skip if scheduled in the past

            ip = switch.ip.split('/')[0]
            switchdata = json.loads(switch.switchdata)
            isclinical = switchdata.get('isclinical', False)
            tier = switchdata.get('service_tier', 0)
            bldg_name = switchdata.get('building_name', None)

            logging.info("Rescheduling discovery thread for " + str(switch.ip))
            # Schedule the actual SNMPv3 discovery
            t_disc = threading.Timer((switch.schedule - int(time.time())),
                    self.discover_snmpv3_switch,
                    (ip, isclinical, switch.id))
            t_disc.name = 'snmp3discovery_' + ip
            t_disc.start()

            # Schedule custom properties - the switch must be in Orion first
            t_cp = threading.Timer((switch.schedule - int(time.time()) + 180),
                    self.add_custom_properties_by_ip, (ip, bldg_name, tier))
            t_cp.name = 'snmp3props_' + ip
            t_cp.start()

    def get_memory_usage_batch(self):
        query = """SELECT IPAddress, MemoryUsed, PercentMemoryUsed FROM Orion.Nodes WHERE NodeID IN ('1007','1120','1121','1122','1190','1221','1227','1230','1237','1247','1256','1285','1287','1304','1347','1393','1490','1542','1552','1553','1554','1557','1560','1563','1564','1576','1582','1640','1831','1842','1892','1965','1968','1977','1987','2021','2050','2075','2077','2078','2079','2086','2104','2109','2152','2155','2161','2241','2282','2406','2407','2692','2782','2800','2801','2802','3405','3483','3515','3870','4025','4027','4028','4029','4030','4031','4116','4122','6230','6569','6669','7031','7053','7055','7056','7058','7085','7086','7155','9894','12129','13044','13045','13993','14729','16656','17090','21432','21686','22159','31251','32225','32544','32668','34113','34230','41922','42126','44507','46724','46980','46981','46982','46996','47005','47090','47091','47092','47093','47094','47095','47096','47099','47100','47723','48226','48228','48246','48247','48260','48667','48668','48734','48746','48752','48758','48759','48760','48763','48780','48885','48936','49057','49058','49059','49061','49062','49063','49125','49127','49162','49209','49237','49312','49317','49370','49414','49415','49426','49440','49443','49455','49456','49475','49483','49595','49596','49605','50503','52166','60844','68835','69082','74621','74937','75036','75088','75208','75424','75435','75573','75666','75724','75726','76099','76124','76144','76311','82106','82174','82195','82197','82203','82264','82265','82271','82313','82315','82316','82319','82320','82346','82347','82348','82713','82741','83744','83745','83746','83747','83748','83749','83766','83767','83945','84060','84087','84110','84111','84112','84113','86693','86811','86813','90633','90654','95331','95334','95407','95424','95425','95431','95435','95527','95530','102262','104868','104869','104915','105005','105184','105185','105316')"""
        result = self.swis.query(query)
        return result

    def get_no_ssh_Response(self):
        query = """SELECT CoreNodeID, LoginStatus FROM NCM.NodeProperties 
        WHERE LoginStatus LIKE '%Connection Refused by%' OR 'Cannot Log into Device : bad password.' """
        result = self.swis.query(query)['results']
        query_2 = """SELECT NodeID, Caption, IPAddress FROM Orion.Nodes"""
        result_2 = self.swis.query(query_2)['results']
        final_results = []
        for r in result:
            for r_2 in result_2:
                if r['CoreNodeID'] == r_2['NodeID']:
                    r_new = {**r,**r_2}
                    final_results.append(r_new)
                    break
        return final_results

    def get_no_snmp_Response(self):
        query = """SELECT CoreNodeID, SNMPLevel, SNMPUsername,SNMPAuthType,
        SNMPAuthPass,SNMPEncryptType,SNMPEncryptPass,Community,CommunityReadWrite,
          EncryptionAlgorithm,Username,Password  FROM NCM.Nodes"""
        result_1 = self.swis.query(query)['results']
        query = """SELECT CoreNodeID, LastInventory FROM NCM.NodeProperties"""
        result_2 = self.swis.query(query)['results']
        week_no_snmp = []
        for r in result_2:
            log_date = parser.parse(r['LastInventory'])
            week_ago = datetime.datetime.now() - datetime.timedelta(days=7)
            if log_date < week_ago: #more than a week ago
                week_no_snmp.append(r)
        query_2 = """SELECT NodeID, Caption, IPAddress FROM Orion.Nodes"""
        result_3 = self.swis.query(query_2)['results']
        first_results = []
        for r in week_no_snmp:
            for r_2 in result_3:
                if r['CoreNodeID'] == r_2['NodeID']:
                    r_new = {**r, **r_2}
                    first_results.append(r_new)
                    break
        final_results = []
        for r in first_results:
            for r_1 in result_1:
                if r['NodeID'] == r_1['CoreNodeID']:
                    r_new = {**r, **r_1}
                    final_results.append(r_new)
                    break
        return final_results
    def update_snmp(self,orionobj,tablename,columnname,columnvalue):
        """
        Modifies the provided Monitoring object with the correct snmp entries
        Args:
            orionobj (JSON): A JSON object from the Orion API
        """
        try:
            # add node properties
            query = f"SELECT Uri FROM {tablename} WHERE {columnname}={columnvalue}"
            uri = self.swis.query(f"SELECT Uri FROM {tablename} WHERE {columnname}={columnvalue}")['results'][0]['Uri']
            props = {'SNMPLevel': 3,
                     'SNMPUsername':'NONUserv3Rw',
                     'SNMPAuthType':'MD5',
                     'SNMPAuthPass':'U!tN0cRW#2',
                     'SNMPEncryptType':'DES',
                     'SNMPEncryptPass':'U!tN0cRW#2'}

            self.swis.update(uri, **props)
            query = f"""SELECT CoreNodeID, SNMPLevel, SNMPUsername,SNMPAuthType,SNMPAuthPass,SNMPEncryptType,SNMPEncryptPass,Community,CommunityReadWrite  FROM {tablename} WHERE {columnname}={columnvalue}"""
            result_1 = self.swis.query(query)['results']
            if result_1[0]['SNMPUsername'] != 'NONUserv3Rw':
                raise ConnectionError ('SNMP Username not updated')
            if result_1[0]['SNMPAuthType'] != 'MD5':
                raise ConnectionError ('SNMP AuthType not updated')
            if result_1[0]['SNMPEncryptType'] != 'DES':
                raise ConnectionError ('SNMP EncryptType not updated')
        except Exception as e:
            logging.error(e, exc_info=True)
            raise
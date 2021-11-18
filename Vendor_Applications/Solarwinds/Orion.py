import orionsdk
from auth import Orionapi


class Orion(object):
    """
    Args:
        server (str): IP or hostname of the Orion server.
        username (str): Username of the API user.
        password (str): Password of the API user.
    """

    def __init__(self):
        # set up swis access
        self.swis = None
    xmlnamespaces = {
        "main": "http://schemas.solarwinds.com/2008/Orion",
        "discovery": ("http://schemas.datacontract.org/2004/07/" +
                      "SolarWinds.Orion.Core.Models.Discovery")
    }

    def login(self):
        try:
            self.swis = orionsdk.SwisClient(Orionapi.server, Orionapi.username, Orionapi.password)
        except Exception as e:
            print(e)

    def logout(self):

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
            raise self.OrionObjectException("Error querying node: " + str(result))
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

    def get_switch(self, ip=None,dns_name=None):
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
        query = ("SELECT (Uri, NodeID, IP, DNS, NodeName, Location, Contact," \
                 "IOSVersion, MachineType, SNMPVersion) FROM Orion.Nodes ")
        if ip:
            ip = ip.split('/')[0]  # get rid of CIDR just in case
            result = self.swis.query(query + f"WHERE IP='{ip}'")
        elif dns_name:
            result = self.swis.query(query + "WHERE DNS LIKE '%" +
                                     dns_name + "%'")
        else:
            raise ValueError("no information given")

        result = self._parse_results(result)[0]

        return (result['Uri'], result['NodeID'], result['IP'],
                               result['NodeName'], result['DNS'], result['Location'],
                               result['MachineType'], result['SNMPVersion'],
                               result['IOSVersion'])

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
            if vlan['VlanId'] != 1:  # don't care about default vlan
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
                 'UnManageUntil': endtime}

        self.swis.update(uri, **props)

    def get_memory_usage_batch(self):
        query = """SELECT IPAddress, MemoryUsed, PercentMemoryUsed FROM Orion.Nodes WHERE NodeID IN ('1007','1120','1121','1122','1190','1221','1227','1230','1237','1247','1256','1285','1287','1304','1347','1393','1490','1542','1552','1553','1554','1557','1560','1563','1564','1576','1582','1640','1831','1842','1892','1965','1968','1977','1987','2021','2050','2075','2077','2078','2079','2086','2104','2109','2152','2155','2161','2241','2282','2406','2407','2692','2782','2800','2801','2802','3405','3483','3515','3870','4025','4027','4028','4029','4030','4031','4116','4122','6230','6569','6669','7031','7053','7055','7056','7058','7085','7086','7155','9894','12129','13044','13045','13993','14729','16656','17090','21432','21686','22159','31251','32225','32544','32668','34113','34230','41922','42126','44507','46724','46980','46981','46982','46996','47005','47090','47091','47092','47093','47094','47095','47096','47099','47100','47723','48226','48228','48246','48247','48260','48667','48668','48734','48746','48752','48758','48759','48760','48763','48780','48885','48936','49057','49058','49059','49061','49062','49063','49125','49127','49162','49209','49237','49312','49317','49370','49414','49415','49426','49440','49443','49455','49456','49475','49483','49595','49596','49605','50503','52166','60844','68835','69082','74621','74937','75036','75088','75208','75424','75435','75573','75666','75724','75726','76099','76124','76144','76311','82106','82174','82195','82197','82203','82264','82265','82271','82313','82315','82316','82319','82320','82346','82347','82348','82713','82741','83744','83745','83746','83747','83748','83749','83766','83767','83945','84060','84087','84110','84111','84112','84113','86693','86811','86813','90633','90654','95331','95334','95407','95424','95425','95431','95435','95527','95530','102262','104868','104869','104915','105005','105184','105185','105316')"""
        result = self.swis.query(query)
        return result

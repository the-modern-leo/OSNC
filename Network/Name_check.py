from builtins import str
from concurrent.futures.thread import ThreadPoolExecutor

import requests
import orionsdk
import re
import paramiko
import logging
import auth
from logging import FileHandler, Formatter
from Network.Network import Switch
from Network import Switch.settings as nwsettings
import Switch.settings
import os
from datetime import datetime
import json
import random
import csv


LOGFILE = f"{__name__}_{datetime.today().date()}.info"
Metrics = f"{__name__}_{datetime.today().date()}.Metrics"
Error = f"{__name__}_{datetime.today().date()}.error"

#Metrics Logger
metrics_logger = logging.getLogger(f"{__name__}.metrics")
metrics_logger.setLevel(logging.DEBUG)
handler = FileHandler(Metrics)
formatter = Formatter("%(asctime)s:%(name)s:%(thread)d:%(message)s")
handler.setFormatter(formatter)
metrics_logger.addHandler(handler)


ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

#General Logging file
infohandler = logging.FileHandler(LOGFILE)
logger = logging.getLogger(__name__)

#Error Handler File
errorhandler = logging.FileHandler(Error)


logger.setLevel(logging.INFO)
errorhandler.setLevel(logging.ERROR)
formatter = logging.Formatter("%(asctime)s:%(name)s:%(levelno)s:%(levelname)s:%(thread)d:%(message)s")
handler.setFormatter(formatter)
errorhandler.setFormatter(formatter)

#add files to logger
logger.addHandler(infohandler)
logger.addHandler(errorhandler)
logger.addHandler(ch)

def RepresentsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

class Building:
    def __init__(self):
        self.BuildingNumber = None
        self.BuildingName = None
        self.Abbreviation = None
        self.Campus = None
        self.StreetAddress = None
        self.StreetCoordinate = None
        self.City = None
        self.State = None
        self.zip = None
        self.Status = None
        self.Leased = None
        self.Built = None
        self.Demolished = None
        self.LocationCode = None
        self.NASF =None
        self.NSF = None
        self.GSF = None

class Namecheck():
    class OrionObjectException(Exception):
        """
        This exception is raised when there is a problem accessing an Monitoring
        object (i.e. it does not exist or is invalid)
        """
        pass

    def __init__(self,switch,orion_name=None,orion_dns=None):
        """
        Initializes the Namecheck object and sets all class variables. Establishes connections with all of the APIs
        that are used within the program.
        """
        try:
            # Initialize request session object and login to Infoblox
            self.ib_session = requests.session()
            self.ib_session.verify = False
            self.ib_url = auth.InfobloxAPI.url

            # Connects to the Orion API
            self.orionapi = orionsdk.SwisClient(hostname=auth.OrionAPI.url,
                                                username=auth.OrionAPI.username,
                                                password=auth.OrionAPI.password)
            # self.orionapi = orionsdk.SwisClient(auth.OrionTestAPI.test_api_host,
            #                                     auth.OrionTestAPI.test_api_usr, auth.OrionTestAPI.test_api_pwd)

            # Instantiate statistics fields for the results
            self.buildinglist = []

            # create the building list
            self.generate_building_list()

            #variables to assign to Infoblox
            self.ipv4addrs_obj = None
            self.host_object = None
            self.external_host_object = False
            self.arecord_object = None
            self.cname_objects = []
            self.multiple_hosts = False
            self.cname1check = False
            self.cname2check = False
            self.aliascheck = False
            self.rightcnames = {}
            self.wrongcnames = {}
            self.righthost = {}
            self.wronghost = {}
            self.multiple_arecord = False
            self.missing_host_record = False

            #Monitoring Variables
            self.orion_name = orion_name
            self.orion_dns = orion_dns

            #switch variables = None
            self.switch = switch
            self.skipswitch = False

            #name check vriables
            self.NameEqual_check = False
            self.orion = False
            self.switchbanner = False
            self.switchhost = False
            self.infoblox = False
            self.orion = False

            #names
            self.AuthoritativeName = None
            self.cname1 = None
            self.cname2 = None
        except Exception as e:
            logger.error(e, exc_info=True)

###################################################InfoBlox#############################################################
    def get_InfoBlox_data(self):
        """
        Generates and returns a list of Uris that will be used in calling the Infoblox API to change records

        Args:
            ip: The ip address of the switch that will have its records changed through the API call

        Returns:
            A list of Node URI Strings
        """
        logger.info(f"Pulling Records From InfoBlox for {self.switch.ip} - Starting")
        try:
            host = self.ib_session.get(self.ib_url + "ipv4address?status=USED&ip_address=" + self.switch.ip,
                                       auth=(auth.InfobloxAPI.username, auth.InfobloxAPI.password))
            response = self._process_get_response(host)
            if response:
                self.ipv4addrs_obj = response[0]
                host_objects = []
                arcord_object = []
                for item in response[0]['objects']:
                    item_split = item.split('/')
                    if item_split[0] == "record:host":
                        host_obj = self.ib_session.get(self.ib_url + f'record:host?name~='
                                                                     f'{item_split[1].split(":")[1]}'
                                                                     f'&_return_fields%2B=aliases',
                                                     auth=(auth.InfobloxAPI.username, auth.InfobloxAPI.password))
                        response = self._process_get_response(host_obj)
                        if response:
                            host_objects += response
                        continue
                    elif item_split[0] == "record:a":
                        arecord_obj = self.ib_session.get(self.ib_url + "record:a?name~=" + item_split[1].split(":")[1],
                                                     auth=(auth.InfobloxAPI.username, auth.InfobloxAPI.password))
                        response = self._process_get_response(arecord_obj)
                        if response:
                            arcord_object += response
                        continue
                if len(host_objects) >= 2:
                    self.multiple_hosts = True
                    self.host_object = host_objects
                    self._check_multiple_hosts()
                if len(host_objects) == 0 and len(arcord_object) > 0:
                    self.missing_host_record = True
                    self.arecord_object = arcord_object
                else:
                    self.host_object = host_objects[0]
                if len(host_objects) == 0:
                    self.missing_host_record = True
                if len(arcord_object) >= 2:
                    self.multiple_arecord = True
                self.arecord_object = arcord_object
                self._get_cname_from_record()
        except Exception as e:
            logger.info(f"Pulling Records From InfoBlox for {self.switch.ip} - Failed")
            logger.debug("THERE IS NO OBJECTS FIELD FOR THIS IP")
            logger.error(e, exc_info=True)
            pass
        else:
            logger.info(f"Pulling Records From InfoBlox for {self.switch.ip} - Success")
    def change_infoblox_fields(self):
        """
        Performs the act of changing the names of a switch in Infoblox through use of its API

        <function descriptor><number>-<building number><building code>-<room number>-<node>
        <function descriptor><number>-<building number>
        Args:
            Switch: A Switch Object containing strings that will be used as the new names of the switch in each
               specified DNS record in Infoblox

        Returns:
            The Node URI as a string.
        """
        logger.info(f"Updating Infoblox for: {self.switch.ip} to {self.AuthoritativeName} - Starting")
        try:
            # List of buildings that keep their own DNS records, do not change these buildings' records
            buildings_to_not_change = ["6", "8", "25", "26", "36", "48", "57", "61", "72", "73", "84", "85", "87",
                                       "006",
                                       "008", "025", "026", "036", "048", "057", "061", "072", "073", "084", "085",
                                       "087"]

            # Checks if the Infoblox Record is in the DO NOT Change list
            if f'{self.switch.buildnumber}' in buildings_to_not_change:
                logger.info(f"{self.switch.ip}: self.switch Building Number Found in DO NOT CHANGE list")
                return
            headers = {'content-type': "application/json"}
            #updatge Host Records:
            if self.host_object: #if a record exists already than update old record.
                put_data = self.host_object
                if '.net.utah.edu' in put_data['name']:
                    put_data['name'] = self.AuthoritativeName + '.net.utah.edu'
                elif '.med.utah.edu' in put_data['name']:
                    put_data['name'] = self.AuthoritativeName + '.med.utah.edu'
                if 'ipv4addrs' in put_data:
                    del put_data['ipv4addrs']
                response = self._process_put_response(self.ib_session.put(self.ib_url + put_data['_ref'],
                                    auth=(auth.InfobloxAPI.username, auth.InfobloxAPI.password),
                                    data=json.dumps(put_data), headers=headers))

                response = self._process_get_response(self.ib_session.get(self.ib_url + "record:host?name~=" +
                                                                          self.AuthoritativeName,
                                             auth=(auth.InfobloxAPI.username, auth.InfobloxAPI.password)))
                if response:
                    self.host_object = response[0]
                else: # object was not created.
                    metrics_logger.info(f'{self.switch.ip}: InfoBlox Name host record - updated')
            if self.arecord_object:
                for arecord in self.arecord_object:# delete A records
                    put_data = arecord
                    response = self._process_delete_response(self.ib_session.delete(self.ib_url + put_data['_ref'],
                                        auth=(auth.InfobloxAPI.username, auth.InfobloxAPI.password)),put_data)
                    metrics_logger.info(f'{self.switch.ip}: InfoBlox Name arecord - deleted')
        except Exception as e:
            logger.info(f"Updating Infoblox for: {self.switch.ip}  to {self.AuthoritativeName} - Failed")
            logger.error(e, exc_info=True)
            pass
        else:
            logger.info(f"Updating Infoblox for: {self.switch.ip} to {self.AuthoritativeName} - Success")
        return
    def _delete_hosts(self):
        """

        Returns:

        """
        if self.wronghost:  # delete any incorrect Cnames
            for hostname, obj in self.wronghost.items():
                try:
                    response = self._process_delete_response(self.ib_session.delete(self.ib_url + obj['_ref'],
                                                                                    auth=(auth.InfobloxAPI.username,
                                                                                          auth.InfobloxAPI.password)),
                                                             obj)
                except Exception as e:
                    logger.info(
                        f"Deleting Record Infoblox for: {obj['name']} - Failed")
                    logger.error(e,exc_info=e)
                    raise
                else:
                    metrics_logger.info(
                        f"{self.switch.ip} Deleting Host Record - Success")
    def _delete_cname(self):
        """

        Returns:

        """
        if self.wrongcnames:  # delete any incorrect Cnames
            for cname, obj in self.wrongcnames.items():
                try:
                    response = self._process_delete_response(self.ib_session.delete(self.ib_url + obj['_ref'],
                                                                                    auth=(auth.InfobloxAPI.username,
                                                                                          auth.InfobloxAPI.password)),
                                                             obj)
                except Exception as e:
                    logger.info(
                        f"Deleting Record Infoblox for: {obj['name']} - Failed")
                    logger.error(e,exc_info=e)
                    raise
                else:
                    metrics_logger.info(
                        f"{self.switch.ip} Deleting Cname Record - Success")
    def _process_put_response(self,response):
        """

        Args:
            response:

        Returns:

        """
        if response.status_code != 200:  # object was not created
            pass
        else:
            return response.json()
    def _process_post_response(self, response):
        """

        Args:
            response:

        Returns:

        """
        if response.status_code != 201:  # failed to create record
           raise NameError (response.text)
        else:
            return response.json()
    def _process_delete_response(self,response,obj):
        """
        Process the delete response from Infoblox API
        Args:
            response:

        Returns:
        """
        if response.status_code != 200:
            raise NameError (response.text)
        try:
            response_2 = self._process_get_response(self.ib_session.get(
                self.ib_url + obj['_ref'],
                auth=(auth.InfobloxAPI.username, auth.InfobloxAPI.password)))
        except LookupError as L:
            return response.json() #successfully deleted record
        else:
            return response_2 # unsuccessful at deleting record.
    def _update_cname_infoblox(self):
        """
        Deletes all wrong entries of cnames, and creates the correct cnames to the new authoritative name record
        Args:
            Switch:

        Returns:

        """
        logger.info(f"Updating Cname Record Infoblox for: {self.switch.ip}  to {self.AuthoritativeName} - Starting")
        try:
            if not self.cname1check:
                putdata_1 = None
                if self.cname1 and self.host_object:
                    putdata_1 = {'canonical': self._remove_domains(self.host_object['name']),
                                 'name': self.cname1.lower(),
                                 'view': 'Internal'}
                    if '.net.utah.edu' in self.host_object['name']:
                        putdata_1['name'] = self.cname1 + '.net.utah.edu'
                    elif '.med.utah.edu' in self.host_object['name']:
                        putdata_1['name'] = self.cname1 + '.med.utah.edu'
                if putdata_1: #create the correct Cname Records
                    try:
                        response = self._process_post_response(self.ib_session.post(url=self.ib_url + 'record:cname',data=putdata_1,
                                                    auth=(auth.InfobloxAPI.username, auth.InfobloxAPI.password)))
                    except Exception as e:
                        logger.info(
                            f"Updating Cname 1 Record Infoblox for: {self.switch.ip} - Failed")
                    else:
                        logger.info(
                            f"{self.switch.ip} Updating Cname 1 Record Infoblox - Success")

            if not self.cname2check:
                putdata_2 = None
                if self.cname2 and self.host_object['name']:
                    putdata_2 = {'canonical': self._remove_domains(self.host_object['name']),
                                 'name': self.cname2.lower(),
                                 'comment': 'Testing Script Cname Creation',
                                 'view': 'Internal'}
                    if '.net.utah.edu' in self.host_object['name']:
                        putdata_2['name'] = self.cname2 + '.net.utah.edu'
                    elif '.med.utah.edu' in self.host_object['name']:
                        putdata_2['name'] = self.cname2 + '.med.utah.edu'
                if putdata_2: #create the correct Cname Records
                    try:
                        response = self._process_post_response(self.ib_session.post(url=self.ib_url + 'record:cname', data=putdata_2,
                                                        auth=(auth.InfobloxAPI.username, auth.InfobloxAPI.password)))
                    except Exception as e:
                        logger.info(
                            f" Failed: Updating Cname 2 Record Infoblox for: {self.switch.ip}")
                    else:
                        logger.info(
                            f"Success: Updating Cname 2 Record Infoblox for: {self.switch.ip}")

        except Exception as e:
            logger.info(f"Updating Cname Record Infoblox for: {self.switch.ip}  to {self.AuthoritativeName} - Failed")
            logger.error(e, exc_info=True)
            pass
    def _search_for_cname_record(self,record):
        cname = self.ib_session.get(self.ib_url + "record:cname?canonical=" + record,
                                    auth=(auth.InfobloxAPI.username, auth.InfobloxAPI.password))
        cname = self._process_get_response(cname)
        if cname:
            if self.cname_objects:
                ref_set = set()
                for cn in self.cname_objects:
                    ref_set.add(cn['_ref'])

                for recname in cname:
                    if recname['_ref'] in ref_set:
                        continue
                    else:
                        self.cname_objects.append(recname)
            else:
                self.cname_objects += cname
    def _get_cname_from_record(self):
        """
        Using both a records, and host records we look for cnames pointing to any of them. Add them to the switch object
        Args:
            record:

        Returns:

        """
        try:
            if self.host_object:# collect Cnames
                if self.multiple_hosts:
                    for name,host in self.righthost.items():
                        self._search_for_cname_record(host['name'])
                        self._search_for_cname_record(self._remove_domains(host['name']))
                    if self.wronghost:
                        for name, host in self.wronghost.items():
                            self._search_for_cname_record(host['name'])
                            self._search_for_cname_record(self._remove_domains(host['name']))
                else:
                    self._search_for_cname_record(self.host_object['name'])
                    self._search_for_cname_record(self._remove_domains(self.host_object['name']))

            if self.arecord_object:  # collect Cnames from arecords
                for arecord in self.arecord_object:
                    self._search_for_cname_record(arecord['name'])
                    self._search_for_cname_record(self._remove_domains(arecord['name']))
        except Exception as e:
            logger.error(e, exc_info=True)
            pass
        else:
            pass
    def _process_get_response(self,response):
        """
        Handles for standard connection errors from Infoblox API. Reads information, and sends back lists of dictionaries
        Args:
            response:
        Returns:
        """
        if response.status_code != 200:
            raise LookupError("Something went wrong")
        if len(response.json()) != 0:  # something to read
            return response.json()
        else: # nothing to read
            return
    def _delete_aliases(self):
        """
        Returns:

        """
        try:
            headers = {'content-type': "application/json"}
            put_data = self.host_object
            put_data['aliases'] = []
            if 'ipv4addrs' in put_data:
                del put_data['ipv4addrs']
            response = self._process_put_response(self.ib_session.put(self.ib_url + put_data['_ref'],
                                                                      auth=(auth.InfobloxAPI.username,
                                                                            auth.InfobloxAPI.password),
                                                                      data=json.dumps(put_data), headers=headers))

            response = self._process_get_response(self.ib_session.get(self.ib_url + "record:host?name~=" +
                                                                      self.AuthoritativeName + '&_return_fields%2B=aliases',
                                                                      auth=(auth.InfobloxAPI.username,
                                                                            auth.InfobloxAPI.password)))
            if response:
                if 'aliases' in response[0]:
                    if response[0]['aliases']:
                        raise NameError("Not able to remove Aliases")
        except Exception as e:
            logger.info(
                f"Failed: Deleting Alias for: {self.switch.ip}")
        else:
            logger.info(
                f"Success: Deleting Alias Infoblox for:{self.switch.ip}")
    def _modify_host_view(self):
        """

        Returns:
        """
        headers = {'content-type': "application/json"}
        obj = self.host_object
        del_response = self._process_delete_response(self.ib_session.delete(self.ib_url + obj['_ref'],
                                                                        auth=(auth.InfobloxAPI.username,
                                                                          auth.InfobloxAPI.password)),obj)
        if not isinstance(del_response,str): # was not deleted
            pass
        obj['view'] = 'Internal'
        obj["ipv4addrs"] = [{"ipv4addr": self.switch.ip}]
        obj["extattrs"] = {'Device Type': {"value": "Switch"}}
        obj = json.dumps(obj)
        try:
            try:
                put_response = self._process_post_response(self.ib_session.post(self.ib_url + 'record:host',
                                                                      auth=(auth.InfobloxAPI.username,
                                                                            auth.InfobloxAPI.password),
                                                                      data=obj, headers=headers))
            except NameError as n:
                raise
            else:
                response = self._process_get_response(self.ib_session.get(self.ib_url + "record:host?name~=" +
                                                                          self.AuthoritativeName,
                                                                          auth=(auth.InfobloxAPI.username,
                                                                                auth.InfobloxAPI.password)))
                if response:
                    self.host_object = response[0]
                else:  # object was not created.
                    logger.info(
                        f"{self.switch.ip} Updating Host Record to Internal - Success")

        except Exception as e:
            logger.info(
                f"Updating Host Record to Internal: {self.switch.ip} - Failed")
        else:
            logger.info(
                f"{self.switch.ip} Updating Host Record to Internal - Success")


    #####################################################Orion##############################################################
    def change_orion_fields(self):
        """
        Change a Node name by IP. If a database/Node ID is given, search with
        that instead.

        Args:
            Swtich: A Switch Object containing strings that will be used as the new names of the switch in Monitoring

        Return:
            None
        """
        logger.info(f"Updating Orion for: {self.switch.ip} to {self.AuthoritativeName} - Starting")
        try:
            dbid = self._get_switch_from_orion(self.switch.ip)['NodeID']

            # get URI to be able to access the specific entry in Monitoring
            uri = self._get_orion_uri(dbid)

            # add node properties, separately done for each prop because Monitoring api restricts these properties from being
            # updated at once
            props = {}
            props['Caption'] = self.AuthoritativeName
            result = self.orionapi.update(uri, **props)  # Change Caption
            props.clear()
            props['DisplayName'] = self.AuthoritativeName
            result = self.orionapi.update(uri, **props)  # Change DisplayName
            props.clear()
            props['SysName'] = self.AuthoritativeName
            result = self.orionapi.update(uri, **props)  # Change SysName
            props.clear()
            props['NodeName'] = self.AuthoritativeName
            result = self.orionapi.update(uri, **props)  # Change NodeName

            # Used as testing to visually verify a change took place in the database
            orionswitch = self.orionapi.query("SELECT (Caption, DNS, SysName, NodeName, DisplayName) " +
                                              "FROM Orion.Nodes WHERE Vendor='Cisco' AND " +
                                              "(DNS LIKE 'dx%' OR DNS LIKE 'sx%') AND ip= '" + self.switch.ip + "'")
            odict = orionswitch['results'][0]

            if odict['Caption'] != self.AuthoritativeName:
                raise ValueError(f"Caption Name Not updated:{odict['Caption']} should be {self.AuthoritativeName}")
            if odict['DisplayName'] != self.AuthoritativeName:
                raise ValueError(f"DisplayName Name Not updated:{odict['DisplayName']} should be {self.AuthoritativeName}")
            if odict['SysName'] != self.AuthoritativeName:
                raise ValueError(f"SysName Name Not updated:{odict['SysName']} should be {self.AuthoritativeName}")
            if odict['NodeName'] != self.AuthoritativeName:
                raise ValueError(f"NodeName Name Not updated:{odict['NodeName']} should be {self.AuthoritativeName}")
        except ValueError as v:
            #handle not updated Monitoring info.
            pass
        except Exception as e:
            logger.info(f"Updating Orion for: {self.switch.ip} to {self.AuthoritativeName} - Failed")
            logger.error(e, exc_info=True)
            pass
        else:
            logger.info(f"Updating Orion for: {self.switch.ip} to {self.AuthoritativeName} - Success")
            metrics_logger.info(f"Success - Updating Orion for: {self.switch.ip}")
    def _get_orion_uri(self, nodeid):
        """
        Get the Solarwinds URI from the Node ID.

        Args:
            nodeid: Node ID as an integer.

        Returns:
            The Node URI as a string.
        """
        results = self.orionapi.query("SELECT Uri FROM Orion.Nodes WHERE NodeID=" + str(nodeid))
        return self._parse_orion_results(results)[0]['Uri']
    def _get_switch_from_orion(self, ip=None, dns_name=None):
        """
        Get switch information by either IP, property tag, or barcode.
        This will return switch information.

        Note that all arguments are optional; however, at least one must be used
        to filter results.

        Args:
            ip: IP address of the switch as a string.
            dns_name: DNS/hostname as a string.

        Returns:
            A SwitchData object with the most relevant switch returned.
        """
        result = ""
        query = "SELECT (Uri, NodeID, IP, DNS, NodeName, Caption, DisplayName, SysName) FROM Orion.Nodes "
        if ip:
            ip = ip.split('/')[0]
            result = self.orionapi.query(query + "WHERE IP = '" + ip + "'")
        elif dns_name:
            result = self.orionapi.query(query + "WHERE DNS LIKE '%" + dns_name + "%'")
        else:
            raise ValueError("no information given")

        try:
            result = self._parse_orion_results(result)[0]
        except:
            print("Orion node for " + ip + " does not exist.")

        return result
    def _parse_orion_results(self, result):
        """
        Internal function: get actual data from the SWIS response string, or
        throw an error if one is encountered.

        Args:
            result: Response dictionary from Orion's SWIS.

        Returns:
            The response string if available. Otherwise raise
            OrionObjectExceptions.
        """
        if result.get('results', None) is None:
            raise self.OrionObjectException("Error querying node: " + str(result))
        elif not result['results']:
            raise self.OrionObjectException("Node does not exist")
        elif len(result['results']) == 0:
            return None

        return result['results']
    def _get_keyboard_name(self):
        self._name_mapping()
        if self.AuthoritativeName == None:
            while True:
                self.AuthoritativeName = input("Please Enter Correct Name:")
                if '\n' in self.AuthoritativeName:
                    self.AuthoritativeName.rstrip('\r')
                    break
                elif self.AuthoritativeName:
                    break
        else:
            return

###################################################Switch#############################################################
    def _check_multiple_hosts(self):
        """

        Returns:

        """
        try:
            for host in self.host_object: # sort which host names to keep
                if ".net.utah.edu" in host['name']:
                    self.righthost[host['name']] = host
                elif ".med.utah.edu" in host['name']:
                    self.wronghost[host['name']] = host
                elif self._remove_domains(host['name']) == self.AuthoritativeName:
                    self.righthost[host['name']] = host
                elif self._remove_domains(host['name']) != self.AuthoritativeName:
                    self.wronghost[host['name']] = host
            if len(self.righthost) == 1:
                for key, value in self.righthost.items():
                    self.host_object = value
                    break
            elif len(self.righthost) >= 2:
                for key, value in self.righthost.items():
                    self.host_object = value
                    break
            elif len(self.righthost) == 0:
                for key, value in self.wronghost.items():
                    self.host_object = value
                    break
        except Exception as e:
            logger.error(e, exc_info=True)
            pass
    def _check_cname(self):
        """

        Args:
            switch:

        Returns:
        """
        try:
            if self.host_object is not None:
                if 'aliases' in self.host_object:
                    if self.host_object['aliases']:
                        self.aliascheck = True
            if 'dx' in self.AuthoritativeName:
                self._check_2_cname_policy() #check 2 cname policy
            elif 'sx' in self.AuthoritativeName:
                if hasattr(self, "cname_objects"):
                    if self.cname_objects:
                        if len(self.cname_objects) > 0: #shouldn't be any Cname Records
                            for cname in self.cname_objects:
                                self.wrongcnames[cname['name']] = cname
            elif 'dvpn' in self.AuthoritativeName:
                self._check_2_cname_policy() #check 2 cname policy
            elif 'dmx' in self.AuthoritativeName:
                self._check_2_cname_policy() #check 2 cname policy
        except Exception as e:
            logger.error(e,exc_info=True)
            pass
    def _check_domain_of_cname(self,name,cname):
        if name == cname + '.net.utah.edu':
            return True
        elif name == cname + '.med.utah.edu':
            return False
    def _check_2_cname_policy(self):
        """

        Args:
            switch:

        Returns:

        """
        try:
            namesplit = self.AuthoritativeName.split('-')
            self.cname1 = f"{namesplit[0]}-{self.switch.buildnumber}".lower()
            self.cname2 = f"{namesplit[0]}-{self.switch.buildnumber}{self.switch.buildingname}".lower()
            if hasattr(self, "cname_objects"):
                if self.cname_objects:
                    if len(self.cname_objects) >= 2:  # should have two cnames pointing at the host record
                        metrics_logger.info(f'{self.switch.ip}: Infoblox Cname Records - Has Both')
                        for cname in self.cname_objects:
                            if self._remove_domains(cname["name"]) == self.cname1:
                                if self._check_domain_of_cname(cname["name"],self.cname1):
                                    metrics_logger.info(f'{self.switch.ip}: Infoblox Cname Records - Correct Cname1')
                                    self.cname1check = True
                                    self.rightcnames[f'{cname["name"]}'] = cname
                                    continue
                                else:
                                    metrics_logger.info(f'{self.switch.ip}: Infoblox Cname Records - Incorrect')
                                    continue
                            elif self._remove_domains(cname["name"]) == self.cname2:
                                if self._check_domain_of_cname(cname["name"],self.cname2):
                                    metrics_logger.info(f'{self.switch.ip}: Infoblox Cname Records - Correct Cname2')
                                    self.cname2check = True
                                    self.rightcnames[f'{cname["name"]}'] = cname
                                    continue
                                else:
                                    metrics_logger.info(f'{self.switch.ip}: Infoblox Cname Records - Incorrect')
                                    continue
                        for cname in self.cname_objects:
                            if cname['name'] not in self.rightcnames:
                                metrics_logger.info(f'{self.switch.ip}: Infoblox Cname Records - Incorrect')
                                self.wrongcnames[f"{cname['name']}"] = cname
                    elif len(self.cname_objects) == 1:
                        if self._remove_domains(self.cname_objects[0]['name']) == self.cname1:
                            if self._check_domain_of_cname(self.cname_objects[0]['name'],self.cname1):
                                metrics_logger.info(f'{self.switch.ip}: Infoblox Cname Records - Correct Cname1')
                                self.cname1check = True  # passed the check
                                self.rightcnames[f"{self.cname_objects[0]['name']}"] = self.cname_objects[0]
                            else:
                                metrics_logger.info(f'{self.switch.ip}: Infoblox Cname Records - Incorrect')
                                self.wrongcnames[f"{self.cname_objects[0]['name']}"] = self.cname_objects[0]
                        elif self._remove_domains(self.cname_objects[0]['name']) == self.cname2:
                            if self._check_domain_of_cname(self.cname_objects[0]['name'],self.cname2):
                                metrics_logger.info(f'{self.switch.ip}: Infoblox Cname Records - Correct Cname2')
                                self.cname2check = True  # passed the check
                                self.rightcnames[f"{self.cname_objects[0]['name']}"] = self.cname_objects[0]
                            else:
                                metrics_logger.info(f'{self.switch.ip}: Infoblox Cname Records - Incorrect')
                                self.wrongcnames[f"{self.cname_objects[0]['name']}"] = self.cname_objects[0]
                        else:
                            metrics_logger.info(f'{self.switch.ip}: Infoblox Cname Records - Incorrect')
                            self.wrongcnames[f"{self.cname_objects[0]['name']}"] = self.cname_objects[0]
                else:
                    metrics_logger.info(f'{self.switch.ip}: Infoblox Cname Records - Missing Both')
            else:
                metrics_logger.info(f'{self.switch.ip}: Infoblox Cname Records - Missing Both')
        except Exception as e:
            logger.error(e,exc_info=True)
            pass
    def _update_function_descriptor(self):
        """
        Checks for terms in names, and updates the function descriptors correctly.
        Returns:
        """
        if ("services" in self.switch.hostname
               or 'services' in self.orion_name):
            if self.switch.function_descriptor == 'dx':
                self.switch.function_descriptor = 'dsx'
                self.switch.description = 'Distribution Services Switch'
            elif self.switch.function_descriptor == 'sx':
                self.switch.function_descriptor = 'ssx'
                self.switch.description = 'Services Sub Access Layer Switch'
    def get_Switch_Data(self):
        """
        Reaches out to the switch to gather the Banner Name, and Host name of the switch.
        Assignes the Banner, and host name to the switch object
        :return:
        """
        logger.info(f"Getting Switch Bannername/Hostname - Starting")
        try:
            self.switch.login()
            self.switch.get_run_data()
            self.switch.sortRun(self.switch.run_result)
            if self.switch.hostname is None:
                raise ValueError(f"Switch not assigned a Host Name")
        except paramiko.ssh_exception.NoValidConnectionsError as p:
            raise
        except IOError as i:
            raise
        except AssertionError as a:
            raise
        except Exception as e:
            logger.info(f"Getting Switch Bannername/Hostname - Failed")
            logger.error(e, exc_info=True)
            pass
        else:
            logger.info(f"Getting Switch Bannername/Hostname - Success")
    def change_Switch_fields(self, updatestring):
        """
        This function takes the switch object, and updates the Banner name or hostname on the switch
        :param updatestring: The Update String
        :param Switch: The Switch Object with the correct information
        :return (Switch): The Switch object
        """
        if len(updatestring) > 75:
            updatefield = 'Bannername'
        else:
            updatefield = 'Hostname'

        logger.info(f"Updating Switch {updatefield} on: {self.switch.ip} to {self.AuthoritativeName} - Starting")
        try:
            self.switch.login()
            result = self.switch.conn.send_command(f'Config t')
            if not len(updatestring) > 75:
                self.switch.conn.update_prompts(self.AuthoritativeName)
            result = self.switch.conn.send_command(f'{updatestring}')
            result = self.switch.conn.send_command(f'end')
            result = self.switch.conn.send_command(f'wri')

            if updatefield == 'Hostname':
                result = self.switch.conn.send_command(' ', trim=False)
                if self.AuthoritativeName in result:
                    metrics_logger.info(f"{self.switch.ip}: Hostname updated - Success")
            else:
                result = self.switch.conn.send_command('show run | begin banner')
                if self.AuthoritativeName in result:
                    metrics_logger.info(f"{self.switch.ip}: BannerName updated - Success")

        except Exception as e:
            logger.info(f"Updating self.switch {updatefield} on: {self.switch.ip} to {self.AuthoritativeName} - Failed")
            logger.error(e, exc_info=True)
            self.switch.logout(self.switch.conn)
            pass
        else:
            logger.info(f"Updating self.switch {updatefield} on: {self.switch.ip} to {self.AuthoritativeName} - Success")
            self.switch.logout(self.switch.conn)

#####################################################Main###############################################################
    def _create_authoritative_name(self,switch):
        """
        Issues the get request to the TOAST API and calls process_get to process that information from the
        HTTP response.

        Args:
            uri: Uri that is used in the call to the api to get the data from the TOAST switch checker
            dns: The dns name on file for the switch
        """
        logger.info(f'Generating Authoritatize name - Starting')
        try:
            Authoritative_name = None
            if switch.hostname:
                if switch.buildnumber != None and switch.buildingname != None:
                    if switch.buildnumber == '3574' or switch.buildingname == 'ddc' or switch.buildingname == 'tdc' or switch.buildnumber == '3475':  # process Data Center Switches_syntax_compatability:
                        if (switch.buildingname
                                and switch.function_descriptor_number
                                and switch.buildnumber
                                and switch.racknumber
                                and switch.function_descriptor
                                and switch.node):
                            # <function descriptor><number>-<building name>-<rack location>.net.utah.edu
                            # create the authoritative name
                            self._update_function_descriptor()
                            Authoritative_name = f"{switch.function_descriptor}{switch.function_descriptor_number}-" \
                                                 f"{switch.buildingname}-{switch.racknumber}-{switch.node}"
                            logger.info(f'Generating Authoritatize name - Success')
                            return Authoritative_name
                    elif hasattr(switch,'address') and switch.address is not None: # process access layer devices with address info
                        if (switch.buildingname and switch.buildnumber and switch.roomnumber
                            and switch.description and switch.node):
                            #<function descriptor><number>-<address>_<building number><building code>-<room number>-<node>.net.utah.edu
                            self._update_function_descriptor()
                            Authoritative_name = f"{switch.function_descriptor}{switch.function_descriptor_number}-" \
                                             f"{switch.address}_" \
                                             f"{switch.buildnumber}{switch.buildingname}-{switch.roomnumber}-{switch.node}"
                            logger.info(f'Generating Authoritatize name - Success')
                            return Authoritative_name
                    elif (switch.buildingname and switch.buildnumber and switch.roomnumber
                        and switch.description and switch.node): # process access layer devices
                        #<function descriptor><number>-<building number><building code>-<room number>-<node>.net.utah.edu
                        self._update_function_descriptor()
                        Authoritative_name = f"{switch.function_descriptor}{switch.function_descriptor_number}-" \
                                             f"{switch.buildnumber}{switch.buildingname}-{switch.roomnumber}-{switch.node}"
                        logger.info(f'Generating Authoritatize name - Success')
                        return Authoritative_name
                    elif ("airmed" in self.switch.hostname
                                or 'airmed' in self.orion_name):
                        if switch.buildingname and switch.buildnumber:
                            self.switch.function_descriptor = 'dvpn'
                            self.switch.description = 'Demarc and VPN'
                            self.switch.node = 'hscp2p'
                            Authoritative_name = f"{switch.function_descriptor}-" \
                                                 f"{switch.buildnumber}{switch.buildingname}-airmed-{switch.node}"
                            logger.info(f'Generating Authoritatize name - Success')
                            return Authoritative_name
                    else:
                        pass
        except ValueError as v:
            logger.error(v, exc_info=True)
            raise
        except Exception as e:
            logger.info(f'Generating Authoritatize name - Failed')
            logger.error(e, exc_info=True)
            pass
        else:
            pass
    def create_name_update_excel(self):
        try:
            self.gather_all_Data()

            if self.skipswitch:
                metrics_logger.info(f"{self.switch.ip}: Unable to update all names")
                updatestring = f""" IP Address: {self.switch.ip}
                ----------------------------------------------------------------------------
                SKIPPING DEVICE NOT ABLE TO SSH INTO DEVICE
                """
                return updatestring
            else:
                # Compare the names from all sources, and check them against our standards
                self.check_names()
            wrong_host_strings = ""
            for key,host in self.wronghost.items():
                update_host_str = f"""Host Record: {self._remove_domains(host['name'])} -- {host['view']} --> Delete --> None -- None """
                wrong_host_strings += update_host_str
            wrong_cname_strings = ""
            for key,cname in self.wrongcnames.items():
                update_cname_str = f"""Cname Record: {self._remove_domains(cname['name'])} -- None --> Delete --> None -- None """
                wrong_cname_strings += update_cname_str
            wrong_arecord_strings = ""
            for arecord in self.arecord_object:
                update_arecord_str = f"""A Record: {self._remove_domains(arecord['name'])} -- {arecord['view']} --> Delete --> None -- None """
                wrong_arecord_strings += update_arecord_str
            cname1_string = ''
            if self.cname1 is not None and self.cname1check == True:
                cname1_string = f"""Cname_1: None -- None --> Create --> {self.cname1} -- Internal"""
            cname2_string = ''
            if self.cname2 is not None and self.cname2check == True:
                cname2_string = f"""Cname_2: None -- None --> Create --> {self.cname1} -- Internal"""
            host_record_str = ''
            if self.missing_host_record:
                host_record_str = f"""Host Record: None -- None --> create --> {self.AuthoritativeName} -- Internal """
            else:
                host_record_str = f"""Host Record: {self._remove_domains(self.host_object['name'])} --> {f'change --> {self.AuthoritativeName}' if self.infoblox == True else 'None --> None' }"""
            if self.switch.bannername == None:
                bannername = f"None --> create --> {self.AuthoritativeName}"
            else:
                bannername = f"{self._remove_domains(self.switch.bannername)} --> {f'change --> {self.AuthoritativeName}' if self.switchbanner == False else 'None --> None' }"
            updatestring = f""" IP Address: {self.switch.ip}
----------------------------------------------------------------------------
___ Names on the Switch ___
Field: Old Name --> Action --> New Name
Hostname: {self._remove_domains(self.switch.hostname)} --> {f'change --> {self.AuthoritativeName}' if self.switchhost == False else 'None --> None' }
Bannername: {bannername}

___ Orion Names ____
Field: Old Name --> Action --> New Name
Caption: {self._remove_domains(self.orion_name)} --> {f'change --> {self.AuthoritativeName}' if self.orion == False else 'None --> None' }


___ Infoblox Names ____
Field: Old Name -- Old View --> Action --> New Name -- New View
{host_record_str}
{cname1_string}
{cname2_string}
{wrong_arecord_strings}
{wrong_cname_strings}
{wrong_host_strings}"""
        except Exception as e:
            logger.error(e, exc_info=True)
            raise
        else:
            return updatestring
    def check_names(self):
        """
        Compares the names from InfoBlox, Orion, Switch Hostname, And Banner name together to see if they are the same.
        Also checks to see if these names are following the correct naming convention

        Naming Policy for Access Layer:
        <function descriptor><number>-<building number><building code>-<room number>-<node>.net.utah.edu

        For those that have an address for the building code:

        <function descriptor><number>-<building number><building code>-<room number>-<node>.net.utah.edu
        Example: dx1-892_585komas-101-ebc.net.utah.edu

        """
        logger.info(f"Checking names - Starting")
        try:
            # compare all of the names to each other.
            assert hasattr(self, 'host_object'), f'{self.switch.ip}: Missing host entry'
            assert hasattr(self.switch, 'hostname'), f'{self.switch.ip}: Hostname not Assigned'
            assert hasattr(self, 'orion_name'), f'{self.switch.ip}: orion_name not Assigned'
            if self.missing_host_record:
                if (self._remove_domains(self.switch.bannername) ==
                        self._remove_domains(self.switch.hostname) ==
                        self._remove_domains(self.orion_name)):
                    metrics_logger.info(f"{self.switch.ip}: Names are Consistent in all Locations")
                    self.NameEqual_check = True
                else:
                    metrics_logger.info(f"{self.switch.ip}: Names are not Consistent in all Locations")
            else:
                if (self._remove_domains(self.switch.bannername) ==
                        self._remove_domains(self.switch.hostname) ==
                        self._remove_domains(self.host_object['name']) ==
                        self._remove_domains(self.orion_name)):
                    metrics_logger.info(f"{self.switch.ip}: Names are Consistent in all Locations")
                    self.NameEqual_check = True
                else:
                    metrics_logger.info(f"{self.switch.ip}: Names are not Consistent in all Locations")
            #find the correct name
            self.AuthoritativeName = self._create_authoritative_name(self.switch)
            if "mgmt" in self.switch.hostname:
                self._get_keyboard_name()
            if "airmed" in self.switch.hostname and 'dvpn' not in self.switch.hostname:
                self._get_keyboard_name()
            if self.AuthoritativeName == None: #process banner name if unsucessful
                # attempt to figure out what is missing
                if self.switch.bannername is not '':
                    switch = self.sort_name(self.switch, self._remove_domains(self.switch.bannername))
                    self.AuthoritativeName = self._create_authoritative_name(switch)
                if self.AuthoritativeName == None: #process Infoblox host record if unsucessful
                    if self.host_object == None:
                        for arecord in self.arecord_object:
                            switch = self.sort_name(self.switch, self._remove_domains(arecord['name']))
                            self.AuthoritativeName = self._create_authoritative_name(switch)
                            if self.AuthoritativeName == None:
                                continue
                            else:
                                break
                    else:
                        switch = self.sort_name(self.switch, self._remove_domains(self.host_object['name']))
                        self.AuthoritativeName = self._create_authoritative_name(switch)
                    if self.AuthoritativeName == None: #process Monitoring container name if unsucessful
                        switch = self.sort_name(self.switch, self._remove_domains(self.orion_name))
                        self.AuthoritativeName = self._create_authoritative_name(switch)
                        if self.AuthoritativeName == None:
                            self._get_keyboard_name()
            # compare all the names to the correct name to see what is wrong and what is right
            self.AuthoritativeName = self.AuthoritativeName.lower()

            if self.switchbanner != None:
                if self._remove_domains(self.switch.bannername) != self.AuthoritativeName:
                    metrics_logger.info(f'{self.switch.ip}: BannerName - Incorrect')
                else:
                    metrics_logger.info(f'{self.switch.ip}: BannerName - Correct')
                    self.switchbanner = True

            # compare Hostname to Correct name
            if self._remove_domains(self.switch.hostname) != self.AuthoritativeName:
                metrics_logger.info(f'{self.switch.ip}: HostName - Incorrect')
            else:
                metrics_logger.info(f'{self.switch.ip}: HostName - Correct')
                self.switchhost = True

            # compare Infoblox Host Record name to Correct name
            if self.host_object is not None:
                if self._remove_domains(self.host_object['name']) != self.AuthoritativeName:
                    metrics_logger.info(f'{self.switch.ip}: InfoBlox Name - InCorrect')
                if self.arecord_object:
                    metrics_logger.info(f'{self.switch.ip}: InfoBlox Name has arecord')
                else:
                    metrics_logger.info(f'{self.switch.ip}: InfoBlox Name - Correct')
                    self.infoblox = True

                if self.host_object['view'] == 'External':
                    metrics_logger.info(f'{self.switch.ip}: InfoBlox host record set to Internal - InCorrect')
                    self.external_host_object = True
                else:
                    metrics_logger.info(f'{self.switch.ip}: InfoBlox host record set to Internal - Correct')

            # Compare Orion name to correct name
            if self._remove_domains(self.orion_name) != self.AuthoritativeName:
                metrics_logger.info(f'{self.switch.ip}: Orion Name - Incorrect')
            else:
                metrics_logger.info(f'{self.switch.ip}: Orion Name - Correct')
                self.orion = True

            self._check_cname()
        except ValueError as v:
            logger.info(f"Checking names for: {self.switch.ip} - failed")
            pass
        except Exception as e:
            logger.info(f"Checking names for: {self.switch.ip} - failed")
            logger.error(e, exc_info=True)
            pass
    def get_node_from_building_number(self):
        """

        Returns:
        """
        try:
            if self.switch.node == None:
                if self.switch.buildnumber == '3574' and 'pdu' in self.switch.hostname.lower():
                    self.switch.node = 'ebc'
                    return
                elif self.switch.buildnumber:
                    with open('buildinglist_202007061623.csv',mode='r+') as csvfile:
                        readcsv = csv.reader(csvfile, delimiter=',',)
                        for count,row in enumerate(readcsv):
                            if count == 0:
                                continue
                            if int(self.switch.buildnumber) == int(row[0]):
                                if row[0] == '3701':
                                    self.switch.node = 'sjhc'
                                    return
                                elif row[0] == '482':
                                    self.switch.node = '102tower'
                                elif row[3].lower() == 'self':
                                    pass
                                else:
                                    self.switch.node = row[3].lower()
                                    return
        except Exception as e:
            logger.error(e,exc_info=True)
            pass

    def _name_mapping(self):
        for name in Switch.settings.name_mapping:
            if self.switch.hostname == name['hostname']:
                self.AuthoritativeName = name['newname']
                return

    def process_name(self):
        """
        Run this function to process the name for this device
        """
        # gathers all the data
        self.gather_all_Data()

        if self.skipswitch:
            metrics_logger.info(f"{self.switch.ip}: Unable to update all names")
            return
        else:
            # Compare the names from all sources, and check them against our standards
            self.check_names()
            # update names in all the locations
            self.update_names()
    def gather_all_Data(self):
        """
        Begins the collection phase of all the data from all the systems.
        For every switch in self.switches this function runs the functions to
        collect infomation from Infoblox, and from the switch
        Compiling the data into a switch object and rebuilding self.switches
        """
        logger.info(f"Gathering Data - Starting")
        try:
            logger.debug(f'Switch: {self.switch.ip} - Starting')
            # collects the data from Infoblox for all switches
            self.get_InfoBlox_data()
            # collects the Data from Orion for all switches in the list
            self.get_Switch_Data()
            self.get_building_info()
            self.get_node_from_building_number()

        except paramiko.ssh_exception.NoValidConnectionsError as N:
            self.skipswitch = True
            return
        except IOError as N:
            self.skipswitch = True
            return
        except AssertionError as a:
            pass
        except Exception as e:
            logger.debug(f'Switch: {self.switch.ip} - Failed')
            pass
        else:
            logger.debug(f'Switch: {self.switch.ip} - Success')
    def _check_portion(self,switch,portion):
        """
        checks if the portion is applied anywhere already
        Args:
            switch:
            portion:

        Returns:

        """
        if isinstance(portion,list):
            new_hostsplit = []
            for portion_2 in portion:
                if portion_2 == switch.address:
                    continue
                elif portion_2 == switch.buildingname:
                    continue
                elif portion_2 == switch.node:
                    continue
                elif portion_2 == switch.racknumber:
                    continue
                elif portion_2 == switch.roomnumber:
                    continue
                elif RepresentsInt(portion_2):
                    if portion_2 == switch.address:
                        continue
                    elif portion_2 == switch.buildnumber:
                        continue
                else:
                    new_hostsplit.append(portion_2)
            return new_hostsplit
        if isinstance(portion,str):
            if portion == switch.address:
                return
            elif portion == switch.buildingname:
                return
            elif portion == switch.node:
                return
            elif portion == switch.racknumber:
                return
            elif portion == switch.roomnumber:
                return
            elif RepresentsInt(portion):
                if portion == switch.address:
                    return
                elif portion == switch.buildnumber:
                    return
            else:
                return portion

    def sort_name(self,switch, hostname):
        """
        Gets room numbers, bldg numbers, rack numbers, and node information
        """
        try:
            pattern = re.compile("([0-9]{2,4}[A-Za-z]{2,10})")
            hostsplit = hostname.split("-")
            hostsplit = [x for x in hostsplit if x]
            if "_" in hostname:  # checks for address info
                hostsplit_a = hostname.split("_")
                result = self._check_portion(switch,hostsplit_a[0].split("-")[1])
                if result:
                    if RepresentsInt(result):
                        switch.address = result
                        hostname = re.sub(f"{switch.address}_", "", hostname)
                        hostsplit = hostname.split("-")
                        hostsplit = [x for x in hostsplit if x]
                        switch.function_descriptor = None
                        if "PoE" in hostsplit:
                            hostsplit.remove("PoE")
                        if "noc" in hostsplit:
                            hostsplit.remove("noc")
                        if 'airmed' in hostsplit:
                            hostsplit.remove('airmed')
                        for i in range(1, 10):
                            if f"sx{i}" in hostsplit[0]:
                                hostsplit.remove(f"sx{i}")
                                switch.function_descriptor_number = i
                                switch.function_descriptor = "sx"
                            elif f"SX{i}" in hostsplit[0]:
                                hostsplit.remove(f"SX{i}")
                                switch.function_descriptor_number = i
                                switch.function_descriptor = "sx"
                        for i in range(1, 3):
                            if f"dx{i}" in hostsplit[0]:
                                hostsplit.remove(f"dx{i}")
                                switch.function_descriptor_number = i
                                switch.function_descriptor = "dx"
                            elif f"DX{i}" in hostsplit[0]:
                                hostsplit.remove(f"DX{i}")
                                switch.function_descriptor_number = i
                                switch.function_descriptor = "dx"
                        for i in range(1, 3):
                            if f"r{i}" in hostsplit[0]:
                                hostsplit.remove(f"r{i}")
                                switch.function_descriptor_number = i
                                switch.function_descriptor = "r"
                            elif f"R{i}" in hostsplit[0]:
                                hostsplit.remove(f"R{i}")
                                switch.function_descriptor_number = i
                                switch.function_descriptor = "r"
                        if switch.function_descriptor:
                            switch.description = nwsettings.function_descriptors[switch.function_descriptor]
                        for abv in nwsettings.nodeabrlist:
                            if abv in hostsplit:
                                switch.node = abv
                                hostsplit.remove(abv)
                                break
                        for portion in hostsplit:
                            if pattern.match(portion):
                                hostsplit.remove(portion)
                                bldgsplit = re.split('(\d+)', portion)
                                bldgsplit = [x for x in bldgsplit if x]
                                switch.buildnumber = int(bldgsplit[0])
                                switch._pad_building_number()
                                switch.buildingname = bldgsplit[1]
                        if len(hostsplit) > 0:
                            hostsplit = self._check_portion(switch,hostsplit)
                            if hostsplit:
                                if len(hostsplit) == 1:  # most likely the room
                                    switch.roomnumber = hostsplit[0]
                                if len(hostsplit) == 2:
                                    switch.roomnumber = hostsplit[0]
                                    switch.racknumber = hostsplit[1]
            else:
                if "ddc" in hostname and not "3574ddc" in hostname:  # process Dataceneter names
                    # <function descriptor><number>-<building name>-<rack location>
                    switch.function_descriptor = ''.join([i for i in hostsplit[0] if not i.isdigit()])
                    switch.function_descriptor_number = int(re.sub(switch.function_descriptor, "", hostsplit[0]))
                    switch.description = nwsettings.function_descriptors[switch.function_descriptor]
                    switch.buildingname = hostsplit[1]
                    switch.buildnumber = '3574'
                    switch.racknumber = hostsplit[2]
                elif "3574ddc" in hostname:
                    switch.function_descriptor = ''.join([i for i in hostsplit[0] if not i.isdigit()])
                    switch.function_descriptor_number = int(re.sub(switch.function_descriptor, "", hostsplit[0]))
                    switch.description = nwsettings.function_descriptors[switch.function_descriptor]
                    switch.buildingname = hostsplit[1]
                    switch.buildnumber = '3574'
                    switch.racknumber = hostsplit[2]
                    switch.node = 'ebc'
                    for abv in nwsettings.nodeabrlist:
                        if abv in hostsplit:
                            switch.node = abv
                            hostsplit.remove(abv)
                            break
                elif "tdc" in hostname:
                    # <function descriptor><number>-<building name>-<rack location>
                    switch.function_descriptor = ''.join([i for i in hostsplit[0] if not i.isdigit()])
                    switch.function_descriptor_number = int(re.sub(switch.function_descriptor, "", hostsplit[0]))
                    switch.description = nwsettings.function_descriptors[switch.function_descriptor]
                    switch.buildingname = hostsplit[1]
                    switch.buildnumber = '3475'
                    switch.racknumber = hostsplit[2]
                elif not pattern.match(hostsplit[1]) and RepresentsInt(hostsplit[1]):  # process addresses locations in research park
                    if "PoE" in hostsplit:
                        hostsplit.remove("PoE")
                    if "noc" in hostsplit:
                        hostsplit.remove("noc")
                    if 'airmed' in hostsplit:
                        hostsplit.remove('airmed')
                    for i in range(1, 10):
                        if f"sx{i}" in hostsplit[0]:
                            hostsplit.remove(f"sx{i}")
                            switch.function_descriptor_number = i
                            switch.function_descriptor = "sx"
                        elif f"SX{i}" in hostsplit[0]:
                            hostsplit.remove(f"SX{i}")
                            switch.function_descriptor_number = i
                            switch.function_descriptor = "sx"
                    for i in range(1, 3):
                        if f"dx{i}" in hostsplit[0]:
                            hostsplit.remove(f"dx{i}")
                            switch.function_descriptor_number = i
                            switch.function_descriptor = "dx"
                        elif f"DX{i}" in hostsplit[0]:
                            hostsplit.remove(f"DX{i}")
                            switch.function_descriptor_number = i
                            switch.function_descriptor = "dx"
                    for i in range(1, 3):
                        if f"r{i}" in hostsplit[0]:
                            hostsplit.remove(f"r{i}")
                            switch.function_descriptor_number = i
                            switch.function_descriptor = "r"
                        elif f"R{i}" in hostsplit[0]:
                            hostsplit.remove(f"R{i}")
                            switch.function_descriptor_number = i
                            switch.function_descriptor = "r"
                    if switch.function_descriptor:
                        switch.description = nwsettings.function_descriptors[switch.function_descriptor]
                    switch.address = hostsplit[0]
                    hostsplit.remove(switch.address)
                    for abv in nwsettings.nodeabrlist:
                        if abv in hostsplit:
                            switch.node = abv
                            hostsplit.remove(abv)
                            break
                    for portion in hostsplit:
                        if pattern.match(portion):
                            hostsplit.remove(portion)
                            bldgsplit = re.split('(\d+)', portion)
                            bldgsplit = [x for x in bldgsplit if x]
                            switch.buildnumber = int(bldgsplit[0])
                            switch._pad_building_number()
                            switch.buildingname = bldgsplit[1]
                    if len(hostsplit) > 0:
                        hostsplit = self._check_portion(switch,hostsplit)
                        if hostsplit:
                            if len(hostsplit) == 1:  # most likely the room
                                switch.roomnumber = hostsplit[0]
                            if len(hostsplit) == 2:
                                switch.roomnumber = hostsplit[0]
                                switch.racknumber = hostsplit[1]
                            if len(hostsplit) == 3:
                                switch.buildnumber = int(hostsplit[0])
                                switch._pad_building_number()
                                switch.buildingname = hostsplit[1]
                                switch.roomnumber = hostsplit[2]
                else:  # edge names
                    switch.function_descriptor = None
                    if "PoE" in hostsplit:
                        hostsplit.remove("PoE")
                    if "noc" in hostsplit:
                        hostsplit.remove("noc")
                    if 'airmed' in hostsplit:
                        hostsplit.remove('airmed')
                    for i in range(1, 10):
                        if f"sx{i}" in hostsplit[0]:
                            hostsplit.remove(f"sx{i}")
                            switch.function_descriptor_number = i
                            switch.function_descriptor = "sx"
                        elif f"SX{i}" in hostsplit[0]:
                            hostsplit.remove(f"SX{i}")
                            switch.function_descriptor_number = i
                            switch.function_descriptor = "sx"
                    for i in range(1, 5):
                        if f"dx{i}" in hostsplit[0]:
                            hostsplit.remove(f"dx{i}")
                            switch.function_descriptor_number = i
                            switch.function_descriptor = "dx"
                        elif f"DX{i}" in hostsplit[0]:
                            hostsplit.remove(f"DX{i}")
                            switch.function_descriptor_number = i
                            switch.function_descriptor = "dx"
                    for i in range(1, 3):
                        if f"r{i}" in hostsplit[0]:
                            hostsplit.remove(f"r{i}")
                            switch.function_descriptor_number = i
                            switch.function_descriptor = "r"
                        elif f"R{i}" in hostsplit[0]:
                            hostsplit.remove(f"R{i}")
                            switch.function_descriptor_number = i
                            switch.function_descriptor = "r"
                    if switch.function_descriptor:
                        switch.description = nwsettings.function_descriptors[switch.function_descriptor]
                    for abv in nwsettings.nodeabrlist:
                        if abv in hostsplit:
                            switch.node = abv
                            hostsplit.remove(abv)
                            break
                    for portion in hostsplit:
                        if pattern.match(portion):
                            hostsplit.remove(portion)
                            bldgsplit = re.split('(\d+)', portion)
                            bldgsplit = [x for x in bldgsplit if x]
                            switch.buildnumber = int(bldgsplit[0])
                            switch._pad_building_number()
                            switch.buildingname = bldgsplit[1]
                    if len(hostsplit) > 0:
                        hostsplit = self._check_portion(switch,hostsplit)
                        if hostsplit:
                            if len(hostsplit) == 1:  # most likely the room
                                switch.roomnumber = hostsplit[0]
                            if len(hostsplit) == 2:
                                switch.roomnumber = hostsplit[0]
                                switch.racknumber = hostsplit[1]
                            if len(hostsplit) == 3:
                                switch.buildnumber = int(hostsplit[0])
                                switch._pad_building_number()
                                switch.buildingname = hostsplit[1]
                                switch.roomnumber = hostsplit[2]
        except Exception as e:
            logger.error(e, exc_info=True)
            raise
        else:
            return switch
    def update_names(self):
        """
        This Function updates the names in all the locations all the switches in self.Switches_syntax_compatability
        """

        logger.info(f"Updating all names - started")
        cname_policy = ['dx', 'dvpn', 'dmx']
        try:
            if not self.orion:
                self.change_orion_fields()
            if not self.infoblox:
                self.change_infoblox_fields()
            if self.aliascheck:
                self._delete_aliases()
            if self.wrongcnames:
                self._delete_cname()
            if self.wronghost:
                self._delete_hosts()
            if self.external_host_object:
                self._modify_host_view()
            if self.switch.function_descriptor in cname_policy:  # only run on records requiring cnames
                if not self.cname1check or not self.cname2check:
                    self._update_cname_infoblox()
            if not self.switchhost:
                updatestring = f'hostname {self.AuthoritativeName}'
                self.change_Switch_fields(updatestring)
            if not self.switchbanner:
                updatestring = (
                    f"""banner login ^
{self.AuthoritativeName}

University of Utah Network:  All use of this device must comply
with the University of Utah policies and procedures.  Any use of
this device, whether deliberate or not will be held legally
responsible.  See University of Utah Information Security
Policy (4-004) for details.

Problems within the University of Utah's network should be reported
by calling the Campus Helpdesk at 581-4000, or via e-mail at
helpdesk@utah.edu

DO NOT LOGIN
if you are not authorized by NetCom at the University of Utah.

^       
                """)
                self.change_Switch_fields(updatestring)
        except Exception as e:
            logger.info(f"Updating all names - Failed")
            logger.error(e, exc_info=True)
            pass
        else:
            logger.info(f"Updating all names - Success")

###################################################Helpers##############################################################
    def _remove_domains(self,record):
        """
        Removes '.net.utah.edu' or '.med.utah.edu' from the string past in.
        Args:
            record(str): a name of a DNS record
        Returns:
            (str) Dns Record name
        """
        if '.net.utah.edu' in record:
            record = re.sub(".net.utah.edu", "", record)
        elif '.med.utah.edu' in record:
            record = re.sub(".med.utah.edu", "", record)
        return record

    def generate_building_list(self):
        """
        This function pulls the building list, and creates an object with all the rows from the CSV file
        """
        logger.info(f"Gathering building list - Starting")
        # TODO Check the building list for missing values and log to Building issue logger
        try:
            files = os.listdir()
            for file in files:
                if file == 'UniversityUtahBuildingList.csv':
                    with open(file, mode="r") as file:
                        wholefile = file.read()
                        wholefile = wholefile.split('\n')
                        for line in wholefile[7:]:
                            line = line.split(",")
                            building = Building()
                            if len(line) == 1:
                                continue
                            building.BuildingNumber = int(line[0])
                            building.BuildingName = line[1]
                            building.Abbreviation = line[2]
                            building.Campus = line[3]
                            building.StreetAddress = line[4]
                            building.StreetCoordinate = line[5]
                            building.City = line[6]
                            building.State = line[7]
                            building.zip = line[8]
                            building.Status = line[9]
                            building.Leased = line[10]
                            building.Built = line[11]
                            building.Demolished = line[12]
                            building.LocationCode = line[13]
                            building.NASF = line[14]
                            building.NSF = line[15]
                            building.GSF = line[16]
                            self.buildinglist.append(building)

        except Exception as e:
            logger.info(f"Gathering building list - Failed")
            logger.error(e, exc_info=True)
            raise
        else:
            logger.info(f"Gathering building list - Success")

    def get_building_info(self):
        """
        Add the building object to the approiate switch object
        """
        logger.info(f"Getting building info - started")
        assert isinstance(self.switch, Switch), f'not a self.switch object got: {type(self.switch)}'
        try:
            self.switch.sort_hostname()
            buildingnumber = None
            buildingname = None
            if self.switch.buildnumber:
                buildingnumber = self.switch.buildnumber
            if self.switch.buildingname:
                buildingname = self.switch.buildingname
            if buildingname and buildingnumber:
                for Building in self.buildinglist:
                    if buildingnumber == 0:
                        if buildingname == Building.Abbreviation:
                            self.switch.Building = Building
                    if Building.BuildingNumber == buildingnumber:
                        self.switch.Building = Building

        except Exception as e:
            logger.info(f"Getting building info - Failed")
            logger.error(e, exc_info=True)
            pass
        else:
            logger.info(f"Getting building info - Success")

def create_sample_and_remove_from_list(list,number):
    randomtest = random.sample(list, number)
    for item in randomtest:
        list.remove(item)
    return randomtest,list

def _run_create_name_update(sw):
    updatestring = f""" IP Address: {sw['ip']}
----------------------------------------------------------------------------
SKIPPING DEVICE NOT ABLE TO SSH INTO DEVICE"""
    if 'sx1-parkcitycovid-indoors-meraki' in sw['Caption']:
        return updatestring
    if ('dx' in sw['DNS'] or
            'dx' in sw['Caption'] or
            'sx' in sw['Caption'] or
            'sx' in sw['DNS']):
        switch = Switch(sw['ip'])
        n = Namecheck(switch, sw['Caption'], sw['DNS'])
        result_str = n.create_name_update_excel()
        return result_str
def _batch_name_update():
    update_email_string = ''
    with ThreadPoolExecutor(max_workers=8) as executor:
        results = executor.map(_run_create_name_update, Switch.settings.Random_batch_test_3)
        for result in results:
            update_email_string += result + '\r\n'


if __name__ == "__main__":
    # switch = Switch('172.31.2.132')
    # n = Namecheck(switch, 'dx1-151ustar.net.utah.edu', 'dx1-151ustar.net.utah.edu')
    # n.process_name()
    """
    Main method, entry point to the program.

    Makes call to Orion API to gather a list of all of the switches monitored by the University of Utah, gathers the
    data for each switch from the TOAST API, and changes the data in the Orion and Infoblox APIs accordingly.
    """

    # orionapi = orionsdk.SwisClient(hostname=auth.OrionAPI.url,
    #                                     username=auth.OrionAPI.username,
    #                                     password=auth.OrionAPI.password)
    logger.info(f"Generating Switch List - Starting")
    try:
        # or_results = orionapi.query("SELECT (ip, DNS, " +
        #                                  "MachineType, NodeName, DisplayName,Caption) FROM Orion.Nodes WHERE Vendor='Cisco' AND " +
        #                                  "(DNS LIKE 'dx%' OR DNS LIKE 'sx%')")
        # if not or_results or not or_results.get('results', None):
        #     raise ValueError("Error retrieving switch list by SWQL query")
        #
        # randomtest_batch_2,list = create_sample_and_remove_from_list(or_results['results'],40)
        # Random_batch_test_3,list = create_sample_and_remove_from_list(list,100)
        # random_batch_production_1,list = create_sample_and_remove_from_list(list,201)
        # random_batch_production_2,list = create_sample_and_remove_from_list(list, 201)
        # random_batch_production_3,list = create_sample_and_remove_from_list(list, 201)
        # random_batch_production_4,list = create_sample_and_remove_from_list(list, 201)
        # random_batch_production_5,list = create_sample_and_remove_from_list(list, 198)
        _batch_name_update()
    except Exception as e:
        logger.info(f"Generating Switch List - Failed")
        logger.error(e, exc_info=True)
        pass
    else:
        logger.info(f"Generating Switch List - Success")


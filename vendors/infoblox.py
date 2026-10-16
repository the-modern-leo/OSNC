import requests
import json
import ssl
from auth import infoblox, SSH
from requests.auth import HTTPBasicAuth

headers = {"Content-Type": "application/json"}

class restapi():
    def __int__(self):
        self.headers = {"Content-Type": "application/json"}

    def _login(self):
        pass
    def get_host_record(self, ipad=None,macaddress=None,dns=None):

        if ipad:
            query = f"record:host?ipv4addr={ipad}"
        elif macaddress:
            query = f"record:host?ipvaddr={ipad}"
        elif dns:
            query = f"record:host?name={dns}"
        else:
            return
        self._get(queryurl=query)

    def create_host_record(self,host_name, ip_address, dns_view="default"):
        """
        Create a host record in Infoblox using WAPI.

        :param host_name: Fully qualified domain name for the host (e.g., host.example.com)
        :param ip_address: IP address to assign to the host
        :param dns_view: DNS view name (default: "default")
        :return: Response from the API (JSON)
        """

        payload = {
            "name": host_name,
            "ipv4addrs": [
                {
                    "ipv4addr": ip_address
                }
            ],
            "view": dns_view
        }
        return self._post("/record:host",payload)

    def get_Network_containers_all(self,netadd):
        return self._get(f"network?network_container={netadd}&_return_fields%2B=network_container",)

    def createContainer(self,data):
        """
        netadd(str): ex - 10.0.0.0/16
        """
        jsondict = {
            "comment": f"""{data["comment"]}""",
            "network": f"""{ data['network']}/{data['size']}"""
        }
        return self._post("networkcontainer",jsondict)
    def get_Network_container(self, netadd):
        return self._get(f"network?network_container={netadd}&_return_fields%2B=network_container", )
    def create_Network_container(self,netadd):
        """
        netadd(str): ex - 10.0.0.0/16
        """
        data = {
            "method": "GET",
            "object": "ipv4address",
            "data": {
                "network": netadd,
                "network_view": "default",
                "status": "USED"
            }}
        return self._post(f"request", data)
    def createNetwork(self,data):
        jsondata = {
            "comment": f"""{data["comment"]}""",
            "network": {
                "_object_function": "next_available_network",
                "_result_field": "networks",
                "_object": "networkcontainer",
                "_object_parameters": {
                    "network": f"{data['network']}",
                },
                "_parameters": {
                    "cidr": data['size'],
                },
            }
        }
        return self._post(f"network", jsondata)
    def create_multiple_networks(self,netcontainer,networks):
        """
        Will create multiple networks under one network container.
        netcontainer(str): ex - 10.0.0.0/16
        networks(list): a list of dictionaries that will be used for the data to create the networks.
        """
        responses = []
        for net in networks:
            data = {
                "comment": f"""Vlan: {net["vlan"]}
Location: {net["location"]}
Router: {net["router"]}""",
                "network": {
                    "_object_function": "next_available_network",
                    "_result_field": "networks",
                    "_object": "networkcontainer",
                    "_object_parameters": {
                        "network": f"{netcontainer}",
                    },
                    "_parameters": {
                        "cidr": net['size'],
                    },
                }
            }
            responses.append(self._post(f"network", data))
        return responses

    def create_HSRP_gateways(self,netcontainer,data):
        pass

    def AssociateNetworkToMember(self,network,dhcpmember):
        """

        """
        reply = None
        reply = self._get(f"network?network={network}")
        data = {
                "members": dhcpmember
            }
        return self._put(reply[0]["_ref"], data)
    def AssociateRangeTofailover(self,network,failover):
        """

        """
        reply = None
        reply = self._get(f"range?network={network}")
        data = {
                "members": failover
            }
        return self._put(reply[0]["_ref"], data)
    def CreateDHCPRange(self,network,network_view,start_addr,end_addr,comment=None,dhcpmember=None,failover_association=None):
        """

        """
        data = {
            "network_view": str(network_view),
            "network": str(network),
            "end_addr": str(end_addr),
            "start_addr": str(start_addr),
        }
        if dhcpmember:
            data["member"] = dhcpmember
        if comment:
            data["comment"] = str(comment)
        if failover_association:
            data["failover_association"] = failover_association

        return self._post(f"range", data)

    def delete_host_record(self, name=None, ipad=None):
        if name:
            ref = self.get_host_record(dns=name)
        elif ipad:
            ref = self.get_host_record(ipad=ipad)
        else:
            return ("Not able to serach for Host Record. No IP or DNS")

        query = f"{ref[0]['_ref']}"
        return self._delete(queryurl=query)

    def _get(self, queryurl):
        response = requests.get(infoblox.url + queryurl, headers=headers,
                                auth=(SSH.username, SSH.password),verify=False)
        if response.status_code == 200:
            return response.json()

    def _post(self, queryurl, jsondict):
        try:
            response = requests.post(infoblox.url + queryurl, data=json.dumps(jsondict), headers=headers,
                                     auth=(SSH.username, SSH.password),verify=False)
            if response.status_code == 200:
                return response.json()
            elif response.status_code == 201:
                return response.json()
            else:
                print (response)
        except requests.exceptions.RequestException as e:
            print(f"Error creating host record: {e}")
            return None
    def _put(self, queryurl, jsondict):
        response = requests.put(infoblox.url + queryurl, data=json.dumps(jsondict), headers=headers,
                                auth=(SSH.username, SSH.password),verify=False)
        response.json()
        if response.status_code == 200:
            return response
        elif response.status_code != 200 or response.status_code != 201:
            return "did not work"

    def _delete(self, queryurl, jsondict):
        response = requests.delete(infoblox.url + queryurl, data=json.dumps(jsondict), headers=headers,
                                   auth=(SSH.username, SSH.password),verify=False)
        response.json()
        if response.status_code == 200:
            return response

class InfobloxAPI:
    def __init__(self, base_url, username, password, wapi_version="2.10", verify_ssl=False):
        """
        Initialize the Infoblox API client.

        Args:
            base_url (str): Base URL of the Infoblox server (e.g., https://infoblox.example.com)
            username (str): Username for authentication
            password (str): Password for authentication
            wapi_version (str): WAPI version to use (default: "2.10")
            verify_ssl (bool): Whether to verify SSL certificates (default: False)
        """
        self.base_url = base_url
        self.username = username
        self.password = password
        self.wapi_version = wapi_version
        self.verify_ssl = verify_ssl
        self.session = requests.Session()
        self.session.auth = HTTPBasicAuth(username, password)
        self.session.headers.update({'Content-Type': 'application/json'})

    def _make_request(self, method, endpoint, data=None, params=None):
        """
        Make an HTTP request to the Infoblox WAPI.

        Args:
            method (str): HTTP method (GET, POST, PUT, DELETE)
            endpoint (str): WAPI endpoint to call
            data (dict, optional): JSON data to send in request body
            params (dict, optional): Query parameters for the request

        Returns:
            dict or None: JSON response from the API, or None if request failed
        """
        url = f"{self.base_url}/wapi/v{self.wapi_version}/{endpoint}"
        try:
            response = self.session.request(method, url, json=data, params=params, verify=self.verify_ssl)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
            return None

    def _get(self, endpoint, params=None):
        """
        Make a GET request to retrieve objects from Infoblox.

        Args:
            endpoint (str): WAPI endpoint to retrieve data from
            params (dict, optional): Query parameters to filter results

        Returns:
            dict or None: JSON response containing the requested objects, or None if request failed
        """
        return self._make_request('GET', endpoint, params=params)

    def _post(self, endpoint, data=None):
        """
        Make a POST request to create objects in Infoblox.

        Args:
            endpoint (str): WAPI endpoint to create object at
            data (dict): JSON data containing object properties

        Returns:
            dict or None: JSON response containing reference to created object, or None if request failed
        """
        return self._make_request('POST', endpoint, data=data)

    def _put(self, endpoint, data=None):
        """
        Make a PUT request to update objects in Infoblox.

        Args:
            endpoint (str): WAPI endpoint of object to update
            data (dict): JSON data containing updated properties

        Returns:
            dict or None: JSON response containing updated object, or None if request failed
        """
        return self._make_request('PUT', endpoint, data=data)

    def _delete(self, endpoint):
        """
        Make a DELETE request to remove objects from Infoblox.

        Args:
            endpoint (str): WAPI endpoint of object to delete

        Returns:
            dict or None: JSON response confirming deletion, or None if request failed
        """
        return self._make_request('DELETE', endpoint)

    def create_a_record(self, name, ipv4addr, view="default"):
        """
        Create an A record in Infoblox.

        Args:
            name (str): Fully qualified domain name for the A record
            ipv4addr (str): IPv4 address to associate with the name
            view (str): DNS view to create the record in (default: "default")

        Returns:
            dict or None: JSON response containing reference to created A record, or None if request failed
        """
        data = {
            'name': name,
            'ipv4addr': ipv4addr,
            'view': view
        }
        return self._post('record:a', data)

    def create_cname_record(self, name, canonical, view="default"):
        """
        Create a CNAME record in Infoblox.

        Args:
            name (str): Alias name for the CNAME record
            canonical (str): Canonical (FQDN) name that the alias points to
            view (str): DNS view to create the record in (default: "default")

        Returns:
            dict or None: JSON response containing reference to created CNAME record, or None if request failed
        """
        data = {
            'name': name,
            'canonical': canonical,
            'view': view
        }
        return self._post('record:cname', data)

    def create_ptr_record(self, ptrdname, ipv4addr, view="default"):
        """
        Create a PTR record in Infoblox.

        Args:
            ptrdname (str): Domain name to associate with the IP address
            ipv4addr (str): IPv4 address for reverse lookup
            view (str): DNS view to create the record in (default: "default")

        Returns:
            dict or None: JSON response containing reference to created PTR record, or None if request failed
        """
        data = {
            'ptrdname': ptrdname,
            'ipv4addr': ipv4addr,
            'view': view
        }
        return self._post('record:ptr', data)

    def create_host_record(self, name, ipv4addr, view="default"):
        """
        Create a host record in Infoblox (automatically creates A and PTR records).

        Args:
            name (str): Fully qualified domain name for the host
            ipv4addr (str): IPv4 address to associate with the host
            view (str): DNS view to create the record in (default: "default")

        Returns:
            dict or None: JSON response containing reference to created host record, or None if request failed
        """
        data = {
            'name': name,
            'ipv4addrs': [{
                'ipv4addr': ipv4addr
            }],
            'view': view
        }
        return self._post('record:host', data)

    def create_network(self, network, netmask, network_view="default", **kwargs):
        """
        Create a network in Infoblox for IP address management.

        Args:
            network (str): Network address (e.g., "192.168.1.0")
            netmask (str): Netmask for the network (e.g., "255.255.255.0")
            network_view (str): Network view to create the network in (default: "default")
            **kwargs: Additional network properties (e.g., comment, disable, etc.)

        Returns:
            dict or None: JSON response containing reference to created network, or None if request failed
        """
        data = {
            'network': network,
            'netmask': netmask,
            'network_view': network_view
        }
        data.update(kwargs)
        return self._post('network', data)

    def create_network_container(self, network, netmask, network_view="default", **kwargs):
        """
        Create a network container in Infoblox for hierarchical IP management.

        Args:
            network (str): Network address for the container (e.g., "10.0.0.0")
            netmask (str): Netmask for the container (e.g., "255.0.0.0")
            network_view (str): Network view to create the container in (default: "default")
            **kwargs: Additional container properties (e.g., comment, disable, etc.)

        Returns:
            dict or None: JSON response containing reference to created network container, or None if request failed
        """
        data = {
            'network': network,
            'netmask': netmask,
            'network_view': network_view
        }
        data.update(kwargs)
        return self._post('networkcontainer', data)

    def find_a_record(self, name=None, ipv4addr=None, view="default"):
        """
        Find A record(s) in Infoblox.

        Args:
            name (str, optional): Fully qualified domain name to search for
            ipv4addr (str, optional): IPv4 address to search for
            view (str): DNS view to search in (default: "default")

        Returns:
            dict or None: JSON response containing matching A records, or None if request failed
        """
        params = {'view': view}
        if name:
            params['name'] = name
        if ipv4addr:
            params['ipv4addr'] = ipv4addr
        return self._get('record:a', params=params)

    def find_cname_record(self, name=None, canonical=None, view="default"):
        """
        Find CNAME record(s) in Infoblox.

        Args:
            name (str, optional): Alias name to search for
            canonical (str, optional): Canonical name to search for
            view (str): DNS view to search in (default: "default")

        Returns:
            dict or None: JSON response containing matching CNAME records, or None if request failed
        """
        params = {'view': view}
        if name:
            params['name'] = name
        if canonical:
            params['canonical'] = canonical
        return self._get('record:cname', params=params)

    def find_ptr_record(self, ptrdname=None, ipv4addr=None, view="default"):
        """
        Find PTR record(s) in Infoblox.

        Args:
            ptrdname (str, optional): Domain name to search for
            ipv4addr (str, optional): IPv4 address to search for
            view (str): DNS view to search in (default: "default")

        Returns:
            dict or None: JSON response containing matching PTR records, or None if request failed
        """
        params = {'view': view}
        if ptrdname:
            params['ptrdname'] = ptrdname
        if ipv4addr:
            params['ipv4addr'] = ipv4addr
        return self._get('record:ptr', params=params)

    def find_host_record(self, name=None, ipv4addr=None, view="default"):
        """
        Find host record(s) in Infoblox.

        Args:
            name (str, optional): Fully qualified domain name to search for
            ipv4addr (str, optional): IPv4 address to search for
            view (str): DNS view to search in (default: "default")

        Returns:
            dict or None: JSON response containing matching host records, or None if request failed
        """
        params = {'view': view}
        if name:
            params['name'] = name
        if ipv4addr:
            params['ipv4addr'] = ipv4addr
        return self._get('record:host', params=params)

    def find_network(self, network=None, network_view="default", **kwargs):
        """
        Find network(s) in Infoblox.

        Args:
            network (str, optional): Network address to search for (e.g., "192.168.1.0")
            network_view (str): Network view to search in (default: "default")
            **kwargs: Additional search parameters

        Returns:
            dict or None: JSON response containing matching networks, or None if request failed
        """
        params = {'network_view': network_view}
        if network:
            params['network'] = network
        params.update(kwargs)
        return self._get('network', params=params)

    def find_network_container(self, network=None, network_view="default", **kwargs):
        """
        Find network container(s) in Infoblox.

        Args:
            network (str, optional): Network address to search for (e.g., "10.0.0.0")
            network_view (str): Network view to search in (default: "default")
            **kwargs: Additional search parameters

        Returns:
            dict or None: JSON response containing matching network containers, or None if request failed
        """
        params = {'network_view': network_view}
        if network:
            params['network'] = network
        params.update(kwargs)
        return self._get('networkcontainer', params=params)

    def modify_a_record(self, ref, **kwargs):
        """
        Modify an existing A record.

        Args:
            ref (str): Object reference of the A record to modify (from find or create)
            **kwargs: Properties to modify (name, ipv4addr, view, etc.)

        Returns:
            dict or None: JSON response containing updated A record, or None if request failed
        """
        return self._put(ref, data=kwargs)

    def delete_a_record(self, ref):
        """
        Delete an A record.

        Args:
            ref (str): Object reference of the A record to delete (from find or create)

        Returns:
            dict or None: JSON response confirming deletion, or None if request failed
        """
        return self._delete(ref)

    def modify_cname_record(self, ref, **kwargs):
        """
        Modify an existing CNAME record.

        Args:
            ref (str): Object reference of the CNAME record to modify (from find or create)
            **kwargs: Properties to modify (name, canonical, view, etc.)

        Returns:
            dict or None: JSON response containing updated CNAME record, or None if request failed
        """
        return self._put(ref, data=kwargs)

    def delete_cname_record(self, ref):
        """
        Delete a CNAME record.

        Args:
            ref (str): Object reference of the CNAME record to delete (from find or create)

        Returns:
            dict or None: JSON response confirming deletion, or None if request failed
        """
        return self._delete(ref)

    def modify_ptr_record(self, ref, **kwargs):
        """
        Modify an existing PTR record.

        Args:
            ref (str): Object reference of the PTR record to modify (from find or create)
            **kwargs: Properties to modify (ptrdname, ipv4addr, view, etc.)

        Returns:
            dict or None: JSON response containing updated PTR record, or None if request failed
        """
        return self._put(ref, data=kwargs)

    def delete_ptr_record(self, ref):
        """
        Delete a PTR record.

        Args:
            ref (str): Object reference of the PTR record to delete (from find or create)

        Returns:
            dict or None: JSON response confirming deletion, or None if request failed
        """
        return self._delete(ref)

    def modify_host_record(self, ref, **kwargs):
        """
        Modify an existing host record.

        Args:
            ref (str): Object reference of the host record to modify (from find or create)
            **kwargs: Properties to modify (name, ipv4addrs, view, etc.)

        Returns:
            dict or None: JSON response containing updated host record, or None if request failed
        """
        return self._put(ref, data=kwargs)

    def delete_host_record(self, ref):
        """
        Delete a host record.

        Args:
            ref (str): Object reference of the host record to delete (from find or create)

        Returns:
            dict or None: JSON response confirming deletion, or None if request failed
        """
        return self._delete(ref)

    def modify_network(self, ref, **kwargs):
        """
        Modify an existing network.

        Args:
            ref (str): Object reference of the network to modify (from find or create)
            **kwargs: Properties to modify (network, netmask, network_view, comment, etc.)

        Returns:
            dict or None: JSON response containing updated network, or None if request failed
        """
        return self._put(ref, data=kwargs)

    def delete_network(self, ref):
        """
        Delete a network.

        Args:
            ref (str): Object reference of the network to delete (from find or create)

        Returns:
            dict or None: JSON response confirming deletion, or None if request failed
        """
        return self._delete(ref)

    def modify_network_container(self, ref, **kwargs):
        """
        Modify an existing network container.

        Args:
            ref (str): Object reference of the network container to modify (from find or create)
            **kwargs: Properties to modify (network, netmask, network_view, comment, etc.)

        Returns:
            dict or None: JSON response containing updated network container, or None if request failed
        """
        return self._put(ref, data=kwargs)

    def delete_network_container(self, ref):
        """
        Delete a network container.

        Args:
            ref (str): Object reference of the network container to delete (from find or create)

        Returns:
            dict or None: JSON response confirming deletion, or None if request failed
        """
        return self._delete(ref)

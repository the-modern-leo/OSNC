import requests
import json
import ssl
from auth import infoblox, SSH
from requests.auth import HTTPBasicAuth

headers = {"Content-Type": "application/json"}


wapi_version = "2.10"
verify_ssl=False

def _make_request(method, endpoint, data=None, params=None):
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
    try:
        session = requests.Session()
        session.auth = HTTPBasicAuth(SSH.username, SSH.password)
        session.headers.update({'Content-Type': 'application/json'})
        response = session.request(method, infoblox.url+endpoint, json=data, params=params, verify=verify_ssl)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None

def _get(endpoint, params=None):
    """
    Make a GET request to retrieve objects from Infoblox.

    Args:
        endpoint (str): WAPI endpoint to retrieve data from
        params (dict, optional): Query parameters to filter results

    Returns:
        dict or None: JSON response containing the requested objects, or None if request failed
    """
    return _make_request('GET', endpoint, params=params)

def _post(endpoint, data=None):
    """
    Make a POST request to create objects in Infoblox.

    Args:
        endpoint (str): WAPI endpoint to create object at
        data (dict): JSON data containing object properties

    Returns:
        dict or None: JSON response containing reference to created object, or None if request failed
    """
    return _make_request('POST', endpoint, data=data)

def _put(endpoint, data=None):
    """
    Make a PUT request to update objects in Infoblox.

    Args:
        endpoint (str): WAPI endpoint of object to update
        data (dict): JSON data containing updated properties

    Returns:
        dict or None: JSON response containing updated object, or None if request failed
    """
    return _make_request('PUT', endpoint, data=data)

def _delete(endpoint):
    """
    Make a DELETE request to remove objects from Infoblox.

    Args:
        endpoint (str): WAPI endpoint of object to delete

    Returns:
        dict or None: JSON response confirming deletion, or None if request failed
    """
    return _make_request('DELETE', endpoint)

class DHCP():
    def __int__(self):
        self.headers = {"Content-Type": "application/json"}

    def AssociateNetworkToMember(self,network,dhcpmember):
        """

        """
        reply = _get(f"network?network={network}")
        data = {
                "members": dhcpmember
            }
        return _put(reply[0]["_ref"], data)
    def AssociateRangeTofailover(self,network,failover):
        """

        """
        reply = _get(f"range?network={network}")
        data = {
                "members": failover
            }
        return _put(reply[0]["_ref"], data)
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

        return _post(f"range", data)

    def create_dhcp_range(self, start_addr, end_addr, network, name=None, comment=None, disable=False, **kwargs):
        """
        Create a DHCP range in Infoblox.

        Args:
            start_addr (str): Starting IP address of the range
            end_addr (str): Ending IP address of the range
            network (str): Network address the range belongs to (e.g., "192.168.1.0/24")
            name (str, optional): Name for the DHCP range
            comment (str, optional): Comment/description for the range
            disable (bool): Whether the range is disabled (default: False)
            **kwargs: Additional properties (e.g., failover_association, extattrs, etc.)

        Returns:
            dict or None: JSON response containing reference to created DHCP range, or None if request failed
        """
        data = {
            'start_addr': start_addr,
            'end_addr': end_addr,
            'network': network,
            'disable': disable
        }
        if name:
            data['name'] = name
        if comment:
            data['comment'] = comment
        data.update(kwargs)
        return _post('range', data)

    def find_dhcp_range(self, start_addr=None, end_addr=None, network=None, name=None, **kwargs):
        """
        Find DHCP range(s) in Infoblox.

        Args:
            start_addr (str, optional): Starting IP address to search for
            end_addr (str, optional): Ending IP address to search for
            network (str, optional): Network address to search for
            name (str, optional): Name of the range to search for
            **kwargs: Additional search parameters

        Returns:
            dict or None: JSON response containing matching DHCP ranges, or None if request failed
        """
        params = {}
        if start_addr:
            params['start_addr'] = start_addr
        if end_addr:
            params['end_addr'] = end_addr
        if network:
            params['network'] = network
        if name:
            params['name'] = name
        params.update(kwargs)
        return _get('range', params=params)

    def modify_dhcp_range(self, ref, **kwargs):
        """
        Modify an existing DHCP range.

        Args:
            ref (str): Object reference of the DHCP range to modify (from find or create)
            **kwargs: Properties to modify (start_addr, end_addr, network, name, comment, disable, etc.)

        Returns:
            dict or None: JSON response containing updated DHCP range, or None if request failed
        """
        return _put(ref, data=kwargs)

    def delete_dhcp_range(self, ref):
        """
        Delete a DHCP range.

        Args:
            ref (str): Object reference of the DHCP range to delete (from find or create)

        Returns:
            dict or None: JSON response confirming deletion, or None if request failed
        """
        return _delete(ref)

    def create_dhcp_failover_association(self, name, primary, secondary, primary_server_type="NONE",
                                         secondary_server_type="NONE", **kwargs):
        """
        Create a DHCP failover association in Infoblox.

        Args:
            name (str): Name for the failover association
            primary (str): Object reference of the primary DHCP server
            secondary (str): Object reference of the secondary DHCP server
            primary_server_type (str): Type of primary server (default: "NONE")
            secondary_server_type (str): Type of secondary server (default: "NONE")
            **kwargs: Additional properties (e.g., mclt, split, load_balance_percent, etc.)

        Returns:
            dict or None: JSON response containing reference to created failover association, or None if request failed
        """
        data = {
            'name': name,
            'primary': primary,
            'secondary': secondary,
            'primary_server_type': primary_server_type,
            'secondary_server_type': secondary_server_type
        }
        data.update(kwargs)
        return _post('dhcpfailover', data)

    def find_dhcp_failover_association(self, name=None, primary=None, secondary=None, **kwargs):
        """
        Find DHCP failover association(s) in Infoblox.

        Args:
            name (str, optional): Name of the failover association to search for
            primary (str, optional): Object reference of primary server to search for
            secondary (str, optional): Object reference of secondary server to search for
            **kwargs: Additional search parameters

        Returns:
            dict or None: JSON response containing matching failover associations, or None if request failed
        """
        params = {}
        if name:
            params['name'] = name
        if primary:
            params['primary'] = primary
        if secondary:
            params['secondary'] = secondary
        params.update(kwargs)
        return _get('dhcpfailover', params=params)

    def modify_dhcp_failover_association(self, ref, **kwargs):
        """
        Modify an existing DHCP failover association.

        Args:
            ref (str): Object reference of the failover association to modify (from find or create)
            **kwargs: Properties to modify (name, mclt, split, load_balance_percent, etc.)

        Returns:
            dict or None: JSON response containing updated failover association, or None if request failed
        """
        return _put(ref, data=kwargs)

    def delete_dhcp_failover_association(self, ref):
        """
        Delete a DHCP failover association.

        Args:
            ref (str): Object reference of the failover association to delete (from find or create)

        Returns:
            dict or None: JSON response confirming deletion, or None if request failed

        Note:
            A failover association cannot be deleted if it is assigned to a DHCP range <kcite ref="116"/>.
        """
        return _delete(ref)

class DNS():

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
        return _post('record:a', data)

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
        return _post('record:cname', data)

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
        return _post('record:ptr', data)

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
        return _post('record:host', data)

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
        return _post('network', data)

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
        return _post('networkcontainer', data)

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
        return _get('record:a', params=params)

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
        return _get('record:cname', params=params)

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
        return _get('record:ptr', params=params)

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
        return _get('record:host', params=params)

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
        return _get('network', params=params)

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
        return _get('networkcontainer', params=params)

    def modify_a_record(self, ref, **kwargs):
        """
        Modify an existing A record.

        Args:
            ref (str): Object reference of the A record to modify (from find or create)
            **kwargs: Properties to modify (name, ipv4addr, view, etc.)

        Returns:
            dict or None: JSON response containing updated A record, or None if request failed
        """
        return _put(ref, data=kwargs)

    def delete_a_record(self, ref):
        """
        Delete an A record.

        Args:
            ref (str): Object reference of the A record to delete (from find or create)

        Returns:
            dict or None: JSON response confirming deletion, or None if request failed
        """
        return _delete(ref)

    def modify_cname_record(self, ref, **kwargs):
        """
        Modify an existing CNAME record.

        Args:
            ref (str): Object reference of the CNAME record to modify (from find or create)
            **kwargs: Properties to modify (name, canonical, view, etc.)

        Returns:
            dict or None: JSON response containing updated CNAME record, or None if request failed
        """
        return _put(ref, data=kwargs)

    def delete_cname_record(self, ref):
        """
        Delete a CNAME record.

        Args:
            ref (str): Object reference of the CNAME record to delete (from find or create)

        Returns:
            dict or None: JSON response confirming deletion, or None if request failed
        """
        return _delete(ref)

    def modify_ptr_record(self, ref, **kwargs):
        """
        Modify an existing PTR record.

        Args:
            ref (str): Object reference of the PTR record to modify (from find or create)
            **kwargs: Properties to modify (ptrdname, ipv4addr, view, etc.)

        Returns:
            dict or None: JSON response containing updated PTR record, or None if request failed
        """
        return _put(ref, data=kwargs)

    def delete_ptr_record(self, ref):
        """
        Delete a PTR record.

        Args:
            ref (str): Object reference of the PTR record to delete (from find or create)

        Returns:
            dict or None: JSON response confirming deletion, or None if request failed
        """
        return _delete(ref)

    def modify_host_record(self, ref, **kwargs):
        """
        Modify an existing host record.

        Args:
            ref (str): Object reference of the host record to modify (from find or create)
            **kwargs: Properties to modify (name, ipv4addrs, view, etc.)

        Returns:
            dict or None: JSON response containing updated host record, or None if request failed
        """
        return _put(ref, data=kwargs)

    def delete_host_record(self, ref):
        """
        Delete a host record.

        Args:
            ref (str): Object reference of the host record to delete (from find or create)

        Returns:
            dict or None: JSON response confirming deletion, or None if request failed
        """
        return _delete(ref)

    def modify_network(self, ref, **kwargs):
        """
        Modify an existing network.

        Args:
            ref (str): Object reference of the network to modify (from find or create)
            **kwargs: Properties to modify (network, netmask, network_view, comment, etc.)

        Returns:
            dict or None: JSON response containing updated network, or None if request failed
        """
        return _put(ref, data=kwargs)

    def delete_network(self, ref):
        """
        Delete a network.

        Args:
            ref (str): Object reference of the network to delete (from find or create)

        Returns:
            dict or None: JSON response confirming deletion, or None if request failed
        """
        return _delete(ref)

    def modify_network_container(self, ref, **kwargs):
        """
        Modify an existing network container.

        Args:
            ref (str): Object reference of the network container to modify (from find or create)
            **kwargs: Properties to modify (network, netmask, network_view, comment, etc.)

        Returns:
            dict or None: JSON response containing updated network container, or None if request failed
        """
        return _put(ref, data=kwargs)

    def delete_network_container(self, ref):
        """
        Delete a network container.

        Args:
            ref (str): Object reference of the network container to delete (from find or create)

        Returns:
            dict or None: JSON response confirming deletion, or None if request failed
        """
        return _delete(ref)

    def find_soa_record(self, zone=None, view="default"):
        """
        Find SOA record(s) in Infoblox.

        Args:
            zone (str, optional): Zone name to search for
            view (str): DNS view to search in (default: "default")

        Returns:
            dict or None: JSON response containing matching SOA records, or None if request failed
        """
        params = {'view': view}
        if zone:
            params['zone'] = zone
        return _get('record:soa', params=params)

    def create_soa_record(self, zone, primary_ns, contact, view="default", **kwargs):
        """
        Create an SOA record in Infoblox.

        Args:
            zone (str): Zone name for the SOA record
            primary_ns (str): Primary nameserver for the zone
            contact (str): Contact email for the zone administrator
            view (str): DNS view to create the record in (default: "default")
            **kwargs: Additional SOA properties (refresh, retry, expire, default_ttl, etc.)

        Returns:
            dict or None: JSON response containing reference to created SOA record, or None if request failed
        """
        data = {
            'zone': zone,
            'primary_ns': primary_ns,
            'contact': contact,
            'view': view
        }
        data.update(kwargs)
        return _post('record:soa', data)

    def modify_soa_record(self, ref, **kwargs):
        """
        Modify an existing SOA record.

        Args:
            ref (str): Object reference of the SOA record to modify (from find or create)
            **kwargs: Properties to modify (primary_ns, contact, refresh, retry, expire, default_ttl, etc.)

        Returns:
            dict or None: JSON response containing updated SOA record, or None if request failed
        """
        return _put(ref, data=kwargs)

    def delete_soa_record(self, ref):
        """
        Delete an SOA record.

        Args:
            ref (str): Object reference of the SOA record to delete (from find or create)

        Returns:
            dict or None: JSON response confirming deletion, or None if request failed
        """
        return _delete(ref)

    def find_ns_record(self, zone=None, view="default", nameserver=None):
        """
        Find NS record(s) in Infoblox.

        Args:
            zone (str, optional): Zone name to search for
            view (str): DNS view to search in (default: "default")
            nameserver (str, optional): Nameserver to search for

        Returns:
            dict or None: JSON response containing matching NS records, or None if request failed
        """
        params = {'view': view}
        if zone:
            params['zone'] = zone
        if nameserver:
            params['nameserver'] = nameserver
        return _get('record:ns', params=params)

    def create_ns_record(self, zone, nameserver, view="default", **kwargs):
        """
        Create an NS record in Infoblox.

        Args:
            zone (str): Zone name for the NS record
            nameserver (str): Nameserver to add to the zone
            view (str): DNS view to create the record in (default: "default")
            **kwargs: Additional NS properties (ttl, comment, etc.)

        Returns:
            dict or None: JSON response containing reference to created NS record, or None if request failed
        """
        data = {
            'zone': zone,
            'nameserver': nameserver,
            'view': view
        }
        data.update(kwargs)
        return _post('record:ns', data)

    def modify_ns_record(self, ref, **kwargs):
        """
        Modify an existing NS record.

        Args:
            ref (str): Object reference of the NS record to modify (from find or create)
            **kwargs: Properties to modify (nameserver, ttl, comment, etc.)

        Returns:
            dict or None: JSON response containing updated NS record, or None if request failed
        """
        return _put(ref, data=kwargs)

    def delete_ns_record(self, ref):
        """
        Delete an NS record.

        Args:
            ref (str): Object reference of the NS record to delete (from find or create)

        Returns:
            dict or None: JSON response confirming deletion, or None if request failed
        """
        return _delete(ref)

    def find_mx_record(self, name=None, view="default", mail_exchanger=None):
        """
        Find MX record(s) in Infoblox.

        Args:
            name (str, optional): Domain name to search for
            view (str): DNS view to search in (default: "default")
            mail_exchanger (str, optional): Mail exchanger to search for

        Returns:
            dict or None: JSON response containing matching MX records, or None if request failed
        """
        params = {'view': view}
        if name:
            params['name'] = name
        if mail_exchanger:
            params['mail_exchanger'] = mail_exchanger
        return _get('record:mx', params=params)

    def create_mx_record(self, name, mail_exchanger, preference=10, view="default", **kwargs):
        """
        Create an MX record in Infoblox.

        Args:
            name (str): Domain name for the MX record
            mail_exchanger (str): Mail exchanger server for the domain
            preference (int): Preference value for the mail exchanger (lower = higher priority)
            view (str): DNS view to create the record in (default: "default")
            **kwargs: Additional MX properties (ttl, comment, etc.)

        Returns:
            dict or None: JSON response containing reference to created MX record, or None if request failed
        """
        data = {
            'name': name,
            'mail_exchanger': mail_exchanger,
            'preference': preference,
            'view': view
        }
        data.update(kwargs)
        return _post('record:mx', data)

    def modify_mx_record(self, ref, **kwargs):
        """
        Modify an existing MX record.

        Args:
            ref (str): Object reference of the MX record to modify (from find or create)
            **kwargs: Properties to modify (mail_exchanger, preference, ttl, comment, etc.)

        Returns:
            dict or None: JSON response containing updated MX record, or None if request failed
        """
        return _put(ref, data=kwargs)

    def delete_mx_record(self, ref):
        """
        Delete an MX record.

        Args:
            ref (str): Object reference of the MX record to delete (from find or create)

        Returns:
            dict or None: JSON response confirming deletion, or None if request failed
        """
        return _delete(ref)

    def find_txt_record(self, name=None, text=None, view="default"):
        """
        Find TXT record(s) in Infoblox.

        Args:
            name (str, optional): Domain name to search for
            text (str, optional): Text content to search for
            view (str): DNS view to search in (default: "default")

        Returns:
            dict or None: JSON response containing matching TXT records, or None if request failed
        """
        params = {'view': view}
        if name:
            params['name'] = name
        if text:
            params['text'] = text
        return _get('record:txt', params=params)

    def create_txt_record(self, name, text, view="default", **kwargs):
        """
        Create a TXT record in Infoblox.

        Args:
            name (str): Domain name for the TXT record
            text (str): Text content for the record
            view (str): DNS view to create the record in (default: "default")
            **kwargs: Additional TXT properties (ttl, comment, etc.)

        Returns:
            dict or None: JSON response containing reference to created TXT record, or None if request failed
        """
        data = {
            'name': name,
            'text': text,
            'view': view
        }
        data.update(kwargs)
        return _post('record:txt', data)

    def modify_txt_record(self, ref, **kwargs):
        """
        Modify an existing TXT record.

        Args:
            ref (str): Object reference of the TXT record to modify (from find or create)
            **kwargs: Properties to modify (text, ttl, comment, etc.)

        Returns:
            dict or None: JSON response containing updated TXT record, or None if request failed
        """
        return _put(ref, data=kwargs)

    def delete_txt_record(self, ref):
        """
        Delete a TXT record.

        Args:
            ref (str): Object reference of the TXT record to delete (from find or create)

        Returns:
            dict or None: JSON response confirming deletion, or None if request failed
        """
        return _delete(ref)

    def find_srv_record(self, name=None, target=None, view="default"):
        """
        Find SRV record(s) in Infoblox.

        Args:
            name (str, optional): Service name to search for
            target (str, optional): Target server to search for
            view (str): DNS view to search in (default: "default")

        Returns:
            dict or None: JSON response containing matching SRV records, or None if request failed
        """
        params = {'view': view}
        if name:
            params['name'] = name
        if target:
            params['target'] = target
        return _get('record:srv', params=params)

    def create_srv_record(self, name, target, port, priority=0, weight=0, view="default", **kwargs):
        """
        Create an SRV record in Infoblox.

        Args:
            name (str): Service name (e.g., _http._tcp.example.com)
            target (str): Target hostname for the service
            port (int): Port number where the service is running
            priority (int): Priority value (lower = higher priority)
            weight (int): Weight for records with the same priority
            view (str): DNS view to create the record in (default: "default")
            **kwargs: Additional SRV properties (ttl, comment, etc.)

        Returns:
            dict or None: JSON response containing reference to created SRV record, or None if request failed
        """
        data = {
            'name': name,
            'target': target,
            'port': port,
            'priority': priority,
            'weight': weight,
            'view': view
        }
        data.update(kwargs)
        return _post('record:srv', data)

    def modify_srv_record(self, ref, **kwargs):
        """
        Modify an existing SRV record.

        Args:
            ref (str): Object reference of the SRV record to modify (from find or create)
            **kwargs: Properties to modify (target, port, priority, weight, ttl, comment, etc.)

        Returns:
            dict or None: JSON response containing updated SRV record, or None if request failed
        """
        return _put(ref, data=kwargs)

    def delete_srv_record(self, ref):
        """
        Delete an SRV record.

        Args:
            ref (str): Object reference of the SRV record to delete (from find or create)

        Returns:
            dict or None: JSON response confirming deletion, or None if request failed
        """
        return _delete(ref)

class GRID():
    def get_grid_member(self, member_ref=None, host_name=None, ip_address=None):
        if member_ref:
            return _get(member_ref,
                        )
        else:
            params = {}
            if host_name:
                params['host_name'] = host_name
            if ip_address:
                params['ipv4addr'] = ip_address
            return _get('member', params=params,
                        )

    def update_grid_member(self, member_ref, **kwargs):
        return _put(member_ref, data=kwargs,
                    )

    def delete_grid_member(self, member_ref):
        return _delete(member_ref,
                       )

    def pull_grid_member(self, member_ref):
        data = {
            'function': 'pull'
        }
        return _post(f"{member_ref}?_function=pull",
                     data=data)
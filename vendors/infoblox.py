import requests
import json
import ssl
from auth import infoblox, SSH

headers = {"Content-Type": "application/json"}

class restapi():
    def __int__(self):
        self.headers = {"Content-Type": "application/json"}

    def _login(self):
        pass

    def get_Network_containers_all(self,netadd):
        return self._get(f"network?network_container={netadd}&_return_fields%2B=network_container",)
    def get_Network_container(self,netadd):
        """
        netadd(str): ex - 10.0.0.0/16
        """
        return self._get(f"network?network_container={netadd}&_return_fields%2B=network_container")
    def create_multiple_networks(self,netcontainer,networks):
        """
        Will create multiple networks under one network container.
        netcontainer(str): ex - 10.0.0.0/16
        networks(list): a list of dictionaries that will be used for the data to create the networks.
        """
        responses = []
        for net in networks:
            data = {
                "comment": f"Location:{net['location']}\r\nVlan:{net['vlan']}\r\nRouter:{net['router']}",
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

    def _get(self, queryurl):
        response = requests.get(infoblox.url + queryurl, headers=headers,
                                auth=(SSH.username, SSH.password),verify=False)
        if response.status_code == 200:
            return response.json()

    def _post(self, queryurl, jsondict):
        response = requests.post(infoblox.url + queryurl, data=json.dumps(jsondict), headers=headers,
                                 auth=(SSH.username, SSH.password),verify=False)
        if response.status_code == 200:
            return response.json()

    def _put(self, queryurl, jsondict):
        response = requests.put(infoblox.url + queryurl, data=json.dumps(jsondict), headers=headers,
                                auth=(SSH.username, SSH.password),verify=False)
        response.json()
        if response.status_code == 200:
            return response

    def _delete(self, queryurl, jsondict):
        response = requests.delete(infoblox.url + queryurl, data=json.dumps(jsondict), headers=headers,
                                   auth=(SSH.username, SSH.password),verify=False)
        response.json()
        if response.status_code == 200:
            return response

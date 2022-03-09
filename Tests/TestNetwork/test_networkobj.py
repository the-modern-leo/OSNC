### Local Packages ###
from Network.Network import Network

### Package imports
import unittest
from openpyxl import load_workbook

nodes = {'ebc': ('172.29.1.10','172.29.1.11'),
                 'remote': ('172.29.4.1','172.29.4.2'),
                 'park': ('172.29.1.12','172.29.1.13'),
                 'lib': ('172.29.1.14','172.29.1.15'),
                 'clinical': ('172.29.1.16','172.29.1.17'),
                 'fort': ('172.29.254.1','172.29.254.2'),
                 'wifi': ('172.29.1.20','172.29.1.21'),
                 '102tower': ('172.29.4.14'),
                 'voice': ('155.99.131.16','155.99.131.17'),
                 'shhc': ('172.29.4.24','172.29.4.25'),
                 'farm': ('172.29.4.13','172.29.4.16'),
                 'cv': ('172.20.241.1'),
                 'services': ('172.29.1.32','172.29.1.33'),
                 'sb': ('172.29.4.3'),
                 'rs': ('172.29.4.4'),
                 'west': ('172.29.4.7'),
                 'pw': ('172.29.4.8'),
                 'sjhc': ('172.29.4.9','172.29.4.15'),
                 'redwood': ('172.29.4.10'),
                 'tower': ('172.29.4.14'),
                 'bsb': ('172.29.4.17'),
                 'mv': ('172.29.4.19'),
                 'plaza': ('172.29.4.20','172.29.4.21'),
                 'sjcn': ('172.29.4.22','172.29.4.23'),
                 'som': ('155.99.131.18'),
                 }

class NetworkObject(unittest.TestCase):
    def test_ssh_connection_status(self):
        wb = load_workbook(r'/opt/project/Tests/TestNetwork/Report_All_UIT_-_NCI_-_Network_Devices.xlsx')
        sheet = wb['Sheet1']
        network_device_list = []
        for count, row in enumerate(sheet.rows):
            if count == 0: #skipping over headers
                continue
            network_device = {}
            network_device["device_name"] = row[0].value
            network_device["system_name"] = row[1].value
            network_device["ip_address"] = row[2].value
            network_device["Status"] = row[7].value
            network_device["row_obj"] = row
            network_device_list.append(network_device)
        n = Network()
        network_device_list_status = n.check_ssh_connection_status_threaded(network_device_list)
        for network_device in network_device_list_status:
            status = network_device["Status"]
            row_obj = network_device["row_obj"]
            wb['Sheet1'][f'{row_obj[7].coordinate}'] = status
        wb.save(filename=r'/opt/project/Tests/TestNetwork/Report_All_UIT_-_NCI_-_Network_Devices_status.xlsx')

    def test_get_all_nodes(self):
        """
        For getting all the routers information
        :return:
        """
        n = Network()
        n.get_all_node_information(nodes)






if __name__ == '__main__':
    unittest.main()

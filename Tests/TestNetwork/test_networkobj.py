### Local Packages ###
from Network.Network import Network

### Package imports
import unittest
from openpyxl import load_workbook


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
            network_device["status"] = row[13].value
            network_device["row_obj"] = row
            network_device_list.append(network_device)
        n = Network()
        network_device_list_status = n.check_ssh_connection_status_threaded(network_device_list)
        for network_device in network_device_list_status:
            device_name = network_device["device_name"]
            system_name = network_device["system_name"]
            ip_address = network_device["ip_address"]
            status = network_device["status"]
            row_obj = network_device["row_obj"]
            wb['Sheet1'][f'{row_obj[13].coordinate}'] = status
        wb.save(filename=r'/opt/project/Tests/TestNetwork/Report_All_UIT_-_NCI_-_Network_Devices_status.xlsx')


if __name__ == '__main__':
    unittest.main()

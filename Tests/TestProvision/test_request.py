import unittest
from Provision import gearrequest, db, settings
from common import database
import os
import auth
from . import settings as data

class SwitchChecker(unittest.TestCase):
    """
    Tests all the function in gear request
    """
    @classmethod
    def setUpClass(self):
        """
        Connect to the Read only test Database
        """
        global db_id
        db_id = str(id(self))
        self.engine = database.bind_engine(auth.Database.connectionstring)
         # not needed, but Tests DB creation syntax

    def test_add_gear_request_from_handler_only_switch(self):
        """
        Mocks the Handler call to this function for adding only one new switch only order.
        Will delete the entry after test
        """
        config_data = {'management_ip': '172.31.29.6',
                       'bldg': '589',
                       'room': '203',
                       'switch_model': 'c9300_48U',
                       'switch_number': '1',
                       'cablemanager': False,
                       'copper cables': {},
                       'fiber cables': {},
                       'cable manager': {},
                       'pickup date': '2020-01-24',
                       'hostname': 'sx1-589ehsl-203-ebc'}
        uid = 'u0800148'
        g = gearrequest.gearrequest()
        g.add_gear_request_from_handler(config_data, uid)
        result = g.get_gearrequests(ip='172.31.29.6',unid=uid,hostname='sx1-589ehsl-203-ebc')[0]
        try:
            result = g.get_gearrequests(ip='172.31.29.6',unid=uid,hostname='sx1-589ehsl-203-ebc')[0]
            self.assertIsInstance(result, dict)
            self.assertEqual(result['pickupdate'], '2020-01-24')
        except AssertionError as a:
            g = gearrequest.gearrequest()
            result = g.get_gearrequests(ip='172.31.29.6', unid=uid, hostname='sx1-589ehsl-203-ebc')[0]
            g.delete_request_gear(result['id'])
        try:
            propertyresult = g.get_property(tableid=result['id'])
            self.assertIsInstance(propertyresult,list)
            self.assertEqual(len(propertyresult),1)
            self.assertEqual(propertyresult[0]['buildingnumber'],'589')
            self.assertEqual(propertyresult[0]['roomnumber'], '203')
            self.assertEqual(propertyresult[0]['make'], 'Cisco')
            self.assertEqual(propertyresult[0]['geartype'], 'Switch')
            self.assertEqual(propertyresult[0]['quantity'], 1)
            self.assertEqual(propertyresult[0]['mac'], "UIT Mac")
            self.assertEqual(propertyresult[0]['model'], 'c9300_48U')

            g.delete_property(propertyresult[0]['id'])
            g.delete_request_gear(result['id'])
        except AssertionError as a:
            g = gearrequest.gearrequest()
            result = g.get_gearrequests(ip='172.31.29.6', unid=uid, hostname='sx1-589ehsl-203-ebc')[0]
            propertyresult = g.get_property(tableid=result['id'])
            for item in propertyresult:
                g.delete_property(item['id'])
            g.delete_request_gear(result['id'])

    def test_add_gear_request_from_handler_Multiple_switches(self):
        """
        Mocks the Handler call to this function for adding 3 new switch only order.
        Will delete the entry after test
        """
        config_data = {'management_ip': '172.31.29.6',
                       'bldg': '589',
                       'room': '203',
                       'switch_model': 'c9300_48U',
                       'switch_number': '3',
                       'copper cables': {},
                       'fiber cables': {},
                       'cable manager': {},
                       'pickup date': '2020-01-24',
                       'hostname': 'sx1-589ehsl-203-ebc'}
        uid = 'u0800148'
        g = gearrequest.gearrequest()
        g.add_gear_request_from_handler(config_data, uid)
        result = g.get_gearrequests(ip='172.31.29.6',unid=uid,hostname='sx1-589ehsl-203-ebc')[0]
        try:
            result = g.get_gearrequests(ip='172.31.29.6',unid=uid,hostname='sx1-589ehsl-203-ebc')[0]
            self.assertIsInstance(result, dict)
            self.assertEqual(result['pickupdate'], '2020-01-24')
        except AssertionError as a:
            g = gearrequest.gearrequest()
            result = g.get_gearrequests(ip='172.31.29.6', unid=uid, hostname='sx1-589ehsl-203-ebc')[0]
            g.delete_request_gear(result['id'])
        try:
            propertyresult = g.get_property(tableid=result['id'])
            self.assertIsInstance(propertyresult, list)
            self.assertEqual(len(propertyresult), 3)
            for item in propertyresult:
                self.assertEqual(item['buildingnumber'],'589')
                self.assertEqual(item['roomnumber'], '203')
                self.assertEqual(item['make'], 'Cisco')
                self.assertEqual(item['geartype'], 'Switch')
                self.assertEqual(item['quantity'], 1)
                self.assertEqual(item['mac'], "UIT Mac")
                self.assertEqual(item['model'], 'c9300_48U')
                g.delete_property(item['id'])
            g.delete_request_gear(result['id'])
        except AssertionError as a:
            g = gearrequest.gearrequest()
            result = g.get_gearrequests(ip='172.31.29.6', unid=uid, hostname='sx1-589ehsl-203-ebc')[0]
            propertyresult = g.get_property(tableid=result['id'])
            for item in propertyresult:
                g.delete_property(item['id'])
            g.delete_request_gear(result['id'])

    def test_add_gear_request_from_handler_switches_and_cablemanager(self):
        """
        Mocks the Handler call to this function for adding 3 new switch, and
        2 types of Cable Managers
        Will delete the entry after test
        """
        config_data = {'management_ip': '172.31.29.6',
                       'bldg': '589',
                       'room': '203',
                       'switch_model': 'c9300_48U',
                       'switch_number': '3',
                       'copper cables': {},
                       'fiber cables': {},
                       'cable manager': {'WM1455': '2', 'WM1435': '3'},
                       'pickup date': '2020-01-24',
                       'hostname': 'sx1-589ehsl-203-ebc'}

        uid = 'u0800148'
        g = gearrequest.gearrequest()
        g.add_gear_request_from_handler(config_data, uid)
        try:
            result = g.get_gearrequests(ip='172.31.29.6',unid=uid,hostname='sx1-589ehsl-203-ebc')[0]
            self.assertIsInstance(result, dict)
            self.assertEqual(result['pickupdate'], '2020-01-24')
        except AssertionError as a:
            g = gearrequest.gearrequest()
            result = g.get_gearrequests(ip='172.31.29.6', unid=uid, hostname='sx1-589ehsl-203-ebc')[0]
            g.delete_request_gear(result['id'])
        try:
            propertyresult = g.get_property(tableid=result['id'])
            self.assertIsInstance(propertyresult, list)
            self.assertEqual(len(propertyresult), 5)
            for item in propertyresult:
                if item['geartype'] == 'Switch':
                    self.assertEqual(item['buildingnumber'],'589')
                    self.assertEqual(item['roomnumber'], '203')
                    self.assertEqual(item['make'], 'Cisco')
                    self.assertEqual(item['geartype'], 'Switch')
                    self.assertEqual(item['quantity'], 1)
                    self.assertEqual(item['mac'], "UIT Mac")
                    self.assertEqual(item['model'], 'c9300_48U')
                elif item['geartype'] == 'Cable Manager':
                    self.assertEqual(item['buildingnumber'], '589')
                    self.assertEqual(item['roomnumber'], '203')
                    self.assertEqual(item['make'], 'Unknown')
                    self.assertEqual(item['geartype'], 'Cable Manager')
                    self.assertEqual(item['mac'], "UIT Mac")
                    self.assertEqual(item['model'], 'Unknown')
                    if item['itemnumber'] == 'WM1455':
                        self.assertEqual(item['quantity'], 2)
                    elif item['itemnumber'] == 'WM1435':
                        self.assertEqual(item['quantity'], 3)
                g.delete_property(item['id'])
            g.delete_request_gear(result['id'])

        except AssertionError as a:
            g = gearrequest.gearrequest()
            result = g.get_gearrequests(ip='172.31.29.6', unid=uid, hostname='sx1-589ehsl-203-ebc')[0]
            propertyresult = g.get_property(tableid=result['id'])
            for item in propertyresult:
                g.delete_property(item['id'])
            g.delete_request_gear(result['id'])

    def test_add_gear_request_from_handler_switches_cablemanagers_coppercables(self):
        """
        Mocks the Handler call to this function for adding 3 new switch,
        2 types of cablemanagers, and copper cables
        Will delete the entry after test
        """
        config_data = {'management_ip': '172.31.29.6',
                       'bldg': '589',
                       'room': '203',
                       'switch_model': 'c9300_48U',
                       'switch_number': '4',
                       'cablemanager': True,
                       'copper cables': {'MC68T0102': '1',
                                         'MC68T0202': '1',
                                         'MC68T0302': '1',
                                         'MC68T0402': '1',
                                         'MC68T0502': '1',
                                         'MC68T0602': '1',
                                         'MC68T0702': '1',
                                         'MC68T0802': '1',
                                         'MC68T0902': '1',
                                         'MC68T1002': '1',
                                         'MC68T1502': '1',
                                         'MC68T2002': '1',
                                         'MC68T2502': '1'},
                       'fiber cables': {},
                       'cable manager': {'WM1455': '2',
                                         'WM1435': '3'},
                       'pickup date': '2020-01-24',
                       'hostname': 'sx1-589ehsl-203-ebc'}

        uid = 'u0800148'
        g = gearrequest.gearrequest()
        g.add_gear_request_from_handler(config_data, uid)
        try:
            result = g.get_gearrequests(ip='172.31.29.6',unid=uid,hostname='sx1-589ehsl-203-ebc')[0]
            self.assertIsInstance(result, dict)
            self.assertEqual(result['pickupdate'], '2020-01-24')
        except AssertionError as a:
            g = gearrequest.gearrequest()
            result = g.get_gearrequests(ip='172.31.29.6', unid=uid, hostname='sx1-589ehsl-203-ebc')[0]
            g.delete_request_gear(result['id'])
        try:
            propertyresult = g.get_property(tableid=result['id'])
            self.assertIsInstance(propertyresult, list)
            self.assertEqual(len(propertyresult), 19)
            for item in propertyresult:
                self.assertEqual(item['buildingnumber'], '589')
                self.assertEqual(item['roomnumber'], '203')
                self.assertEqual(item['mac'], "UIT Mac")
                if item['geartype'] == 'Switch':
                    self.assertEqual(item['make'], 'Cisco')
                    self.assertEqual(item['geartype'], 'Switch')
                    self.assertEqual(item['quantity'], 1)
                    self.assertEqual(item['model'], 'c9300_48U')
                elif item['geartype'] == 'Cable Manager':
                    self.assertEqual(item['make'], 'Unknown')
                    self.assertEqual(item['geartype'], 'Cable Manager')
                    self.assertEqual(item['model'], 'Unknown')
                    if item['itemnumber'] == 'WM1455':
                        self.assertEqual(item['quantity'], 2)
                    elif item['itemnumber'] == 'WM1435':
                        self.assertEqual(item['quantity'], 3)
                elif item['geartype'] == 'Patch Cable':
                    self.assertEqual(item['make'], 'Clearlinks')
                    self.assertEqual(item['geartype'], 'Patch Cable')
                    self.assertEqual(item['model'], 'Cat 6')
                    self.assertEqual(item['quantity'], 1)
                    self.assertIn(item['itemnumber'],settings.ethernetcable)
                    self.assertIn(item['description'], settings.ethernetcable)

                g.delete_property(item['id'])
            g.delete_request_gear(result['id'])

        except AssertionError as a:
            g = gearrequest.gearrequest()
            result = g.get_gearrequests(ip='172.31.29.6', unid=uid, hostname='sx1-589ehsl-203-ebc')[0]
            propertyresult = g.get_property(tableid=result['id'])
            for item in propertyresult:
                g.delete_property(item['id'])
            g.delete_request_gear(result['id'])
    def test_add_gear_request_from_handler_all(self):
        """
        Mocks the Handler call to this function for adding 3 new switch,
        2 types of cablemanagers, copper cables, and fiber cables
        Will delete the entry after test
        """
        config_data = {'management_ip': '172.31.29.6',
                       'bldg': '589',
                       'room': '203',
                       'switch_model': 'c9300_48U',
                       'switch_number': '4',
                       'cablemanager': True,
                       'copper cables': {'MC68T0102': '1',
                                         'MC68T0202': '1',
                                         'MC68T0302': '1',
                                         'MC68T0402': '1',
                                         'MC68T0502': '1',
                                         'MC68T0602': '1',
                                         'MC68T0702': '1',
                                         'MC68T0802': '1',
                                         'MC68T0902': '1',
                                         'MC68T1002': '1',
                                         'MC68T1502': '1',
                                         'MC68T2002': '1',
                                         'MC68T2502': '1'},
                       'fiber cables': {'SMLCLC01': '1', 'MMLCLC01': '1'},
                       'cable manager': {'WM1455': '2',
                                         'WM1435': '3'},
                       'pickup date': '2020-01-24',
                       'hostname': 'sx1-589ehsl-203-ebc'}
        uid = 'u0800148'
        g = gearrequest.gearrequest()
        g.add_gear_request_from_handler(config_data, uid)
        try:
            result = g.get_gearrequests(ip='172.31.29.6',unid=uid,hostname='sx1-589ehsl-203-ebc')[0]
            self.assertIsInstance(result, dict)
            self.assertEqual(result['pickupdate'], '2020-01-24')
        except AssertionError as a:
            g = gearrequest.gearrequest()
            result = g.get_gearrequests(ip='172.31.29.6', unid=uid, hostname='sx1-589ehsl-203-ebc')[0]
            g.delete_request_gear(result['id'])
        try:
            propertyresult = g.get_property(tableid=result['id'])
            self.assertIsInstance(propertyresult, list)
            self.assertEqual(len(propertyresult), 19)
            for item in propertyresult:
                self.assertEqual(item['buildingnumber'], '589')
                self.assertEqual(item['roomnumber'], '203')
                self.assertEqual(item['mac'], "UIT Mac")
                if item['geartype'] == 'Switch':
                    self.assertEqual(item['make'], 'Cisco')
                    self.assertEqual(item['geartype'], 'Switch')
                    self.assertEqual(item['quantity'], 1)
                    self.assertEqual(item['model'], 'c9300_48U')
                elif item['geartype'] == 'Cable Manager':
                    self.assertEqual(item['make'], 'Unknown')
                    self.assertEqual(item['geartype'], 'Cable Manager')
                    self.assertEqual(item['model'], 'Unknown')
                    if item['itemnumber'] == 'WM1455':
                        self.assertEqual(item['quantity'], 2)
                    elif item['itemnumber'] == 'WM1435':
                        self.assertEqual(item['quantity'], 3)
                elif item['geartype'] == 'Patch Cable':
                    self.assertEqual(item['make'], 'Clearlinks')
                    self.assertEqual(item['geartype'], 'Patch Cable')
                    self.assertEqual(item['model'], 'Cat 6')
                    self.assertEqual(item['quantity'], 1)
                    self.assertIn(item['itemnumber'], settings.ethernetcable.keys())
                    self.assertIn(item['description'], settings.ethernetcable.values())
                g.delete_property(item['id'])
            ebcresult = g.get_ebc(tableid=result['id'])
            self.assertIsInstance(ebcresult, list)
            self.assertIsInstance(ebcresult[0], dict)
            self.assertEqual(len(ebcresult), 2)
            for item in ebcresult:
                self.assertEqual(item['fiberquantity'],1)
                self.assertEqual(item['fibermac'], "UIT MAC")
                g.delete_ebc(item['id'])
            g.delete_request_gear(result['id'])

        except AssertionError as a:
            g = gearrequest.gearrequest()
            result = g.get_gearrequests(ip='172.31.29.6', unid=uid, hostname='sx1-589ehsl-203-ebc')[0]
            propertyresult = g.get_property(tableid=result['id'])
            ebcresult = g.get_ebc(tableid=result['id'])
            for item in ebcresult:
                g.delete_ebc(item['id'])
            for item in propertyresult:
                g.delete_property(item['id'])
            g.delete_request_gear(result['id'])

    def test_update_request_gear(self):
        uid = 'u0800148'
        g = gearrequest.gearrequest()
        result = g.update_database_from_handler(data.deardata_ddc_complete_change,uid)

        
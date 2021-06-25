from openpyxl import load_workbook
from SSH.ParamikoConnection import SwitchAccess
import os
import re



class generate_test_files:
    def __init__(self,filename):
        """
        Creates several files for switches
        :return:
        """
        wb = load_workbook(filename=filename)
        self.sheet = wb['Sheet1']
        self.rows = []
        self.filenames = []
        self.parent_dir = "/opt/project/Tests/TestNetwork/device_list/"
        self.directory = None

    def create_folder(self):
        """
        Creates the containing folder for files to go into
        :return:
        """
        try:

            path = os.path.join(self.parent_dir, self.directory)
            if not os.path.isdir(path):
                os.mkdir(path)
        except Exception as E:
            print(E)
            pass

    def create_file_placeholders(self):
        """
        Will create the file title, and placeholders
        :return:
        """
        try:
            for count, row in enumerate(self.sheet.rows):
                if count != 0:
                    self.rows.append(row)

            for r in self.rows:
                hardware = re.sub(' ','_',r[4].value).lower()
                software = re.sub(' ', '_', r[2].value).lower()
                # software = re.sub('\.', '_', software).lower()
                s = SwitchAccess(r[1].value)
                try:
                    s.login()
                except Exception as e:
                    pass
                filename = f'{self.parent_dir}{self.directory}/{hardware}:{software}.py'
                if os.path.isfile(filename):
                    continue
                self.filenames.append(filename)
                with open(filename, 'a+') as e:
                    e.write(f"ip_address = '{r[1].value}'" + os.linesep)
                    e.write(f"software = 'software'" + os.linesep)
                    e.write(f"hardware = 'hardware'" + os.linesep)
                    e.write(f"read_results = {{" + os.linesep)
                    if ('cisco' in r[4].value.lower() or 'catalyst' in r[4].value.lower() or 'nexus' in r[4].value.lower()
                    or 'ie30008tc' in r[4].value.lower()):
                        command_list = ['show version', 'show run', 'show int status', 'show run | section interface',
                                        'show run | in interface', 'show interface link', 'show interface',
                                        'show inventory',
                                        'show interface counters', 'show cdp nei detail', 'show module all',
                                        'show module',
                                        'show run | section snmp', 'show run | in snmp', 'show snmp user',
                                        'show access-list',
                                        'show run | section logging', 'show run | in logging', 'show mac address-table',
                                        'show run | section tacacs',
                                        'show run | in tacacs', 'show power inline', 'show environment all']
                        for com in command_list:
                            results = s.conn.send_command(com)
                            e.write(f""" '{str(com)}':""" + f'"""{str(results)}""",'  + os.linesep)
                    else:
                        command_list = ['show version', 'show run', 'show interfaces brief',
                                        'show run | in interface', 'show interface',
                                        'show lldp nei detail', 'show run | in snmp', 'show snmp user',
                                        'show access-list all', 'show run | in logging', 'show mac address-table',
                                        'show run | in tacacs']
                        for com in command_list:
                            results = s.conn.send_command(com)
                            e.write(f""" '{str(com)}':""" + f'"""{str(results)}""",'  + os.linesep)
                    e.write(f"}}" + os.linesep)
        except Exception as E:
            print(E)
            pass

class Generate_test_switches_files(generate_test_files):
    def __init__(self,*args):
        """
        Creates several files for switches
        :return:
        """
        super(Generate_test_switches_files, self).__init__(*args)
        self.directory = "Switches"

if __name__=="__main__":
    g = Generate_test_switches_files('/opt/project/Tests/TestNetwork/device_list/Test_switch_devices.xlsx')
    g.create_folder()
    g.create_file_placeholders()
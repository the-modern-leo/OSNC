from datetime import datetime, date

import logging
import netmiko
import re
import threading


class WirelessTools:
    """
    This class is a connection of methods that get information from wireless
    controllers and logging servers to help diagnose wireless issues.

    Args:
        wian_user (str): Wian username.
        wian_password (str): Wian password.
        log_user (str): Logging servers (NALO/DHLO) username.
        log_password (str): Logging servers (NALO/DHLO) password.
        sno (ServiceNow): Service Now object
    """
    def __init__(self, wian_user, wian_password, log_user, log_password):
        # Wireless Controller Auth
        self.wian_user = wian_user
        self.wian_password = wian_password
        # Nalo/Dhlo Auth
        self.log_user = log_user
        self.log_password = log_password
        # Threading Junk
        self.threads = {}
        self.lock = threading.Lock()

    def try_ssh_connection(self, host, is_wian, tries=3):
        """
        Creates a paramiko ssh client into given host with correct
        credidentials.

        Args:
            host (str): Host or IP to connect to.
            is_wian (bool): If true uses wian credidentials, otherwise uses
                logging credidentials.
            tries (int): Optional - Number of tries to connect to host. Default
                is 3.

        Returns:
            netmiko.ConnectHandler: Returns client if connection is successful.

        Raises:
            ConnectionError: Caused if connection fails after given attempts.
        """
        connection_info = {
            "device_type": "cisco_wlc" if is_wian else "linux",
            "host": host,
            "username": self.wian_user if is_wian else self.log_user,
            "password": self.wian_password if is_wian else self.log_password}
            # "fast_cli": True}
        if not is_wian:
            connection_info["secret"] = self.log_password
        # Trys to connect 3 times
        for i in range(0, tries):
            try:
                ssh = netmiko.ConnectHandler(**connection_info)
                return ssh
            except:
                if i == (tries - 1):
                    logging.info('', exc_info=True)
                    raise ConnectionError(f"Could not connect to {host}.")

    def update_thread(self, thread_id, finished, error, message, data=None):
        """
        Updates thread status in thread dictionary. Threadsafe.

        Args:
            thread_id (int): ID of thread in thread dictionary.
            finished (bool): Whether the thread is finished running.
            error (bool): Whether the thread has run into an error.
            message (str): Status message of the thread. All past messages for a
                given thread_id are stored.
            data (obj): Return data from the thread.
        """
        self.lock.acquire()
        if thread_id in self.threads:
            self.threads[thread_id]['message'].append(message)
            message = self.threads[thread_id]['message']
        else:
            message = [message]
        self.threads[thread_id] = {
                "finished": finished,
                "error": error,
                "message": message,
                "data": data}
        self.lock.release()

    def create_all_wlc_connections(self):
        """
        Currently not in use.
        Creates a connection to every WLC. Uses threads to start connection
        simultaneously.

        Returns:
            list: List of open connections to WLC. If a connection cannot be
            made, it won't be returned in this list.
        """
        def open_connection(host, lock, connections):
            try:
                ssh = self.try_ssh_connection(host, True)
                ssh.send_command("config disable paging")
            except ConnectionError:
                logging.info(f"failed to connect to {host}")
                return
            lock.acquire()
            connections.append(ssh)
            lock.release()

        connections = []
        threads = []
        lock = threading.Lock()
        for i in range(1, 6):
            new_thread = threading.Thread(target=open_connection, args=[
                        f"r1-wlc{i}-mgmt", lock, connections])
            new_thread.start()
            threads.append(new_thread)

        for thread in threads:
            thread.join()
        return connections

    def disconnect_all_wlc_connections(self, wlc_connections):
        """
        Currently not in use.
        Disconnects open wlc connections from provided list. Uses threads to
        disconnect connections simultaneously.

        Args:
            wlc_connections (list): List of open connections provided from
            create_all_wlc_connections().
        """
        threads = []
        for ssh in wlc_connections:
            new_thread = threading.Thread(target=lambda x: x.disconnect(),
                    args=[ssh])
            new_thread.start()
            threads.append(new_thread)

        for thread in threads:
            thread.join()

    def get_floor_status(self, wlc_connections, bldg, floor):
        """
        Currently not in use.
        Finds the total amount of APs on a given floor and building. APs are
        identified by their name "ap-bldg#-floor#".

        Args:
            wlc_connections (list): List of open connects to all WLCs.
            bldg (int): Building number.
            floor (int): Floor number.

        Returns:
            int: Number of APs found for given floor and building.
        """
        ap_amount = 0
        for ssh in wlc_connections:
            output = ssh.send_command(f"show ap summary").split('\n')
            for line in output:
                if line.startswith(f"ap-{bldg:04}-{floor}-"):
                    ap_amount += 1
        return ap_amount

    def find_client_ap(self, wlc_connections, mac):
        """
        Currently not in use.
        Given a client's MAC address, this function will find the ap this client
        is connected too.

        Args:
            wlc_connections (list): List of open connects to all WLCs.
            mac (str): Client MAC address, lowercase seperated by colons every
            two characters.

        Returns:
            tuple or None: Returns AP name and WLC index if the
            given client is found; Otherwise returns nothing.
        """
        client_ap = None
        for ssh in wlc_connections:
            output = ssh.send_command('show client summary').split('\n')
            # Greps for MAC address manually cause netmiko just CAN'T
            for line in output:
                if mac in line:
                    client_ap = line.split()[1]
                    break
            if client_ap:
                return client_ap, wlc_connections.index(ssh)

    def get_client_wireless_status(self, ssh, mac):
        """
        Currently not in use.
        Retrieves multiple pieces of information about a given client.

        Args:
            ssh (netmiko.ConnectionHandler): Connection to WLC that client is
            located on.
            mac (str): Client MAC address, lowercase seperated by colons every
            two characters.

        Returns:
            dict: Dictionary containing client profilename, ip address, uptime,
            and signal strength.
        """
        output = ssh.send_command(f"show client detail {mac}").split('\n')
        return_dict = {}
        for line in output:
            if "Wireless LAN Profile Name" in line:
                return_dict["profilename"] = line.split()[-1]
            elif line.strip().startswith("IP Address"):
                return_dict["ip"] = line.split()[-1]
            elif "Connected For" in line:
                seconds=int(line.split()[-2])
                days = seconds // 86400
                seconds = seconds % 86400
                hours = seconds // 3600
                seconds = seconds % 3600
                minutes = seconds // 60
                seconds = seconds % 60
                return_dict["uptime"] = (f"{days} days, {hours} h " +
                        f"{minutes} m {seconds} s")
            elif "Radio Signal Strength Indicator" in line:
                signal_strength = abs(int(line.split()[-2]))
        return return_dict

    def get_ap_status(self, ssh, ap_name):
        """
        Currently not in use.
        Using an AP's name, this will retrieve related information about ap.

        Args:
            ssh (netmiko.ConnectionHandler): Connection to WLC that client is
            located on.
            ap_name (str): AP name.


        Returns:
            dict: Dictonary containing all the information. Uptime, client
            amount, and airquality are given.
        """
        # Up Time
        ap_up_time = None
        output = ssh.send_command("show ap uptime").split('\n')
        for line in output:
            if line.startswith(ap_name):
                ap_up_time = re.split(r" {2,}", line)[2]
                break
        # AP Client Amount
        ap_client_amount = None
        output = ssh.send_command(f"show ap summary").split('\n')
        for line in output:
            if line.startswith(ap_name):
                ap_client_amount = re.split(r" {2,}", line)[-2]
                break
        # Air quality
        ap_802_11a = None
        ap_802_11b = None
        output = ssh.send_command("show 802.11a cleanair air-quality summary"
                ).split('\n')
        for line in output:
            if line.startswith(ap_name):
                ap_802_11a = line.split()
                break
        output = ssh.send_command("show 802.11b cleanair air-quality summary"
                ).split('\n')
        for line in output:
            if line.startswith(ap_name):
                ap_802_11b = line.split()
                break
        output = ssh.send_command(f"show ap auto-rf 802.11a {ap_name}").split(
                '\n')
        inter_devices = 0
        for i in range(len(output)):
            if "Persistent Interference Devices" in output[i]:
                # Removes header and trademark lines to get device amount
                inter_devices = len(output) - i - 5
                break

        return {"located": True,
                "name": ap_name,
                "clients": ap_client_amount,
                "uptime": ap_up_time,
                "interfering": inter_devices,
                "802.11a_avg": ap_802_11a[2] if ap_802_11a else "n/a",
                "802.11a_min": ap_802_11a[3] if ap_802_11a else "n/a",
                "802.11b_avg": ap_802_11b[2] if ap_802_11b else "n/a",
                "802.11b_min": ap_802_11b[3] if ap_802_11b else "n/a"}

    def build_ap_config(self, apname, a_power, b_power, a_channel, b_channel,
            a_width):
        """
        Generate AP configs for a controller.

        Args:
            apname (str): AP name.
            a_power (int): 5Ghz power, from 1 to 7
            b_power (int): 2.4Ghz power, from 1 to 7
            a_channel (int): 5Ghz channel (39 to 165)
            b_channel (int): 2.4Ghz channel (1 to 11)
            a_width (int): 5Ghz channel width, integer in Mhz (20 or 40)

        Returns:
            str: Contains the AP config lines to copy and paste.
        """
        int(a_power)
        int(b_power)
        int(a_channel)
        int(b_channel)
        int(a_width)
        return ("config 802.11b disable " + apname +
                "\nconfig 802.11b txpower ap " + apname + " " + str(b_power) +
                "\nconfig 802.11b channel ap " + apname + " " + str(b_channel) +
                "\nconfig 802.11b enable " + apname + "\n\n" +
                "config 802.11a disable " + apname +
                "\nconfig 802.11a txpower ap " + apname + " " + str(a_power) +
                "\nconfig 802.11a chan_width " + apname + " " + str(a_width) +
                "\nconfig 802.11a channel ap " + apname + " " + str(a_channel) +
                "\nconfig 802.11a enable " + apname)

########################### Client History Methods ###########################
    def organize_logs_by_hour(self, logs):
        """
        Organizes logs by hour into a dictionary.

        Args:
            logs (list): List of logging lines.

        Returns:
            dict: Contains logs by each hour. Key is hour and value is list of
            logs.
        """
        organized_logs = {}
        for hour in range(0, 24):
            organized_logs[hour] = []
        for line in logs:
            if not line:
                continue
            timestamp = line.split(' ', 1)[0]
            line_datetime = datetime.strptime(timestamp,
                    r"%Y-%m-%dT%H:%M:%S-06:00")
            organized_logs[line_datetime.hour].append(line)
        for hour in range(0, 24):
            organized_logs[hour].sort()
        return organized_logs

    def get_client_log_info(self, mac, logdate):
        """
        Gets client history, hour by hour, for a given date.

        Args:
            mac (str): Client MAC address.
            logdate (date): Day for logs.

        Returns:
            dict: Dictonary containing client info for every hour in a day.
        """
        ssh = self.try_ssh_connection("swat", False)
        # Sometimes, trying to enable (sudo su) will fail, so try it 3 times
        # before giving up.
        tries = 0
        while True:
            tries += 1
            try:
                ssh.enable() # will this work?
                break
            except Exception as e:
                if tries > 2:
                    logging.info('', exc_info=True)
                    raise Exception("Could not enable sudo su on swat " +
                            "(try again?)")
        final_dict = {}
        path = "/home/u0569223/wlc-files/"
        for hour in range(0, 24):
            final_dict[hour] = {}
            filename = (f"r1-wlc*-{logdate.isoformat()}-{hour:02}:00.log.gz")
            output = ssh.send_command(f"zcat {path}{filename} | grep {mac}")
            for line in output.split('\n'):
                line_split = line.split(' ', 1) # Get MAC address from line
                if mac != line_split[0]:
                    continue
                line = [sect.strip() for sect in line_split[-1].split('  ') if
                        sect.strip()]
                # Show Client Summary
                if (len(line) == 10 and line[1].isdigit and line[3].isdigit and
                        line[6].isdigit):
                    final_dict[hour]["auth"] = line[4]
                # Show Client Summary SSID IP Username Devicetype Security
                elif (len(line) == 6 or len(line) == 9):
                    final_dict[hour]["ap"] = line[0]
                    final_dict[hour]["network"] = line[2]
                    final_dict[hour]["ip"] = line[3]
                    final_dict[hour]["device"] = line[4]
                    final_dict[hour]["username"] = line[5]
        ssh.disconnect()
        return final_dict

    def get_ap_log_info(self, bldg, floor, logdate):
        """
        Gets a day of information about all aps on a given floor of a bldg.

        Args:
            bldg (int): Building number.
            floor (int): Floor number.
            logdate (date): Day for logs.

        Returns:
            dict: Dictonary containing ap information for every hour in a day.
        """
        ssh = self.try_ssh_connection("swat", False)
        # Sometimes, trying to enable (sudo su) will fail, so try it 3 times
        # before giving up.
        tries = 0
        while True:
            tries += 1
            try:
                ssh.enable() # will this work?
                break
            except Exception as e:
                if tries > 2:
                    logging.info('', exc_info=True)
                    raise Exception("Could not enable sudo su on swat " +
                            "(try again?)")
        final_dict = {}
        path = "/home/u0569223/wlc-files/"
        ap_pre = f"ap-{bldg:04}-{floor}"
        for hour in range(0, 24):
            final_dict[hour] = {}
            filename = (f"r1-wlc*-{logdate.isoformat()}-{hour:02}:00.log.gz")
            output = ssh.send_command(f"zcat {path}{filename} | grep {ap_pre}")
            for line in output.split('\n'):
                if not line.startswith(ap_pre):
                    continue
                # Splits on 2 or more spaces
                line = [sect.strip() for sect in line.split('  ')
                        if sect.strip()]
                ap_name = line[0]
                if ap_name not in final_dict[hour]:
                    final_dict[hour][ap_name] = {}
                # show ap summary
                if len(line) == 9 and line[1].isdigit and line[7].isdigit:
                    final_dict[hour][ap_name]["clients"] = line[7]
                # show ap uptime
                elif len(line) == 4 and "days" in line[2] and "days" in line[3]:
                    final_dict[hour][ap_name]["uptime"] = line[2]
                    final_dict[hour][ap_name]["associationtime"] = line[3]
                # show 802.11* cleanair air-quality summary
                elif (len(line) == 5 and line[1].isdigit and line[2].isdigit and
                        line[3].isdigit and line[4].isdigit):
                    if "airquality" not in final_dict[hour][ap_name]:
                        final_dict[hour][ap_name]["airquality"] = {}
                    if int(line[1]) < 11:
                        final_dict[hour][ap_name]["airquality"]["b"] = {
                                "avg": line[2], "min": line[3]}
                    else:
                        final_dict[hour][ap_name]["airquality"]["a"] = {
                                "avg": line[2], "min": line[3]}
        ssh.disconnect()
        return final_dict

    def get_auth_logs(self, mac, log_date, uid=None):
        """
        Gets a day of authentication logs with a MAC address and a possible UID.

        Args:
            mac (str): Lowercase colon formated MAC address.
            log_date (date): Day for logs.
            uid (str): Optional - UID of client. If provided will provide
                another section with UID logs.

        Returns:
            dict: All logs found. If there are errors when gathering logs, error
            messages will also be contained in this return. Logs are under the
            key for each hour.
        """
        ssh = self.try_ssh_connection("nalo", False)
        # Calculates today's date and past days log date
        today = date.today()
        log_day = (today - log_date).days - 1
        # Getting Logs with MAC
        output = []
        error = ""
        try:
            if log_date == today: # Different syntax for today's logs
                output.extend(ssh.send_command("cat /var/log/cisco/*.log | " +
                        f"grep {mac}").split('\n'))
            else:
                output.extend(ssh.send_command("cat /var/log/cisco/*.log." +
                        f"{log_day} | grep {mac}").split('\n'))
        except Exception as e:
            error = str(e)
        # Formatting and organizing logs into dictionary
        final_logs = self.organize_logs_by_hour(output)
        for hour in range(0, 24):
            log_str = "Logs from MAC address:\n"
            if final_logs[hour]:
                log_str += '\n'.join(final_logs[hour]) + "\n\n"
            elif not error:
                log_str += "No logs found\n\n"
            else:
                log_str += (f"Error getting logs on {log_date} with {mac} " +
                        f"(try again?)\n{error}\n")
            final_logs[hour] = log_str
        # Getting Logs with UID
        if uid:
            output = []
            error = ""
            try:
                if log_date == today: # Different syntax for today's logs
                    output.extend(ssh.send_command("cat /var/log/cisco/*.log | "
                            + f"grep {uid}").split('\n'))
                else:
                    output.extend(ssh.send_command("cat /var/log/cisco/*.log." +
                            f"{log_day} | grep {uid}").split('\n'))
            except Exception as e:
                error = str(e)
            # Formatting and organizing logs into dictionary
            uid_logs = self.organize_logs_by_hour(output)
            for hour in range(0, 24):
                log_str = "Logs from UID:\n"
                if uid_logs[hour]:
                    log_str += '\n'.join(uid_logs[hour]) + "\n\n"
                elif not error:
                    log_str += "No logs found\n\n"
                else:
                    log_str += (f"Error getting logs on {log_date} with {uid} "
                            + f"(try again?)\n{error}\n")
                final_logs[hour] += log_str
        # Cleaning Up connection
        ssh.disconnect()
        return final_logs

    def get_dhcp_logs(self, mac, log_date):
        """
        Gets a day of DHCP logs from DHLO using a MAC address.

        Args:
            mac (str): Lowercase colon formated MAC address.
            log_date (date): Day for logs.

        Returns:
            dict: All logs found. If there are errors when gathering logs, error
            messages will also be contained in this return. Logs are under the
            key for each hour.
        """
        ssh = self.try_ssh_connection("dhlo", False)
        # Sometimes, trying to enable (sudo su) will fail, so try it 3 times
        #   before giving up.
        tries = 0
        while True:
            tries += 1
            try:
                ssh.enable() # will this work?
                break
            except Exception as e:
                if tries > 2:
                    logging.info('', exc_info=True)
                    raise Exception("Could not enable sudo su on dhlo " +
                            "(try again?)")
        # Calculates today's date and past days log date
        today = date.today()
        log_day = (today - log_date).days - 1
        # Getting Logs with MAC
        output = []
        error = ""
        try:
            if log_date == today: # Different syntax for today's logs
                output.extend(ssh.send_command("cat /var/log/cisco/*.log | " +
                        f"grep {mac}").split('\n'))
            else:
                output.extend(ssh.send_command("cat /var/log/cisco/*.log." +
                        f"{log_day} | grep {mac}").split('\n'))
        except Exception as e:
            error = str(e)
        # Formatting and organizing logs into dictionary
        final_logs = self.organize_logs_by_hour(output)
        for hour in range(0, 24):
            log_str = "Logs from MAC address:\n"
            if final_logs[hour]:
                log_str += '\n'.join(final_logs[hour]) + "\n\n"
            elif not error:
                log_str += "No logs found\n\n"
            else:
                log_str += (f"Error getting logs on {log_date} with {mac} " +
                        f"(try again?)\n{error}\n")
            final_logs[hour] = log_str
        # Cleaning Up connection
        ssh.disconnect()
        return final_logs

class ClientHistoryThread(threading.Thread):
    def __init__(self, wtools, thread_id, mac, bldg, floor, logdate, uid=None):
        """
        Thread to retrieve all client historical information. This includes
        client information, ap information, authentication logs and dhcp logs.
        All information is for a given day, organized by each hour.

        Args:
            wtools (WirelessTools): WirelessTools Object.
            thread_id (int): Thread ID for each instance of this thread.
            mac (str): Client MAC address, lowercase colon seperated.
            bldg (int): Building number.
            floor (int): Floor number.
            logdate (date): Date of past day to get information from.
            uid (str): Optional - Client UID.
        """
        threading.Thread.__init__(self)
        self.wtools = wtools
        self.thread_id = thread_id
        self.mac = mac
        self.bldg = bldg
        self.floor = floor
        self.logdate = logdate
        self.uid = uid

    def run(self):
        """
        Runs the thread.
        """
        wlc_connections = []
        try:
            # This function runs any provided function and returns its output
            def thread_wrapper(*args, **kwargs):
                lock = kwargs['lock']
                function = kwargs['func']
                return_dict = kwargs['return']
                thread_id = kwargs['id']
                message = kwargs['message']
                update_func = kwargs['update']
                try:
                    return_value = function(*args)
                    update_func(thread_id, False, False,
                            f"Finished {message}....")
                    lock.acquire()
                    # Uses provided function as key to return dictionary
                    return_dict[function] = return_value
                    lock.release()
                except Exception as e:
                    logging.info('', exc_info=True)
                    return_dict[function] = e

            thread_return_dict = dict()
            lock = threading.Lock()
            self.wtools.update_thread(self.thread_id, False, False,
                    "Starting all threads...")
            # Client RF History thread
            client = threading.Thread(target=thread_wrapper,
                    args=[self.mac, self.logdate], kwargs={
                    "lock": lock,
                    "func": self.wtools.get_client_log_info,
                    "return": thread_return_dict,
                    'id': self.thread_id,
                    "message": "Client RF History",
                    "update": self.wtools.update_thread})
            client.start()
            # AP RF History thread
            aps = threading.Thread(target=thread_wrapper,
                    args=[self.bldg, self.floor, self.logdate], kwargs={
                    "lock": lock,
                    "func": self.wtools.get_ap_log_info,
                    "return": thread_return_dict,
                    'id': self.thread_id,
                    "message": "AP RF History",
                    "update": self.wtools.update_thread})
            aps.start()
            # Auth Logs thread
            auth = threading.Thread(target=thread_wrapper,
                    args=[self.mac, self.logdate, self.uid], kwargs={
                    "lock": lock,
                    "func": self.wtools.get_auth_logs,
                    "return": thread_return_dict,
                    'id': self.thread_id,
                    "message": "Authentication Logs",
                    "update": self.wtools.update_thread})
            auth.start()
            # DHCP Logs thread
            dhcp = threading.Thread(target=thread_wrapper,
                    args=[self.mac, self.logdate], kwargs={
                    "lock": lock,
                    "func": self.wtools.get_dhcp_logs,
                    "return": thread_return_dict,
                    'id': self.thread_id,
                    "message": "DHCP Logs",
                    "update": self.wtools.update_thread})
            dhcp.start()
            # Wait for all threads to finish
            client.join()
            aps.join()
            auth.join()
            dhcp.join()
            # Gets all output from threads
            client_dict = thread_return_dict[self.wtools.get_client_log_info]
            ap_dict = thread_return_dict[self.wtools.get_ap_log_info]
            auth_dict = thread_return_dict[self.wtools.get_auth_logs]
            dhcp_dict = thread_return_dict[self.wtools.get_dhcp_logs]
            # If any errors happened during each thread, bail out
            for thread_dict in [client_dict, ap_dict, auth_dict, dhcp_dict]:
                if isinstance(thread_dict, Exception):
                    raise thread_dict
            # Combining all the dicts into one final dict
            final_dict = {}
            for hour in range(0, 24):
                final_dict[hour] = {}
                final_dict[hour]["client"] = (client_dict[hour]
                        if client_dict[hour] else None)
                final_dict[hour]["aps"] = ap_dict[hour]
                final_dict[hour]["auth"] = auth_dict[hour]
                final_dict[hour]["dhcp"] = dhcp_dict[hour]
            self.wtools.update_thread(self.thread_id, True, False, "Complete",
                    final_dict)
        except Exception as e:
            logging.info('', exc_info=True)
            self.wtools.update_thread(self.thread_id, True, True, str(e))

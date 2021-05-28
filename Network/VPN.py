class CryptoMap:

    def __init__(self, concentrator_ip):
        self.object_local = None
        self.object_remote = None
        self.number = None
        self.insideips = []
        self.inside_network = []
        self.outsideip = None
        self.concentrator_ip = concentrator_ip

    def __str__(self):
        networks = ''
        if hasattr(self, "inside_network"):
            if isinstance(self.inside_network, set):
                for count, x in enumerate(self.inside_network):
                    if count == len(self.inside_network) - 1:
                        networks += f"{str(x)}\r\n"
                    else:
                        networks += f"{str(x)},"
            else:
                networks += f"{str(self.inside_network)}\r\n"
        ips = ''
        if hasattr(self, "insideips"):
            if isinstance(self.insideips, set):
                for count, x in enumerate(self.insideips):
                    if count == len(self.insideips) - 1:
                        ips += f"{str(x)}\r\n"
                    else:
                        ips += f"{str(x)},"
            else:
                ips += f"{str(self.insideips)}\r\n"

        string = f"----------------------------------------------------------\r\n" \
                 f"{self.object_remote if hasattr(self, 'object_remote') else ''}\r\n" \
                 f"{f'Concentrator: {self.concentrator_ip} to Inside Ip Addresses: {ips}' if hasattr(self, 'insideips') else ''}" \
                 f"{f'Concentrator: {self.concentrator_ip} to Inside Networks: {networks}' if hasattr(self, 'inside_network') else ''}" \
                 f"Public Ip address:{self.outsideip if hasattr(self, 'outsideip') else ''}\r\n"
        return string

class ASA(Router):
    def __init__(self, *args, **kwargs):
        self.snmp_host_group_wrong = False
        super(ASA, self).__init__(*args, **kwargs)

    def connect_to_ASA(self):
        """
        Figures out which ASA to log into, and creates a connection for that device
        Connection to device assigned to self.con
        """
        self.login()
        result = self.conn.send_command(f"sh run", manypages=True)
        result = result.split("\r\n")
        crypto_objs = []
        for line in result:
            if "access-list outside_cryptomap_" in line:
                c = CryptoMap(concentrator_ip=self.ip)
                line = re.sub("access-list outside_cryptomap_", "", line)
                c.number = line.split(' ')[0]
                line = ' '.join(line.split(' ')[1:])
                line = re.sub("extended permit ip any4 ", "", line)
                line = re.sub("extended permit ip ", "", line)
                line = re.sub("<--- More --->", "", line)
                if 'object-group' in line or 'object' in line:
                    object_groups = line.split('object-group')
                    object_groups = [x for x in object_groups if x]
                    object_groups = [x for x in object_groups if x != ' ']
                    if len(object_groups) == 1:
                        if 'host' in object_groups[0]:
                            object_groups_2 = object_groups[0].split('host')
                            object_local = [x for x in object_groups_2[0] if x]
                            object_local = [x for x in object_groups_2[0] if x != ' ']
                            object_local = ''.join(object_local)
                            c.object_local = object_local
                            object_remote = [x for x in object_groups_2[1] if x]
                            object_remote = [x for x in object_groups_2[1] if x != ' ']
                            c.insideips = ipaddress.IPv4Address(''.join(object_remote))
                        elif 'object' in object_groups[0]:
                            object_groups_2 = object_groups[0].split('object')
                            object_local = [x for x in object_groups_2[0] if x]
                            object_local = [x for x in object_groups_2[0] if x != ' ']
                            object_local = ''.join(object_local)
                            c.object_local = object_local
                            object_remote = [x for x in object_groups_2[1] if x]
                            object_remote = [x for x in object_groups_2[1] if x != ' ']
                            object_remote = ''.join(object_remote)
                            c.object_remote = object_remote
                        else:
                            object_remote = [x for x in object_groups[0] if x]
                            object_remote = [x for x in object_groups[0] if x != ' ']
                            object_remote = ''.join(object_remote)
                            c.object_remote = object_remote
                    elif len(object_groups) == 2:
                        object_local = [x for x in object_groups[0] if x]
                        object_local = [x for x in object_groups[0] if x != ' ']
                        object_local = ''.join(object_local)
                        c.object_local = object_local
                        object_remote = [x for x in object_groups[1] if x]
                        object_remote = [x for x in object_groups[1] if x != ' ']
                        object_remote = ''.join(object_remote)
                        c.object_remote = object_remote
                    crypto_objs.append(c)

        result = self.conn.send_command(f"show object-group", manypages=True)
        result = result.split("object-group network")
        for c in crypto_objs:
            for group in result:
                if group == '':
                    continue
                if hasattr(c, 'object_remote'):
                    if c.object_remote:
                        if c.object_remote in group:
                            lines = group.split("\r\n")
                            c.insideips = set()
                            c.inside_network = set()
                            for line in lines:
                                line = line.rstrip()
                                line = re.sub("\r", "", line)
                                if c.object_remote in line:
                                    continue
                                elif 'description' in line:
                                    continue
                                elif 'host' in line:
                                    ip = re.sub("network-object host ", "", line)
                                    ip = re.sub(" ", "", ip)
                                    ip = [x for x in ip if x]
                                    ip = [x for x in ip if x != ' ']
                                    ip = ''.join(ip)
                                    ip = ipaddress.IPv4Address(ip)
                                    c.insideips.add(ip)
                                    continue
                                else:
                                    line = re.sub("network-object ", "", line)
                                    if 'object' in line:
                                        continue
                                    line = line.split(' ')
                                    line = [x for x in line if x]
                                    line = [x for x in line if x != ' ']
                                    if len(line) == 2:
                                        ip = line[0]
                                        ip = re.sub(" ", "", ip)
                                        ip = [x for x in ip if x]
                                        ip = [x for x in ip if x != ' ']
                                        ip = ''.join(ip)
                                        subnet = line[1]
                                        subnet = re.sub(" ", "", subnet)
                                        subnet = [x for x in subnet if x]
                                        subnet = [x for x in subnet if x != ' ']
                                        subnet = ''.join(subnet)
                                        network = ipaddress.IPv4Network(f"{ip}/{subnet}")
                                        c.inside_network.add(network)
                                        continue
                                    else:
                                        pass
        if self.ip == '155.98.175.84':
            result = self.conn.send_command(f"show run crypto map", manypages=True)
        else:
            result = self.conn.send_command(f"show run | in CryptoMap map outside_map0", manypages=True)
        result = result.split("\r\n")
        crypto_numbers = set()
        for group in result:
            if group == '':
                continue
            number = re.sub("crypto map vpn ", "", group)
            number = re.sub('crypto map inside_map ', "", number)
            number = re.sub("CryptoMap map outside_map0 ", "", number)
            number = re.sub("\r", "", number)
            number = number.rstrip("\r")
            number = number.split(" ")
            number = [x for x in number if x]
            number = [x for x in number if x != ' '][0]
            if number == 'interface':
                continue
            crypto_numbers.add(int(number))

        grouped_crypto_lines = []
        for num in crypto_numbers:
            Crypto_group = []
            for group in result:
                number = re.sub("crypto map vpn ", "", group)
                number = re.sub('crypto map inside_map ', "", number)
                number = re.sub("CryptoMap map outside_map0 ", "", number)
                number = re.sub("\r", "", number)
                number = number.rstrip("\r")
                number = number.split(" ")
                number = [x for x in number if x]
                number = [x for x in number if x != ' '][0]
                if number == 'interface':
                    continue
                if int(number) == num:
                    Crypto_group.append(group)
            lines = '\r\n'.join(Crypto_group)
            grouped_crypto_lines.append(lines)

        crypto_dict = {}
        for lines in grouped_crypto_lines:
            line = lines.split("\r\n")
            for l in line:
                if "match address outside_cryptomap_" in l:
                    number = re.sub("match address outside_cryptomap_", "", l)
                    number = re.sub("\r", "", number)
                    number = number.rstrip("\r")
                    number = number.split(" ")
                    number = [x for x in number if x]
                    number = [x for x in number if x != ' ']
                    number = number[len(number) - 1]
                    crypto_dict[number] = lines

        for c in crypto_objs:
            for key, lines in crypto_dict.items():
                if c.number == key:
                    line = lines.split("\r\n")
                    for l in line:
                        if 'peer' in l:
                            ip = re.sub(f"set peer ", "", l)
                            ip = re.sub("crypto map vpn ", "", ip)
                            ip = re.sub("CryptoMap map outside_map0 ", "", ip)
                            ip = re.sub("\r", "", ip)
                            ip = ip.rstrip("\r")
                            ip = ip.split(" ")
                            ip = [x for x in ip if x]
                            ip = [x for x in ip if x != ' '][1]
                            ip = ipaddress.IPv4Address(ip)
                            c.outsideip = ip

        for c in crypto_objs:
            print(c)

    def check_SNMP(self):
        """
        Takes the SNMP Information stored in self.SNMP, and checks it against our standards
        """
        logger.info(f"Checking SNMP ({self.IPAddress}) - Starting ")
        try:
            if self.SNMP.groups: # check SNMP groups
                if self.SNMP.groups[0].line != 'orionvpn v3 priv ':
                    self.snmp_group_wrong = True
            if self.SNMP.loggingips: #checking SNMP logging
                for log in self.SNMP.loggingips:
                    if str(log) not in settings.standard_log_ips:
                        self.snmp_logging_wrong = True
            if self.SNMP.user: # check user info
                if self.SNMP.user.name != 'Orion':
                    self.snmp_user_wrong = True
            if self.SNMP.host_group: # check host_group info
                if (self.SNMP.host_group.user != 'Orion' or self.SNMP.host_group.interface != 'inside' or
                    self.SNMP.host_group.network_object !=  'Orion_Monitoring'):
                    self.snmp_host_group_wrong = True
        except Exception as e:
            logger.info(f"Checking SNMP ({self.IPAddress}) - Failed ")
            logger.error(e, exc_info=True)
            _exception(e)
            raise
        else:
            logger.info(f"Checking SNMP ({self.IPAddress}) - Success ")
    def check_SNMP_v2(self):
        """
        Checks the SNMP object for Version 2 standards
        """
        logger.info(f"Checking SNMP v2 ({self.IPAddress}) - Starting")
        try:
            standard_ro = False
            standard_rw = False
            snmp_communities = []
            for s in self.SNMP.communities:
                if (s.string == settings.SNMP_V2.standard_ro and
                        SNMP_community.accesslist == '70'):  # Check for the Standard RO SNMP V2
                    metrics_logger.info(f"SNMP v2 Standard RO ({self.IPAddress}) - Present")
                    standard_ro = True
                    snmp_communities.append(s)
                elif (s.string == settings.SNMP_V2.standard_rw and
                      SNMP_community.accesslist == '71'):  # Check for the Standard RO SNMP V2
                    metrics_logger.info(f"SNMP v2 Standard RW ({self.IPAddress}) - Present")
                    standard_rw = True
                    snmp_communities.append(s)
                else:
                    metrics_logger.info(f'SNMP Community: {s.string} {"RO" if s.ro else ""} '
                                        f'{"RW" if s.rw else ""} {s.accesslist} ({self.IPAddress}) - Removing')

            if not standard_ro:
                metrics_logger.info(f"SNMP v2 Standard RO ({self.IPAddress}) - Missing")
            if not standard_rw:
                metrics_logger.info(f"SNMP v2 Standard RW ({self.IPAddress}) - Missing")

        except Exception as e:
            logger.info(f"Checking SNMP v2 ({self.IPAddress}) - Failed ")
            logger.error(e, exc_info=True)
        else:
            logger.info(f"Checking SNMP v2 ({self.IPAddress}) - Success ")
            self.SNMP.communities = snmp_communities

    def check_SNMP_v3(self):
        """
        Checks the SNMP object for Version 3 standards
        """
        logger.info(f"Checking SNMP v3 ({self.IPAddress}) - Starting")
        try:
            snmp_groups = []
            # remove SNMP Groups outside of accepted
            logger.debug(f"SNMP Groups {self.SNMP.groups}")
            for snmp_group in self.SNMP.groups:
                if snmp_group.acl.number not in settings.permitted_SNMP_Groups:
                    snmp_group.remove = True
                    logger.debug(f"SNMP Group ({snmp_group}) - Not Needed")
                else:
                    snmp_groups.append(snmp_group)
            self.SNMP.groups = snmp_groups

            # remove SNMP Views outside of what is needed
            snmp_views = []
            # remove SNMP Groups outside of accepted
            logger.debug(f"SNMP Views {self.SNMP.views}")
            for snmp_view in self.SNMP.views:
                if snmp_view.name not in settings.permitted_SNMP_views:
                    snmp_view.remove = True
                    logger.debug(f"SNMP view ({snmp_view}) - Not Needed")
                else:
                    snmp_views.append(snmp_view)
            self.SNMP.views = snmp_views

            acl71auth = False
            acl70auth = False
            acl71priv = False
            acl70priv = False
            acl76priv = False
            RWview = False
            ROview = False
            PFview = False
            if self.SNMP.context:
                metrics_logger.info(f"SNMP Context Line ({self.IPAddress}) - Present")
            else:
                metrics_logger.info(f"SNMP Context Line ({self.IPAddress}) - Missing")
            if self.SNMP.contextPFG:
                metrics_logger.info(f"SNMP PFG Context Line ({self.IPAddress}) - Present")
            else:
                metrics_logger.info(f"SNMP PFG Context Line ({self.IPAddress}) - Missing")
            for group in self.SNMP.groups:
                if 'NOCViewRO' in group.viewname:
                    ROview = True
                if 'NOCViewRW' in group.viewname:
                    RWview = True
                if 'PFViewRO' in group.viewname:
                    PFview = True
                if group.acl.number == '76':
                    if group.securitylevel == 'priv':
                        acl76priv = group
                        metrics_logger.info(f"ACL 76 priv ({self.IPAddress}) - Present")
                if group.acl.number == '70':
                    if group.securitylevel == 'auth':
                        acl70auth = group
                        metrics_logger.info(f"ACL 70 auth ({self.IPAddress}) - Present")
                    if group.securitylevel == 'priv':
                        acl70priv = group
                        metrics_logger.info(f"ACL 70 priv ({self.IPAddress}) - Present")
                if group.acl.number == '71':
                    if group.securitylevel == 'auth':
                        acl71auth = group
                        metrics_logger.info(f"ACL 71 auth ({self.IPAddress}) - Present")
                    if group.securitylevel == 'priv':
                        acl71priv = group
                        metrics_logger.info(f"ACL 71 priv ({self.IPAddress}) - Present")

            grouplist = []
            # check the accuracy of every line
            if acl71auth:
                if acl71auth.RW and acl71auth.name == 'NOCGrv3RW' and acl71auth.viewname == 'NOCViewRW':
                    metrics_logger.info(f"ACL 71 auth ({self.IPAddress}) - Corrrect")
                    acl71auth.correct = True
                    grouplist.append(acl71auth)
                else:
                    metrics_logger.info(f"ACL 71 auth ({self.IPAddress}) - Incorrect")
                    grouplist.append(acl71auth)
            else:
                metrics_logger.info(f"ACL 71 auth ({self.IPAddress}) - Missing")

            if acl70auth:
                if acl70auth.RO and acl70auth.name == 'NOCGrv3RO' and acl70auth.viewname == 'NOCViewRO':
                    metrics_logger.info(f"ACL 70 auth ({self.IPAddress}) - Corrrect")
                    acl70auth.correct = True
                    grouplist.append(acl70auth)
                else:
                    metrics_logger.info(f"ACL 70 auth ({self.IPAddress}) - Incorrect")
                    grouplist.append(acl70auth)
            else:
                metrics_logger.info(f"ACL 70 auth ({self.IPAddress}) - Missing")

            if acl71priv:
                if acl71priv.RW and acl71priv.name == 'NOCGrv3RW' and acl71priv.viewname == 'NOCViewRW':
                    metrics_logger.info(f"ACL 71 priv ({self.IPAddress}) - Corrrect")
                    acl71priv.correct = True
                    grouplist.append(acl71priv)
                else:
                    metrics_logger.info(f"ACL 71 priv ({self.IPAddress}) - Incorrect")
                    grouplist.append(acl71priv)
            else:
                metrics_logger.info(f"ACL 71 priv ({self.IPAddress}) - Missing")

            if acl70priv:
                if acl70priv.RO and acl70priv.name == 'NOCGrv3RO' and acl70priv.viewname == 'NOCViewRO':
                    metrics_logger.info(f"ACL 70 ({self.IPAddress}) - Corrrect")
                    acl70priv.correct = True
                    grouplist.append(acl70priv)
                else:
                    metrics_logger.info(f"ACL 70 ({self.IPAddress}) - Incorrect")
                    grouplist.append(acl70priv)
            else:
                metrics_logger.info(f"ACL 70 ({self.IPAddress}) - Missing")

            if acl76priv:
                if acl76priv.RO and acl76priv.name == 'PFGrv3RO' and acl76priv.viewname == 'PFViewRO':
                    metrics_logger.info(f"ACL 76 priv ({self.IPAddress}) - Corrrect")
                    acl76priv.correct = True
                    grouplist.append(acl76priv)
                else:
                    metrics_logger.info(f"ACL 76 priv ({self.IPAddress}) - Incorrect")
                    grouplist.append(acl76priv)
            else:
                metrics_logger.info(f"ACL 76 priv ({self.IPAddress}) - Missing")

            # checking SNMP Views
            ROviewline = False
            RWviewline = False
            PFviewline = False
            for snmp_view in self.SNMP.views:
                if RWview:
                    if snmp_view.name == 'NOCViewRW':
                        metrics_logger.info(f"SNMP RWView ({self.IPAddress}) - Present")
                        RWviewline = snmp_view
                if ROview:
                    if snmp_view.name == 'NOCViewRO':
                        metrics_logger.info(f"SNMP ROView ({self.IPAddress}) - Present")
                        ROviewline = snmp_view
                if PFview:
                    if snmp_view.name == 'PFViewRO':
                        metrics_logger.info(f"SNMP PFView ({self.IPAddress}) - Present")
                        PFviewline = snmp_view

            viewlist = []

            if ROviewline:
                if ROviewline.included and ROviewline.mibfamily == 'internet':
                    metrics_logger.info(f"SNMP ROView ({self.IPAddress}) - Correct")
                    ROviewline.correct = True
                    viewlist.append(ROviewline)
                else:
                    metrics_logger.info(f"SNMP ROView ({self.IPAddress}) - Incorrect")
                    viewlist.append(ROviewline)
            else:
                metrics_logger.info(f"SNMP ROView ({self.IPAddress}) - Missing")

            if RWviewline:
                if RWviewline.included and RWviewline.mibfamily == 'internet':
                    metrics_logger.info(f"SNMP RWView ({self.IPAddress}) - Correct")
                    RWviewline.correct = True
                    viewlist.append(RWviewline)
                else:
                    metrics_logger.info(f"SNMP RWView ({self.IPAddress}) - Incorrect")
                    viewlist.append(RWviewline)
            else:
                metrics_logger.info(f"SNMP RWView ({self.IPAddress}) - Missing")

            if PFviewline:
                if PFviewline.included and PFviewline.mibfamily == 'internet':
                    metrics_logger.info(f"SNMP PFView ({self.IPAddress}) - Correct")
                    PFviewline.correct = True
                    viewlist.append(PFviewline)
                else:
                    metrics_logger.info(f"SNMP PFView ({self.IPAddress}) - Incorrect")
                    viewlist.append(PFviewline)
            else:
                metrics_logger.info(f"SNMP PFView ({self.IPAddress}) - Missing")

        except Exception as e:
            logger.info(f"Checking SNMP v3 ({self.IPAddress}) - Failed ")
            logger.error(e, exc_info=True)
        else:
            logger.info(f"Checking SNMP v3 ({self.IPAddress}) - Success ")
            self.SNMP.groups = grouplist
            self.SNMP.views = viewlist

    def assignattributes(self, con=None):
        """
        takes the responses from get switch info, and applies those responses to the object attributes

        """
        logger.info(f"Assigning Data to Router Object - Starting")
        try:
            self.sortVersion(versionresult=self.version_result)
            self.sort_acl()
            self.sort_object_groups()
            self.sortsnmp()

        except Exception as e:
            logger.info(f"Assigning Data to Router Object - Failed")
            logger.error(e, exc_info=True)
            _exception(e)
            raise
        else:
            logger.info(f"Assigning Data to Router Object - Success")

    def getSwitchInfo(self):
        """
        Gathers all the essential information from the switch, and creates a switch object based off the
        results for better use in python coding projects
        Args:
            con (Connection): an active Parimko Connection to a switch

        """
        logger.info(f"Scraping Router Data - Starting")
        try:
            self.conn.enable_cisco(password=Switch_access.password)
            self.hostname = re.sub("hostname", "", self.conn.send_command('show run | inc hostname', manypages=True))
            self.hostname = re.sub(" ", "", self.hostname)
            self.hostname = self.hostname.rstrip("\r")
            self.version_result = self.conn.send_command('show version', manypages=True)
            self.acl_result = self.conn.send_command('show access-list',manypages=True)
            self.object_results = self.conn.send_command('show run object',manypages=True)
            self.snmp_result = self.conn.send_command('show run snmp-server', manypages=True)

        except Exception as e:
            logger.info(f"Scraping Router Data - Failed")
            logger.error(e, exc_info=True)
        else:
            logger.info(f"Scraping Router Data - Success")

    def sortVersion(self, versionresult):
        """
        This functions pulls out the Stack information, Version number, Model Number, Serial number,
        and switch uptime for the 'show version' response
        Args:
            versionresult (str): A response from running 'show version' on a switch
        """
        assert isinstance(versionresult, str), f'versionresult: must be str, but got {type(versionresult)}'
        logger.info("Sorting 'show Version' - Starting")
        try:
            # run code here
            # search through response to gather the indivigual info
            ver = versionresult.split('\r\n')

            for count, line in enumerate(ver):
                if line == '':
                    continue
                # discover if there is more than one blade in this stack by counting serial numbers
                if 'Serial Number: ' in line or 'System serial number' in line or 'Processor board ID' in line:
                    line = re.sub('System Serial Number', '', line)
                    line = re.sub('System serial number', '', line)
                    line = re.sub('Processor board ID', '', line)
                    line = re.sub('Serial Number: ', '', line)
                    line = re.sub(':', '', line)
                    line = re.sub(' ', '', line)
                    self.serial = line
                elif 'Device Manager Version' in line:
                    self.version = re.sub('Device Manager Version ','',line)
                elif 'Hardware: ' in line:
                    self.modelnumber = re.sub('Hardware: ','',line)
                    self.modelnumber = self.modelnumber.split(',')[0]
                    self.modelnumber = re.sub(' ', '', self.modelnumber)
                    pass

        except Exception as e:
            logger.info("Sorting 'show Version' - failed")
            logger.error(e, exc_info=True)
            _exception(e)
            raise
        else:
            logger.info("Sorting 'show Version' - Success")
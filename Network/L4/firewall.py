from Services.SSH.ParamikoConnection import Connection


class PaloAlto():
    def __init__(self,ip,pano=None):
        """

        @param ip:
        @type ip: str
        @param pano:
        @type pano: bool
        """
        self.ip = ip
        self.pano = pano
        self.conn = None

    def __enter__(self):
        self.conn = Connection(self.ip)
        self.conn.login()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.logout()
    def SendConfigCommands(self, commands):
        """

        @param commands:
        @type commands: list
        @return:
        @rtype: list
        """
        results = []
        results.append((self.conn.send_command("config t"), "config t"))
        for command in commands:
            results.append((self.conn.send_command(command), command))
        results.append((self.conn.send_command("save config"), "save config"))
        results.append((self.conn.send_command("commit"), "commit"))
        return results

class adddressobj():
    def __init__(self,address_name, address,pano):
        """

        @param address_name:
        @type address_name: str
        @param address:
        @type address: str
        @param pano:
        @type pano: bool
        """
        self.address_name = address_name
        self.address = address
        self.pano = pano
    def __str__(self):
        return str(self.address_name)
    def Create(self):
        """

        @return:
        @rtype: list
        """
        clicomands = []
        if self.pano:
            clicomands.append(f"set shared address {self.address_name} ip-netmask {self.address}")
        else:
            clicomands.append(f"set address {self.address_name} ip-netmask {self.address}")
        return clicomands

    def Delete(self):
        """

        @return:
        @rtype: list
        """
        clicomands = []
        if self.pano:
            clicomands.append(f"delete shared address {self.address_name} ip-netmask")
        else:
            clicomands.append(f"delete address {self.address_name} ip-netmask")
        return clicomands

class GroupObj():
    def __init__(self,group_name,pano):
        """

        @param group_name:
        @type group_name: str
        @param pano:
        @type pano: bool
        """
        self.group_name = group_name
        self.pano = pano
    def __str__(self):
        return str(self.group_name)
    def Create(self):
        """

        @return:
        @rtype: list
        """
        clicomands = []
        if self.pano:
            clicomands.append(f"set shared address-group {self.group_name}")
        else:
            clicomands.append(f"set address - group {self.group_name}")
        return clicomands

    def AddAddressObj(self, address_name):
        """

         @return:
         @rtype: list
         """
        clicomands = []
        if self.pano:
            clicomands.append(f"set shared address-group {self.group_name} static {address_name}")
        else:
            clicomands.append(f"set address-group {self.group_name} static {address_name}")
        return clicomands

    def Delete(self):
        """

         @return:
         @rtype: list
         """
        clicomands = []
        if self.pano:
            clicomands.append(f"delete shared address-group {self.group_name}")
        else:
            clicomands.append(f"delete address - group {self.group_name}")
        return clicomands

    def RemoveAddressObj(self, address_name):
        """

         @return:
         @rtype: list
         """
        clicomands = []
        if self.pano:
            clicomands.append(f"delete shared address-group {self.group_name} static {address_name}")
        else:
            clicomands.append(f"delete address-group {self.group_name} static {address_name}")
        return clicomands
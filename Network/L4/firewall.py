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
        return results
    def Commit(self):
        results = []
        results.append((self.conn.send_command("save config"), "save config"))
        return results
    def Save(self):
        results = []
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

class Interface():
    def __init__(self,interfacename,pano,template=None,interfacenumber=None):
        """

        @param interfacename:
        @type interfacename: str
        @param pano:
        @type pano: bool
        """
        self.interfacename = interfacename
        self.pano = pano
        self.template = template
        self.interfacenumber = interfacenumber
    def __str__(self):
        return str(self.interfacename)
    def Create(self,ipaddress,tag,comment=None,VRtoAddTo=None,AddtoSZ=None,Vsys=None,zone=None):
        """

        @return:
        @rtype: list
        """
        clicomands = []
        basecommand = f"network interface aggregate-ethernet {self.interfacename} layer3 units {self.interfacename}.{self.interfacenumber} tag {self.interfacenumber}"
        L3command = f"{basecommand} comment {comment} ip {str(ipaddress)}"
        if self.pano:
            clicomands.append(f"set template {self.template} config {basecommand}")
            clicomands.append(f"set template {self.template} config {L3command}")
            if VRtoAddTo:
                clicomands.append(f"set template {self.template} config network virtual-router {VRtoAddTo} interface {self.interfacename}.{self.interfacenumber}")
            if AddtoSZ:
                clicomands.append(
                    f"set template {self.template} config vsys {Vsys} import network interface {self.interfacename}.{self.interfacenumber}")
                clicomands.append(
                    f"set template {self.template} config vsys {Vsys} zone {zone} network layer3 {self.interfacename}.{self.interfacenumber}")
        else:
            clicomands.append(f"set {basecommand}")
            clicomands.append(f"set {L3command}")
            if VRtoAddTo:
                clicomands.append(f"set network virtual-router {VRtoAddTo} interface {self.interfacename}.{self.interfacenumber}")
            if AddtoSZ:
                clicomands.append(
                    f" set zone {zone} network layer3 {self.interfacename}.{self.interfacenumber}")

        return clicomands

    def Delete(self):
        """

         @return:
         @rtype: list
         """
        clicomands = []
        basecommand = f"network interface aggregate-ethernet {self.interfacename} layer3 units {self.interfacename}.{self.interfacenumber}"
        if self.pano:
            clicomands.append(f"delete template {self.template} config {basecommand}")
        else:
            clicomands.append(f"delete {basecommand}")
        return clicomands

class Zone():
    def __init__(self,zone_name,pano,vsys=None,template=None):
        """

        @param zone_name:
        @type zone_name: str
        @param pano:
        @type pano: bool
        """
        self.zone_name = zone_name
        self.pano = pano
        if pano:
            if not vsys or not template:
                print("needs Vsys and template names to be able to configure panorama")
            self.vsys = vsys
            self.template = template
    def __str__(self):
        return str(self.zone_name)
    def Create(self):
        """

        @return:
        @rtype: list
        """
        clicomands = []
        if self.pano:
            clicomands.append(f"set template {self.template} config vsys {self.vsys} zone {self.zone_name}")
        else:
            clicomands.append(f"set zone {self.zone_name}")
        return clicomands

    def AddInterfaceToZone(self, Interface):
        """
         @return:
         @rtype: list
         """
        clicomands = []
        if self.pano:
            clicomands.append(f"set shared address-group {self.zone_name} static {address_name}")
        else:
            clicomands.append(f"set address-group {self.zone_name} static {address_name}")
        return clicomands

    def Delete(self):
        """

         @return:
         @rtype: list
         """
        clicomands = []
        if self.pano:
            clicomands.append(f"delete shared address-group {self.zone_name}")
        else:
            clicomands.append(f"delete address - group {self.zone_name}")
        return clicomands
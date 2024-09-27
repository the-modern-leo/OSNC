from Services.SSH.ParamikoConnection import Connection

class PaloAlto():
    def __int__(self):
        pass

    def SendCommand(self,Command):
        conn = Connection()
        conn.login("10.7.17.132")
        result = conn.send_command(Command)
        conn.logout()
        return result
    def CreateAddressObj(self,AddressName,Address):
        cliComannd = f"set shared address {AddressName} ip - netmask {Address}"

    def CreateGroupObj(self,GroupName):
        cliComannd = f"set shared address - group {GroupName}"

    def AssocateAddressToGroupObj(self,GroupName,AddressName):
        cliComannd = f"set shared address - group {GroupName} static {AddressName}"
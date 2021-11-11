import uuid

class SNMP:
    """
    For looking through the SNMP portion of a device
    """

    def __init__(self):
        self.ifmib = None
        self.version = set()
        self.location_bldg = None
        self.location_rm = None
        self.contacts = []
        self.groups = []
        self.views = []
        self.context = False
        self.contextPFG = False
        self.locationcorrect = False
        self.traps = []
        self.trapscorrect = False
        self.loggingcorrect = False
        self.loggingips = []
        self.communities = []
        self.user = []

class SNMP_User:
    """
    E.X 'snmp-server group v3 auth read access 70'
    """

    def __init__(self):
        self.name = None
        self.Auth_proto = None
        self.priv_proto = None
        self.group = None
        self.remove = False


    def __repr__(self):
        return f"{self.name} {self.securitylevel}"

    def __str__(self):
        return f"{self.name} {self.securitylevel}"

class SNMP_Host_Group:
    """
    E.X 'snmp-server group v3 auth read access 70'
    """

    def __init__(self):
        self.interface = None
        self.network_object = None
        self.polling = None
        self.user = None

class SNMP_Group:
    """
    E.X 'snmp-server group v3 auth read access 70'
    """

    def __init__(self):
        self.acl = None
        self.RO = False
        self.RW = False
        self.securitylevel = None
        self.name = None
        self.version = None
        self.viewname = None
        self.correct = False
        self.remove = False
        self.line = None
        self.hash = uuid.uuid4()

    def __repr__(self):
        return f"{self.name} {self.securitylevel}"

    def __str__(self):
        return f"{self.name} {self.securitylevel}"

class SNMP_view:
    def __init__(self):
        self.name = None
        self.mibfamily = None
        self.included = False
        self.excluded = False
        self.correct = False
        self.remove = False

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

class SNMP_contact:
    def __init__(self):
        self.bc = None
        self.tag = None
        self.serial = None

class SNMP_community():
    def __init__(self):
        self.string = None
        self.rw = False
        self.ro = False
        self.accesslist = None
        self.raw_data = None

    def __repr__(self):
        return f"{self.string} {self.ro if self.ro else ''} {self.rw if self.rw else ''} {self.accesslist}"

    def __str__(self):
        return f"{self.string} {self.ro if self.ro else ''} {self.rw if self.rw else ''} {self.accesslist}"

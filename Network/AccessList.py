class ACL_Entry:
    def __init__(self):
        self.destination_wildcard = None
        self.destination_port = None
        self.permit = None
        self.number = None
        self.matche_count = 0
        self.protocol = None
        self.typeofprotocol = None
        self.raw_data = None
        self.source = None
        self.source_wildcard = None
        self.destination = None
        self.match = None
        self.hash = uuid.uuid4()

    def __repr__(self):
        return self.raw_data

    def __str__(self):
        return self.raw_data

    def __hash__(self):
        return hash((self.hash))

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented
        return self.source == other.source and self.number == other.number

class Access_Lists:
    """
    For looking at the Access lists on a switch
    """

    def __init__(self):
        self.numbers = set()
        self.names = set()
        self.standard_ip_lists = []
        self.extended_ip_lists = []
        self.ipv6_lists = []
        self.extended_mac_lists = []

    def __len__(self):
        length = int(len(self.standard_ip_lists) + len(self.extended_ip_lists) + len(self.ipv6_lists) + len(
            self.extended_mac_lists))
        return length

class ACL:
    """
    For looking at the Access lists on a switch
    """

    def __init__(self):
        self.number = None
        self.Entries = []
        self.type = None
        self.raw_data = None
        self.name = None

    def __len__(self):
        return len(self.Entries)

    def __repr__(self):
        if self.number:
            return self.number
        if self.name:
            return self.name

    def __str__(self):
        return self.raw_data
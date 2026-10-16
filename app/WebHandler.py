from tornado.web import RequestHandler,Application,url
from tornado.template import Loader
import ipaddress

class MainHandler(RequestHandler):
    def get(self):
        self.render("MainPage.html", title="NetRunner")
class VlanHandler(RequestHandler):
    def get(self):
        items = ["1", "2", "3"]
        self.render("VlanHomePage.html", title="Vlans",items=items)
# Master pool of every known subnet in the mock network. Nested subnets are
# included so the drill-down "subnets within this range" feature has data
# to display for demonstration purposes.
IPAM_MASTER_ITEMS = [
    {"ip": "10.0.0.0/16", "comments": "Corporate Backbone", "location": "Arasaka Tower", "svi": "VLAN-000-CORE", "is_container": True},
    {"ip": "10.0.1.0/24", "comments": "Production Cluster A", "location": "Arasaka Tower", "svi": "VLAN-100-CORE", "is_container": True},
    {"ip": "10.0.1.0/25", "comments": "Production Cluster A - Segment 1", "location": "Arasaka Tower", "svi": "VLAN-100-CORE", "is_container": False},
    {"ip": "10.0.1.128/25", "comments": "Production Cluster A - Segment 2", "location": "Arasaka Tower", "svi": "VLAN-100-CORE", "is_container": False},
    {"ip": "192.168.50.0/24", "comments": "Management Subnet", "location": "Night City Datacenter", "svi": "VLAN-200-MGMT", "is_container": False},
    {"ip": "172.16.0.0/16", "comments": "Guest Access Layer", "location": "Watson District", "svi": "VLAN-300-PROD", "is_container": True},
    {"ip": "172.16.1.0/24", "comments": "Guest Access - Zone 1", "location": "Watson District", "svi": "VLAN-300-PROD", "is_container": False},
    {"ip": "172.16.2.0/24", "comments": "Guest Access - Zone 2", "location": "Watson District", "svi": "VLAN-300-PROD", "is_container": False},
    {"ip": "10.10.10.0/30", "comments": "P2P Link to Badlands", "location": "Badlands Hub", "svi": "VLAN-400-SVI", "is_container": False},
    {"ip": "10.255.0.1/32", "comments": "Loopback Interconnect", "location": "Westbrook Node", "svi": "VLAN-100-CORE", "is_container": False}
]

PHYSICAL_LOCATIONS = ["Night City Datacenter", "Badlands Hub", "Watson District", "Westbrook Node", "Arasaka Tower"]
SVI_LOCATIONS = ["VLAN-100-CORE", "VLAN-200-MGMT", "VLAN-300-PROD", "VLAN-400-SVI"]
SUBNET_TYPES = ["DATA", "VOIP", "VIDEO", "MANAGEMENT", "SECURITY"]

class IPAMDetailsHandler(RequestHandler):
    def get(self, network, prefix):
        parent_network = f"{network}/{prefix}"
        parent_item = None
        is_ip_view = False
        items = []

        try:
            parent_net = ipaddress.ip_network(parent_network, strict=False)
        except ValueError:
            parent_net = None

        if parent_net is not None:
            # Check if this specific network is a leaf subnet
            parent_item = next((i for i in IPAM_MASTER_ITEMS if i["ip"] == parent_network), None)
            
            if parent_item and not parent_item.get('is_container', False):
                is_ip_view = True
                # Populate with all IPs in the subnet
                for ip in parent_net:
                    ip_str = str(ip)
                    # Thematic mock comments
                    if ip_str == str(parent_net.network_address):
                        comment = "NETWORK_IDENTIFIER"
                    elif ip_str == str(parent_net.broadcast_address):
                        comment = "BROADCAST_SECTOR"
                    elif ip_str.endswith('.1'):
                        comment = "DEFAULT_GATEWAY"
                    else:
                        comment = "ACTIVE_NODE" if int(ip_str.split('.')[-1]) % 7 == 0 else "UNALLOCATED_SLOT"
                    
                    items.append({"ip": ip_str, "comments": comment})
            else:
                # Drill-down into nested subnets
                for item in IPAM_MASTER_ITEMS:
                    try:
                        candidate_net = ipaddress.ip_network(item["ip"], strict=False)
                    except ValueError:
                        continue
                    if candidate_net == parent_net:
                        continue
                    if candidate_net.subnet_of(parent_net):
                        items.append(item)

        self.render("IPAMHomePage.html", title="IPAM", items=items,
                    physical_locations=PHYSICAL_LOCATIONS,
                    svi_locations=SVI_LOCATIONS,
                    subnet_types=SUBNET_TYPES,
                    parent_network=parent_network,
                    parent_item=parent_item,
                    is_ip_view=is_ip_view)

class IPAMHandler(RequestHandler):
    def get(self):
        self.render("IPAMHomePage.html", title="IPAM", items=IPAM_MASTER_ITEMS,
                    physical_locations=PHYSICAL_LOCATIONS,
                    svi_locations=SVI_LOCATIONS,
                    subnet_types=SUBNET_TYPES,
                    parent_network=None,
                    parent_item=None,
                    is_ip_view=False)

    def post(self):
        # Extract fields from the request
        network_container = self.get_argument("network_container", "off")
        ip_address = self.get_argument("ip_address", "")
        comments = self.get_argument("comments", "")
        physical_location = self.get_argument("physical_location", "N/A")
        svi_location = self.get_argument("svi_location", "N/A")
        subnet_type = self.get_argument("subnet_type", "N/A")
        prefix_size = self.get_argument("prefix_size", "24")
        default_gateway = self.get_argument("default_gateway", "N/A")
        
        # Derived network fields from frontend
        network_address = self.get_argument("network_address", "N/A")
        subnet_mask = self.get_argument("subnet_mask", "N/A")
        wildcard_mask = self.get_argument("wildcard_mask", "N/A")
        ip_class = self.get_argument("ip_class", "N/A")
        in_addr_arpa = self.get_argument("in_addr_arpa", "N/A")
        ipv4_mapped = self.get_argument("ipv4_mapped", "N/A")
        six_to_four_prefix = self.get_argument("six_to_four_prefix", "N/A")

        # Validate that the provided IP address is well-formed
        try:
            ipaddress.ip_address(ip_address)
        except ValueError:
            self.set_status(400)
            self.write({
                "status": "error",
                "message": "VALIDATION FAILED: INVALID IP ADDRESS FORMAT DETECTED"
            })
            return

        # Simulate processing - log to console with Cyberpunk flavor
        print("-" * 40)
        print(">> INCOMING CONNECTION: IPAM_ADD_SERVICE")
        print(f">> DATA PACKET RECEIVED:")
        print(f"   - TARGET IP: {ip_address}/{prefix_size}")
        print(f"   - NET ADDRESS: {network_address}")
        print(f"   - SUBNET MASK: {subnet_mask}")
        print(f"   - WILDCARD: {wildcard_mask}")
        print(f"   - IP CLASS: {ip_class}")
        print(f"   - CONTAINER MODE: {network_container.upper()}")
        print(f"   - DEFAULT GATEWAY: {default_gateway}")
        print(f"   - PHYSICAL LOC: {physical_location}")
        print(f"   - VIRTUAL LOC: {svi_location}")
        print(f"   - CLASS: {subnet_type}")
        print(f"   - IN-ADDR.ARPA: {in_addr_arpa}")
        print(f"   - IPV4 MAPPED: {ipv4_mapped}")
        print(f"   - 6TO4 PREFIX: {six_to_four_prefix}")
        print(f"   - ENCRYPTION NOTES: {comments if comments else 'NONE'}")
        print(">> STATUS: SYNCING WITH ARASAKA MAINFRAME...")
        print(">> RESULT: NODE INITIALIZED SUCCESSFULLY")
        print("-" * 40)

        # Return JSON response to the AJAX caller
        self.write({
            "status": "success",
            "message": "SYSTEM NOTIFICATION: NEW NODE DETECTED AND REGISTERED",
            "ip_registered": f"{ip_address}/{prefix_size}"
        })

app = Application([
    url(r"/", MainHandler),
    url(r"/Vlans", VlanHandler, name="Vlans"),
    url(r"/IPAM/([\d\.]+)/(\d{1,2})", IPAMDetailsHandler, name="IPAMDetails"),
    url(r"/IPAM", IPAMHandler, name="IPAM"),
    ],autoreload=True,debug=True)
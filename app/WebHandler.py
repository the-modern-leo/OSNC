from tornado.web import RequestHandler,Application,url
from tornado.template import Loader

class MainHandler(RequestHandler):
    def get(self):
        self.render("MainPage.html", title="NetRunner")
class VlanHandler(RequestHandler):
    def get(self):
        items = ["1", "2", "3"]
        self.render("VlanHomePage.html", title="Vlans",items=items)
class IPAMHandler(RequestHandler):
    def get(self):
        # Sample data for the table
        items = [
            {"ip": "10.0.1.0/24", "comments": "Production Cluster A", "location": "Arasaka Tower", "svi": "VLAN-100-CORE"},
            {"ip": "192.168.50.0/24", "comments": "Management Subnet", "location": "Night City Datacenter", "svi": "VLAN-200-MGMT"},
            {"ip": "172.16.0.0/16", "comments": "Guest Access Layer", "location": "Watson District", "svi": "VLAN-300-PROD"},
            {"ip": "10.10.10.0/30", "comments": "P2P Link to Badlands", "location": "Badlands Hub", "svi": "VLAN-400-SVI"},
            {"ip": "10.255.0.1/32", "comments": "Loopback Interconnect", "location": "Westbrook Node", "svi": "VLAN-100-CORE"}
        ]
        physical_locations = ["Night City Datacenter", "Badlands Hub", "Watson District", "Westbrook Node", "Arasaka Tower"]
        svi_locations = ["VLAN-100-CORE", "VLAN-200-MGMT", "VLAN-300-PROD", "VLAN-400-SVI"]
        subnet_types = ["DATA", "VOIP", "VIDEO", "MANAGEMENT", "SECURITY"]
        self.render("IPAMHomePage.html", title="IPAM", items=items, 
                    physical_locations=physical_locations, 
                    svi_locations=svi_locations, 
                    subnet_types=subnet_types)

    def post(self):
        # Extract fields from the request
        network_container = self.get_argument("network_container", "off")
        ip_address = self.get_argument("ip_address", "")
        comments = self.get_argument("comments", "")
        physical_location = self.get_argument("physical_location", "N/A")
        svi_location = self.get_argument("svi_location", "N/A")
        subnet_type = self.get_argument("subnet_type", "N/A")
        prefix_size = self.get_argument("prefix_size", "24")

        # Simulate processing - log to console with Cyberpunk flavor
        print("-" * 40)
        print(">> INCOMING CONNECTION: IPAM_ADD_SERVICE")
        print(f">> DATA PACKET RECEIVED:")
        print(f"   - TARGET IP: {ip_address}/{prefix_size}")
        print(f"   - CONTAINER MODE: {network_container.upper()}")
        print(f"   - PHYSICAL LOC: {physical_location}")
        print(f"   - VIRTUAL LOC: {svi_location}")
        print(f"   - CLASS: {subnet_type}")
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
    url(r"/IPAM", IPAMHandler, name="IPAM"),
    ],autoreload=True,debug=True)
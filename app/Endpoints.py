from Network.L2.Switch import Stack
from Network.L3.Router import Router
from Network.MultiDeviceFunctions import Endpoint
from Services.SQL.Mysql import DB
from vendors.infoblox import restapi
from netaddr import mac_cisco


def getIPSFromARPTable(RouterIP,List_of_Endpoints_obj):
    """

    @param RouterIP:
    @type RouterIP:
    @param listofEndpoints: A list of Endpoint objects
    @type listofEndpoints: list
    @return:
    @rtype:
    """
    list_of_endpoints_with_ips = []  # get IP from arp table on router
    r = Router(RouterIP)
    r.get_started()
    for endpoint in List_of_Endpoints_obj:
        endpoint.Router = RouterIP
        for iparp in r.arps:
            if endpoint.mac == iparp.mac:
                endpoint.ip = iparp
                list_of_endpoints_with_ips.append(endpoint)
                break
    r.logout()
    return list_of_endpoints_with_ips
def getDNSNamesForEndpoints(List_of_endpoints):
    final_end_point_infomation = []
    for endp in List_of_endpoints:
        api = restapi()
        endp.dnsname = api.get_host_record(ipad=endp.ip)
        final_end_point_infomation.append(endp)
    return final_end_point_infomation

def ScanNetworkForEndPoints(list_of_switches):
    """
    Collects all the endpoint information need for database from all the access layer switches in the database
    Adds the gathered information into the endpoint table in the database
    @return:
    @rtype:
    """
    routers_for_endpoints = []
    for switchtuple in list_of_switches: # get mac addresses, and ports from access layer switches in database
        try:
            router_with_end_points = {}
            router_with_end_points["endpoints"] = []
            router_with_end_points["switchid"] = (switchtuple[0])
            s = Stack(switchtuple[1])
            s.login()
            s.conn.enable_cisco()
            s.getSwitchInfo()
            s.assignattributes()
            router_with_end_points["routerip"] = s.defaultgateway
            all_ports = s.allinterfaces()
            for port in all_ports:
                if not port.trunk:
                    for macaddress in port.mac_addresses:
                        e = Endpoint()
                        macaddress.dialect = mac_cisco
                        e.mac = str(macaddress)
                        e.switchport = str(port)
                        e.company = macaddress.oui.registration(0).org
                        e.Switch = s.ip
                        router_with_end_points["endpoints"].append(e)
            if router_with_end_points["endpoints"]:
                routers_for_endpoints.append(router_with_end_points)
        except Exception as e:
            print(e)
            continue
        s.logout()
    routers_with_ip_endpoints = []
    for database_router in routers_for_endpoints:
        database_router["endpoints"] = getIPSFromARPTable(database_router["routerip"],database_router["endpoints"])
        routers_with_ip_endpoints.append(database_router)
    final_end_point_infomation = []
    for endpoints_with_ips in routers_with_ip_endpoints:
        final_end_point_infomation.append(getDNSNamesForEndpoints(endpoints_with_ips["endpoints"]))
    with DB() as conn: # add all infomation to table
        for e_point in final_end_point_infomation:
            conn.addendpoint(f"endpoints (ipaddress,dnsname,switchport,macaddress,company,NetID) VALUES (%s,%s,%s,%s,%s,%s)",e_point.sqlValues)

def updateEndpoints():
    with DB() as conn:
        switches = conn.GetallSwitches()
    ScanNetworkForEndPoints(switches[:5])


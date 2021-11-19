from Network.Switch import Stack
from Vendor_Applications.Solarwinds.Orion import Orion


def Update_device_names_in_all_applications(switch=None,orion=False,ddi=false):
    """
    This function is used to update all the locations that a device might have been labeled in all locations.
    :return:
    """
    device_hostname = None
    device_bannername = None
    if switch:
        device_hostname = None
        device_bannername = None
        s = Stack(switch)
        s.login()
        s.getSwitchInfo()
        s.assignattributes()
        device_hostname = s.hostname
        device_bannername = s.bannername
        s.logout()
    if orion:
        o = Orion()
        o.login()
        o.get_switch(switch)
    if ddi:
        ddi =





if __name__=="__main__":
    Update_device_names_in_all_applications("155.101.202.41",orion=True,ddi=True)

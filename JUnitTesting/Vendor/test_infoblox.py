import unittest
from vendors.infoblox import restapi

class TestRouter(unittest.TestCase):

    def test_login(self):
        rest = restapi()
        rest.get_Network_containers_all(netadd="10.0.0.0/8")
    def test_get_network_contrainer(self):
        rest = restapi()
        result = rest.get_Network_container(netadd="10.24.4.0/22")
        print(result)

    def test_createNetwork(self):
        data = [
{"size":24,"network":"10.179.0.0","comment":f"""Vlan: 2401
devices: Network
Router:2100S-CI3850
Location: 2100"""},
{"size":24,"network":"10.179.0.0","comment":f"""Vlan: 2402
devices: Video Security
Router:2100S-CI3850
Location: 2100"""},
{"size":24,"network":"10.179.0.0","comment":f"""Vlan: 2403
devices: Facilities
Router:2100S-CI3850
Location: 2100"""},
{"size":24,"network":"10.179.0.0","comment":f"""Vlan: 2404
devices: Voip
Router:2100S-CI3850
Location: 2100"""},
{"size":24,"network":"10.179.0.0","comment":f"""Vlan: 2405
devices: IOT
Router:2100S-CI3850
Location: 2100"""},
{"size":24,"network":"10.179.0.0","comment":f"""Vlan: 2406
devices: User
Router:2100S-CI3850
Location: 2100"""},
{"size":24,"network":"10.180.0.0","comment":f"""Vlan: 2451
devices: Network
Router:CustFirstCI3850-12
Location: CustFirst"""},
{"size":24,"network":"10.180.0.0","comment":f"""Vlan: 2452
devices: Video Security
Router:CustFirstCI3850-12
Location: CustFirst"""},
{"size":24,"network":"10.180.0.0","comment":f"""Vlan: 2453
devices: Facilities
Router:CustFirstCI3850-12
Location: CustFirst"""},
{"size":24,"network":"10.180.0.0","comment":f"""Vlan: 2454
devices: Voip
Router:CustFirstCI3850-12
Location: CustFirst"""},
{"size":24,"network":"10.180.0.0","comment":f"""Vlan: 2455
devices: IOT
Router:CustFirstCI3850-12
Location: CustFirst"""},
{"size":24,"network":"10.180.0.0","comment":f"""Vlan: 2456
devices: User
Router:CustFirstCI3850-12
Location: CustFirst"""},
{"size":24,"network":"10.181.0.0","comment":f"""Vlan: 2451
devices: Network
Router:CE1CI3850
Location: CE"""},
{"size":24,"network":"10.181.0.0","comment":f"""Vlan: 2452
devices: Video Security
Router:CE1CI3850
Location: CE"""},
{"size":24,"network":"10.181.0.0","comment":f"""Vlan: 2453
devices: Facilities
Router:CE1CI3850
Location: CE"""},
{"size":24,"network":"10.181.0.0","comment":f"""Vlan: 2454
devices: Voip
Router:CE1CI3850
Location: CE"""},
{"size":24,"network":"10.181.0.0","comment":f"""Vlan: 2455
devices: IOT
Router:CE1CI3850
Location: CE"""},
{"size":24,"network":"10.181.0.0","comment":f"""Vlan: 2456
devices: User
Router:CE1CI3850
Location: CE"""},
{"size":24,"network":"10.182.0.0","comment":f"""Vlan: 2451
devices: Network
Router:Tooele-CIASA
Location: Tooele"""},
{"size":24,"network":"10.182.0.0","comment":f"""Vlan: 2452
devices: Video Security
Router:Tooele-CIASA
Location: Tooele"""},
{"size":24,"network":"10.182.0.0","comment":f"""Vlan: 2453
devices: Facilities
Router:Tooele-CIASA
Location: Tooele"""},
{"size":24,"network":"10.182.0.0","comment":f"""Vlan: 2454
devices: Voip
Router:Tooele-CIASA
Location: Tooele"""},
{"size":24,"network":"10.182.0.0","comment":f"""Vlan: 2455
devices: IOT
Router:Tooele-CIASA
Location: Tooele"""},
{"size":24,"network":"10.182.0.0","comment":f"""Vlan: 2456
devices: User
Router:Tooele-CIASA
Location: Tooele"""},
{"size":24,"network":"10.183.0.0","comment":f"""Vlan: 2601
devices: Network
Router:RS1A-C3850-12
Location: riverside"""},
{"size":24,"network":"10.183.0.0","comment":f"""Vlan: 2602
devices: Video Security
Router:RS1A-C3850-12
Location: riverside"""},
{"size":24,"network":"10.183.0.0","comment":f"""Vlan: 2603
devices: Facilities
Router:RS1A-C3850-12
Location: riverside"""},
{"size":24,"network":"10.183.0.0","comment":f"""Vlan: 2604
devices: Voip
Router:RS1A-C3850-12
Location: riverside"""},
{"size":24,"network":"10.183.0.0","comment":f"""Vlan: 2605
devices: IOT
Router:RS1A-C3850-12
Location: riverside"""},
{"size":24,"network":"10.183.0.0","comment":f"""Vlan: 2606
devices: User
Router:RS1A-C3850-12
Location: riverside"""},
{"size":24,"network":"10.184.0.0","comment":f"""Vlan: 3251
devices: Network
Router:OGTC-B-CI3850
Location: Ogden Tic"""},
{"size":24,"network":"10.184.0.0","comment":f"""Vlan: 3252
devices: Video Security
Router:OGTC-B-CI3850
Location: Ogden Tic"""},
{"size":24,"network":"10.184.0.0","comment":f"""Vlan: 3253
devices: Facilities
Router:OGTC-B-CI3850
Location: Ogden Tic"""},
{"size":24,"network":"10.184.0.0","comment":f"""Vlan: 3254
devices: Voip
Router:OGTC-B-CI3850
Location: Ogden Tic"""},
{"size":24,"network":"10.184.0.0","comment":f"""Vlan: 3255
devices: IOT
Router:OGTC-B-CI3850
Location: Ogden Tic"""},
{"size":24,"network":"10.184.0.0","comment":f"""Vlan: 3256
devices: User
Router:OGTC-B-CI3850
Location: Ogden Tic"""},
{"size":24,"network":"10.185.0.0","comment":f"""Vlan: 3301
devices: Network
Router:OG1ACI3850
Location: Ogden"""},
{"size":24,"network":"10.185.0.0","comment":f"""Vlan: 3302
devices: Video Security
Router:OG1ACI3850
Location: Ogden"""},
{"size":24,"network":"10.185.0.0","comment":f"""Vlan: 3303
devices: Facilities
Router:OG1ACI3850
Location: Ogden"""},
{"size":24,"network":"10.185.0.0","comment":f"""Vlan: 3304
devices: Voip
Router:OG1ACI3850
Location: Ogden"""},
{"size":24,"network":"10.185.0.0","comment":f"""Vlan: 3305
devices: IOT
Router:OG1ACI3850
Location: Ogden"""},
{"size":24,"network":"10.185.0.0","comment":f"""Vlan: 3306
devices: User
Router:OG1ACI3850
Location: Ogden"""},
{"size":24,"network":"10.186.0.0","comment":f"""Vlan: 3351
devices: Network
Router:WSACI3850-1
Location: Warm Springs"""},
{"size":24,"network":"10.186.0.0","comment":f"""Vlan: 3352
devices: Video Security
Router:WSACI3850-1
Location: Warm Springs"""},
{"size":24,"network":"10.186.0.0","comment":f"""Vlan: 3353
devices: Facilities
Router:WSACI3850-1
Location: Warm Springs"""},
{"size":24,"network":"10.186.0.0","comment":f"""Vlan: 3354
devices: Voip
Router:WSACI3850-1
Location: Warm Springs"""},
{"size":24,"network":"10.186.0.0","comment":f"""Vlan: 3355
devices: IOT
Router:WSACI3850-1
Location: Warm Springs"""},
{"size":24,"network":"10.186.0.0","comment":f"""Vlan: 3356
devices: User
Router:WSACI3850-1
Location: Warm Springs"""},
{"size":24,"network":"10.187.0.0","comment":f"""Vlan: 3401
devices: Network
Router:FLHQACI3850
Location: FLHQ"""},
{"size":24,"network":"10.187.0.0","comment":f"""Vlan: 3402
devices: Video Security
Router:FLHQACI3850
Location: FLHQ"""},
{"size":24,"network":"10.187.0.0","comment":f"""Vlan: 3403
devices: Facilities
Router:FLHQACI3850
Location: FLHQ"""},
{"size":24,"network":"10.187.0.0","comment":f"""Vlan: 3404
devices: Voip
Router:FLHQACI3850
Location: FLHQ"""},
{"size":24,"network":"10.187.0.0","comment":f"""Vlan: 3405
devices: IOT
Router:FLHQACI3850
Location: FLHQ"""},
{"size":24,"network":"10.187.0.0","comment":f"""Vlan: 3406
devices: User
Router:FLHQACI3850
Location: FLHQ"""},
{"size":24,"network":"10.188.0.0","comment":f"""Vlan: 3451
devices: Network
Router:MB3CI3850
Location: MeadowBrook"""},
{"size":24,"network":"10.188.0.0","comment":f"""Vlan: 3452
devices: Video Security
Router:MB3CI3850
Location: MeadowBrook"""},
{"size":24,"network":"10.188.0.0","comment":f"""Vlan: 3453
devices: Facilities
Router:MB3CI3850
Location: MeadowBrook"""},
{"size":24,"network":"10.188.0.0","comment":f"""Vlan: 3454
devices: Voip
Router:MB3CI3850
Location: MeadowBrook"""},
{"size":24,"network":"10.188.0.0","comment":f"""Vlan: 3455
devices: IOT
Router:MB3CI3850
Location: MeadowBrook"""},
{"size":24,"network":"10.188.0.0","comment":f"""Vlan: 3456
devices: User
Router:MB3CI3850
Location: MeadowBrook"""},
{"size":24,"network":"10.189.0.0","comment":f"""Vlan: 3501
devices: Network
Router:DDC-CI9500-Core
Location: UofU DDC"""},
{"size":24,"network":"10.189.0.0","comment":f"""Vlan: 3502
devices: Video Security
Router:DDC-CI9500-Core
Location: UofU DDC"""},
{"size":24,"network":"10.189.0.0","comment":f"""Vlan: 3503
devices: Facilities
Router:DDC-CI9500-Core
Location: UofU DDC"""},
{"size":24,"network":"10.189.0.0","comment":f"""Vlan: 3504
devices: Voip
Router:DDC-CI9500-Core
Location: UofU DDC"""},
{"size":24,"network":"10.189.0.0","comment":f"""Vlan: 3505
devices: IOT
Router:DDC-CI9500-Core
Location: UofU DDC"""},
{"size":24,"network":"10.189.0.0","comment":f"""Vlan: 3506
devices: User
Router:DDC-CI9500-Core
Location: UofU DDC"""},
{"size":24,"network":"10.190.0.0","comment":f"""Vlan: 3551
devices: Network
Router:DR-TDC-C9500
Location: UofU TDC (DR)"""},
{"size":24,"network":"10.190.0.0","comment":f"""Vlan: 3552
devices: Video Security
Router:DR-TDC-C9500
Location: UofU TDC (DR)"""},
{"size":24,"network":"10.190.0.0","comment":f"""Vlan: 3553
devices: Facilities
Router:DR-TDC-C9500
Location: UofU TDC (DR)"""},
{"size":24,"network":"10.190.0.0","comment":f"""Vlan: 3554
devices: Voip
Router:DR-TDC-C9500
Location: UofU TDC (DR)"""},
{"size":24,"network":"10.190.0.0","comment":f"""Vlan: 3555
devices: IOT
Router:DR-TDC-C9500
Location: UofU TDC (DR)"""},
{"size":24,"network":"10.190.0.0","comment":f"""Vlan: 3556
devices: User
Router:DR-TDC-C9500
Location: UofU TDC (DR)"""},
{"size":24,"network":"10.191.0.0","comment":f"""Vlan: 3601
devices: Network
Router:DDTC3ACI9300
Location: DDTC"""},
{"size":24,"network":"10.191.0.0","comment":f"""Vlan: 3602
devices: Video Security
Router:DDTC3ACI9300
Location: DDTC"""},
{"size":24,"network":"10.191.0.0","comment":f"""Vlan: 3603
devices: Facilities
Router:DDTC3ACI9300
Location: DDTC"""},
{"size":24,"network":"10.191.0.0","comment":f"""Vlan: 3604
devices: Voip
Router:DDTC3ACI9300
Location: DDTC"""},
{"size":24,"network":"10.191.0.0","comment":f"""Vlan: 3605
devices: IOT
Router:DDTC3ACI9300
Location: DDTC"""},
{"size":24,"network":"10.191.0.0","comment":f"""Vlan: 3606
devices: User
Router:DDTC3ACI9300
Location: DDTC"""},
{"size":24,"network":"10.192.0.0","comment":f"""Vlan: 3651
devices: Network
Router:MRSCACI3850
Location: midvale rail service center"""},
{"size":24,"network":"10.192.0.0","comment":f"""Vlan: 3652
devices: Video Security
Router:MRSCACI3850
Location: midvale rail service center"""},
{"size":24,"network":"10.192.0.0","comment":f"""Vlan: 3653
devices: Facilities
Router:MRSCACI3850
Location: midvale rail service center"""},
{"size":24,"network":"10.192.0.0","comment":f"""Vlan: 3654
devices: Voip
Router:MRSCACI3850
Location: midvale rail service center"""},
{"size":24,"network":"10.192.0.0","comment":f"""Vlan: 3655
devices: IOT
Router:MRSCACI3850
Location: midvale rail service center"""},
{"size":24,"network":"10.192.0.0","comment":f"""Vlan: 3656
devices: User
Router:MRSCACI3850
Location: midvale rail service center"""},
{"size":24,"network":"10.193.0.0","comment":f"""Vlan: 3701
devices: Network
Router:JRSCACI3850X
Location: Jordan River"""},
{"size":24,"network":"10.193.0.0","comment":f"""Vlan: 3702
devices: Video Security
Router:JRSCACI3850X
Location: Jordan River"""},
{"size":24,"network":"10.193.0.0","comment":f"""Vlan: 3703
devices: Facilities
Router:JRSCACI3850X
Location: Jordan River"""},
{"size":24,"network":"10.193.0.0","comment":f"""Vlan: 3704
devices: Voip
Router:JRSCACI3850X
Location: Jordan River"""},
{"size":24,"network":"10.193.0.0","comment":f"""Vlan: 3705
devices: IOT
Router:JRSCACI3850X
Location: Jordan River"""},
{"size":24,"network":"10.193.0.0","comment":f"""Vlan: 3706
devices: User
Router:JRSCACI3850X
Location: Jordan River"""},
{"size":24,"network":"10.194.0.0","comment":f"""Vlan: 3751
devices: Network
Router:MC1CI3850-12
Location: Mobility Center"""},
{"size":24,"network":"10.194.0.0","comment":f"""Vlan: 3752
devices: Video Security
Router:MC1CI3850-12
Location: Mobility Center"""},
{"size":24,"network":"10.194.0.0","comment":f"""Vlan: 3753
devices: Facilities
Router:MC1CI3850-12
Location: Mobility Center"""},
{"size":24,"network":"10.194.0.0","comment":f"""Vlan: 3754
devices: Voip
Router:MC1CI3850-12
Location: Mobility Center"""},
{"size":24,"network":"10.194.0.0","comment":f"""Vlan: 3755
devices: IOT
Router:MC1CI3850-12
Location: Mobility Center"""},
{"size":24,"network":"10.194.0.0","comment":f"""Vlan: 3756
devices: User
Router:MC1CI3850-12
Location: Mobility Center"""},
{"size":24,"network":"10.195.0.0","comment":f"""Vlan: 3801
devices: Network
Router:TimpOpsCI3850-12
Location: timp Operations"""},
{"size":24,"network":"10.195.0.0","comment":f"""Vlan: 3802
devices: Video Security
Router:TimpOpsCI3850-12
Location: timp Operations"""},
{"size":24,"network":"10.195.0.0","comment":f"""Vlan: 3803
devices: Facilities
Router:TimpOpsCI3850-12
Location: timp Operations"""},
{"size":24,"network":"10.195.0.0","comment":f"""Vlan: 3804
devices: Voip
Router:TimpOpsCI3850-12
Location: timp Operations"""},
{"size":24,"network":"10.195.0.0","comment":f"""Vlan: 3805
devices: IOT
Router:TimpOpsCI3850-12
Location: timp Operations"""},
{"size":24,"network":"10.195.0.0","comment":f"""Vlan: 3806
devices: User
Router:TimpOpsCI3850-12
Location: timp Operations"""},
{"size":24,"network":"10.196.0.0","comment":f"""Vlan: 3851
devices: Network
Router:ProvoTIC-CI3850
Location: Provo Tic"""},
{"size":24,"network":"10.196.0.0","comment":f"""Vlan: 3852
devices: Video Security
Router:ProvoTIC-CI3850
Location: Provo Tic"""},
{"size":24,"network":"10.196.0.0","comment":f"""Vlan: 3853
devices: Facilities
Router:ProvoTIC-CI3850
Location: Provo Tic"""},
{"size":24,"network":"10.196.0.0","comment":f"""Vlan: 3854
devices: Voip
Router:ProvoTIC-CI3850
Location: Provo Tic"""},
{"size":24,"network":"10.196.0.0","comment":f"""Vlan: 3855
devices: IOT
Router:ProvoTIC-CI3850
Location: Provo Tic"""},
{"size":24,"network":"10.196.0.0","comment":f"""Vlan: 3856
devices: User
Router:ProvoTIC-CI3850
Location: Provo Tic"""},
{"size":24,"network":"10.197.0.0","comment":f"""Vlan: 3901
devices: Network
Router:2100-PA-820
Location: 2100UDP"""},
{"size":24,"network":"10.197.0.0","comment":f"""Vlan: 3902
devices: Video Security
Router:2100-PA-820
Location: 2100UDP"""},
{"size":24,"network":"10.197.0.0","comment":f"""Vlan: 3903
devices: Facilities
Router:2100-PA-820
Location: 2100UDP"""},
{"size":24,"network":"10.197.0.0","comment":f"""Vlan: 3904
devices: Voip
Router:2100-PA-820
Location: 2100UDP"""},
{"size":24,"network":"10.197.0.0","comment":f"""Vlan: 3905
devices: IOT
Router:2100-PA-820
Location: 2100UDP"""},
{"size":24,"network":"10.197.0.0","comment":f"""Vlan: 3906
devices: User
Router:2100-PA-820
Location: 2100UDP"""},
{"size":24,"network":"10.198.0.0","comment":f"""Vlan: 3901
devices: Network
Router:MB1UCJIASA
Location: MurrayUPD"""},
{"size":24,"network":"10.198.0.0","comment":f"""Vlan: 3902
devices: Video Security
Router:MB1UCJIASA
Location: MurrayUPD"""},
{"size":24,"network":"10.198.0.0","comment":f"""Vlan: 3903
devices: Facilities
Router:MB1UCJIASA
Location: MurrayUPD"""},
{"size":24,"network":"10.198.0.0","comment":f"""Vlan: 3904
devices: Voip
Router:MB1UCJIASA
Location: MurrayUPD"""},
{"size":24,"network":"10.198.0.0","comment":f"""Vlan: 3905
devices: IOT
Router:MB1UCJIASA
Location: MurrayUPD"""},
{"size":24,"network":"10.198.0.0","comment":f"""Vlan: 3906
devices: User
Router:MB1UCJIASA
Location: MurrayUPD"""},
{"size":24,"network":"10.199.0.0","comment":f"""Vlan: 3951
devices: Network
Router:ProvoUPD-PA-820
Location: ProvoPD"""},
{"size":24,"network":"10.199.0.0","comment":f"""Vlan: 3952
devices: Video Security
Router:ProvoUPD-PA-820
Location: ProvoPD"""},
{"size":24,"network":"10.199.0.0","comment":f"""Vlan: 3953
devices: Facilities
Router:ProvoUPD-PA-820
Location: ProvoPD"""},
{"size":24,"network":"10.199.0.0","comment":f"""Vlan: 3954
devices: Voip
Router:ProvoUPD-PA-820
Location: ProvoPD"""},
{"size":24,"network":"10.199.0.0","comment":f"""Vlan: 3955
devices: IOT
Router:ProvoUPD-PA-820
Location: ProvoPD"""},
{"size":24,"network":"10.199.0.0","comment":f"""Vlan: 3956
devices: User
Router:ProvoUPD-PA-820
Location: ProvoPD"""},
{"size":24,"network":"10.200.0.0","comment":f"""Vlan: 4001
devices: Network
Router:FW-OgdenPD
Location: OgdenPD"""},
{"size":24,"network":"10.200.0.0","comment":f"""Vlan: 4002
devices: Video Security
Router:FW-OgdenPD
Location: OgdenPD"""},
{"size":24,"network":"10.200.0.0","comment":f"""Vlan: 4003
devices: Facilities
Router:FW-OgdenPD
Location: OgdenPD"""},
{"size":24,"network":"10.200.0.0","comment":f"""Vlan: 4004
devices: Voip
Router:FW-OgdenPD
Location: OgdenPD"""},
{"size":24,"network":"10.200.0.0","comment":f"""Vlan: 4005
devices: IOT
Router:FW-OgdenPD
Location: OgdenPD"""},
{"size":24,"network":"10.200.0.0","comment":f"""Vlan: 4006
devices: User
Router:FW-OgdenPD
Location: OgdenPD"""}]
        for networks in data:
            rest = restapi()
            result = rest.createNetwork(networks)
            print(result)
    def test_createContainer(self):
        datalist = [
{"size":16,"network":"10.179.0.0","comment":f"""Vlan Range: Vlan 2400 -> 2449 
Location: 2100 
Router:2100S-CI3850"""},
{"size":16,"network":"10.180.0.0","comment":f"""Vlan Range: Vlan 2450 -> 2499 
Location: CustFirst 
Router:CustFirstCI3850-12"""},
{"size":16,"network":"10.181.0.0","comment":f"""Vlan Range: Vlan 2500 -> 2549 
Location: CE 
Router:CE1CI3850"""},
{"size":16,"network":"10.182.0.0","comment":f"""Vlan Range: Vlan 2550 -> 2599 
Location: Tooele 
Router:Tooele-CIASA"""},
{"size":16,"network":"10.183.0.0","comment":f"""Vlan Range: Vlan 2600 -> 2649 
Location: riverside 
Router:RS1A-C3850-12"""},
{"size":16,"network":"10.184.0.0","comment":f"""Vlan Range: Vlan 3250 -> 3299 
Location: Ogden Tic 
Router:OGTC-B-CI3850"""},
{"size":16,"network":"10.185.0.0","comment":f"""Vlan Range: Vlan 3300 -> 3349 
Location: Ogden 
Router:OG1ACI3850"""},
{"size":16,"network":"10.186.0.0","comment":f"""Vlan Range: Vlan 3350 -> 3399 
Location: Warm Springs 
Router:WSACI3850-1"""},
{"size":16,"network":"10.187.0.0","comment":f"""Vlan Range: Vlan 3400 -> 3449 
Location: FLHQ 
Router:FLHQACI3850"""},
{"size":16,"network":"10.188.0.0","comment":f"""Vlan Range: Vlan 3450 -> 3499 
Location: MeadowBrook 
Router:MB3CI3850"""},
{"size":16,"network":"10.189.0.0","comment":f"""Vlan Range: Vlan 3500 -> 3549 
Location: UofU DDC 
Router:DDC-CI9500-Core"""},
{"size":16,"network":"10.190.0.0","comment":f"""Vlan Range: Vlan 3550 -> 3599 
Location: UofU TDC (DR) 
Router:DR-TDC-C9500"""},
{"size":16,"network":"10.191.0.0","comment":f"""Vlan Range: Vlan 3600 -> 3649 
Location: DDTC 
Router:DDTC3ACI9300"""},
{"size":16,"network":"10.192.0.0","comment":f"""Vlan Range: Vlan 3650 -> 3699 
Location: midvale rail service center 
Router:MRSCACI3850"""},
{"size":16,"network":"10.193.0.0","comment":f"""Vlan Range: Vlan 3700 -> 3749 
Location: Jordan River 
Router:JRSCACI3850X"""},
{"size":16,"network":"10.194.0.0","comment":f"""Vlan Range: Vlan 3750 -> 3799 
Location: Mobility Center 
Router:MC1CI3850-12"""},
{"size":16,"network":"10.195.0.0","comment":f"""Vlan Range: Vlan 3800 -> 3849 
Location: timp Operations 
Router:TimpOpsCI3850-12"""},
{"size":16,"network":"10.196.0.0","comment":f"""Vlan Range: Vlan 3850 -> 3899 
Location: Provo Tic 
Router:ProvoTIC-CI3850"""},
{"size":16,"network":"10.197.0.0","comment":f"""Vlan Range: Vlan 3900 -> 3949 
Location: 2100UDP 
Router:2100-PA-820"""},
{"size":16,"network":"10.198.0.0","comment":f"""Vlan Range: Vlan 3950 -> 3999 
Location: MurrayUPD 
Router:MB1UCJIASA"""},
{"size":16,"network":"10.199.0.0","comment":f"""Vlan Range: Vlan 4000 -> 4049 
Location: ProvoPD 
Router:ProvoUPD-PA-820"""},
{"size":16,"network":"10.200.0.0","comment":f"""Vlan Range: Vlan 4050 -> 4094 
Location: OgdenPD 
Router:FW-OgdenPD"""}]
        for data in datalist:
            rest = restapi()
            result = rest.createContainer(data)

    def test_create_multiple_networks(self,data,network):
        data = [
{"size":24, "router":"FW-Critical", "vlan": "2655", "location":"TRXS"},
{"size":24, "router":"FW-Critical", "vlan": "2705", "location":"TRXN"},
{"size":24, "router":"FW-Critical", "vlan": "2755", "location":"TXU"},
{"size":24, "router":"FW-Critical", "vlan": "2805", "location":"CRN"},
{"size":24, "router":"FW-Critical", "vlan": "2855", "location":"CRS"},
{"size":24, "router":"FW-Critical", "vlan": "2905", "location":"TMJ"},
{"size":24, "router":"FW-Critical", "vlan": "2955", "location":"TWV"},
{"size":24, "router":"FW-Critical", "vlan": "3005", "location":"TXA"},
{"size":24, "router":"FW-Critical", "vlan": "3055", "location":"SC"},
{"size":24, "router":"FW-Critical", "vlan": "3105", "location":"UVX"},
{"size":24, "router":"FW-Critical", "vlan": "3155", "location":"OGX"},
]
        rest = restapi()
        rest.create_multiple_networks("10.70.0.0/16",data)

    def test_create_host_record(self):
        r = restapi()
        records = [("TVM-CRN-Clearfield_N","10.23.0.4","10.23.0.0/26"),
("TVM-CRN-Clearfield_S","10.23.0.5","10.23.0.0/26"),
("TVM-CRN-Farm_S","10.23.0.6","10.23.0.0/26"),
("TVM-CRN-Farm_N","10.23.0.7","10.23.0.0/26"),
("TVM-CRN-Layton_S","10.23.0.8","10.23.0.0/26"),
("TVM-CRN-Layton_N","10.23.0.9","10.23.0.0/26"),
("TVM-CRN-N_Temple_S1","10.23.0.10","10.23.0.0/26"),
("TVM-CRN-N_Temple_N2","10.23.0.11","10.23.0.0/26"),
("TVM-CRN-OgdenSE","10.23.0.12","10.23.0.0/26"),
("TVM-CRN-OgdenSW","10.23.0.13","10.23.0.0/26"),
("TVM-CRN-Ogden_N","10.23.0.14","10.23.0.0/26"),
("TVM-CRN-Roy_S","10.23.0.15","10.23.0.0/26"),
("TVM-CRN-Roy_N","10.23.0.16","10.23.0.0/26"),
("TVM-CRN-SLCentralSW","10.23.0.17","10.23.0.0/26"),
("TVM-CRN-SLCentralSE","10.23.0.18","10.23.0.0/26"),
("TVM-CRN-SLCentral_N","10.23.0.19","10.23.0.0/26"),
("TVM-CRN-WoodsCr_S","10.23.0.20","10.23.0.0/26"),
("TVM-CRN-WoodsCr_N","10.23.0.21","10.23.0.0/26"),
("TVM-CRS-Am_Fork_S1","10.23.0.68","10.23.0.64/26"),
("TVM-CRS-Am_Fork_N2","10.23.0.69","10.23.0.64/26"),
("TVM-CRS-Draper_S1","10.23.0.70","10.23.0.64/26"),
("TVM-CRS-Draper_N2","10.23.0.71","10.23.0.64/26"),
("TVM-CRS-Lehi_S1","10.23.0.72","10.23.0.64/26"),
("TVM-CRS-Lehi_N2","10.23.0.73","10.23.0.64/26"),
("TVM-CRS-Vineyard_S1","10.23.0.74","10.23.0.64/26"),
("TVM-CRS-Vineyard_N2","10.23.0.75","10.23.0.64/26"),
("TVM-CRS-Murray_S1","10.23.0.76","10.23.0.64/26"),
("TVM-CRS-Murray_N2","10.23.0.77","10.23.0.64/26"),
("TVM-CRS-Orem_S1","10.23.0.78","10.23.0.64/26"),
("TVM-CRS-Orem_N2","10.23.0.79","10.23.0.64/26"),
("TVM-CRS-Provo_SE1","10.23.0.80","10.23.0.64/26"),
("TVM-CRS-Provo_NW2","10.23.0.81","10.23.0.64/26"),
("TVM-CRS-Provo_SE3","10.23.0.82","10.23.0.64/26"),
("TVM-CRS-Provo_NW4","10.23.0.83","10.23.0.64/26"),
("TVM-CRS-Jordan_S1","10.23.0.84","10.23.0.64/26"),
("TVM-CRS-Jordan_N2","10.23.0.85","10.23.0.64/26"),
("TVM-SC-300E","10.23.0.132","10.23.0.128/26"),
("TVM-SC-500E_N","10.23.0.133","10.23.0.128/26"),
("TVM-SC-500E_S","10.23.0.134","10.23.0.128/26"),
("TVM-SC-700E","10.23.0.135","10.23.0.128/26"),
("TVM-SC-CntrlPnt","10.23.0.136","10.23.0.128/26"),
("TVM-SC-1045E_N","10.23.0.137","10.23.0.128/26"),
("TVM-SC-1045E_S","10.23.0.138","10.23.0.128/26"),
("TVM-SC-StateSt","10.23.0.139","10.23.0.128/26"),
("TVM-SC-900E","10.23.0.140","10.23.0.128/26"),
("TVM-TXA-1940W_WW1","10.23.0.195","10.23.0.192/26"),
("TVM-TXA-1940W_EE4","10.23.0.196","10.23.0.192/26"),
("TVM-TXA-Airport_WC1","10.23.0.197","10.23.0.192/26"),
("TVM-TXA-Airport_NN3","10.23.0.198","10.23.0.192/26"),
("TVM-TXA-AirportSS6","10.23.0.199","10.23.0.192/26"),
("TVM-TXA-Fairpark_WW1","10.23.0.200","10.23.0.192/26"),
("TVM-TXA-Fairpark_EE4","10.23.0.201","10.23.0.192/26"),
("TVM-TXA-JksnEcld_WW1","10.23.0.202","10.23.0.192/26"),
("TVM-TXA-JksnEcld_EE4","10.23.0.203","10.23.0.192/26"),
("TVM-TXA-Ntemple_WW1","10.23.0.204","10.23.0.192/26"),
("TVM-TXA-Ntemple_EE4","10.23.0.205","10.23.0.192/26"),
("TVM-TXA-Ntemple_N5","10.23.0.206","10.23.0.192/26"),
("TVM-TXA-Power_WW1","10.23.0.207","10.23.0.192/26"),
("TVM-TXA-Power_EE4","10.23.0.208","10.23.0.192/26"),
("TVM-TXMJ-2700WNE1","10.23.1.4","10.23.1.0/26"),
("TVM-TXMJ-2700WSW8","10.23.1.5","10.23.1.0/26"),
("TVM-TXMJ-4773WNE1","10.23.1.6","10.23.1.0/26"),
("TVM-TXMJ-4773WSW8","10.23.1.7","10.23.1.0/26"),
("TVM-TXMJ-5651WNE1","10.23.1.8","10.23.1.0/26"),
("TVM-TXMJ-5651WSW8","10.23.1.9","10.23.1.0/26"),
("TVM-TXMJ-BngJnctNE1","10.23.1.10","10.23.1.0/26"),
("TVM-TXMJ-BngJnctSW8","10.23.1.11","10.23.1.0/26"),
("TVM-TXMJ-DbrkPkwyNE1","10.23.1.12","10.23.1.0/26"),
("TVM-TXMJ-DbrkPkwyNE2","10.23.1.13","10.23.1.0/26"),
("TVM-TXMJ-DbrkPkwySW7","10.23.1.14","10.23.1.0/26"),
("TVM-TXMJ-DbrkPkwySW8","10.23.1.15","10.23.1.0/26"),
("TVM-TXMJ-FPWMJNE1","10.23.1.16","10.23.1.0/26"),
("TVM-TXMJ-FPWMJSW8","10.23.1.17","10.23.1.0/26"),
("TVM-TXMJ-HGardnerNE1","10.23.1.18","10.23.1.0/26"),
("TVM-TXMJ-HGardnerSW8","10.23.1.19","10.23.1.0/26"),
("TVM-TXMJ-JordanVlyNE1","10.23.1.20","10.23.1.0/26"),
("TVM-TXMJ-JordanVlySW8","10.23.1.21","10.23.1.0/26"),
("TVM-TXMJ-SJPkwyNE1","10.23.1.22","10.23.1.0/26"),
("TVM-TXMJ-SJPkwySW7","10.23.1.23","10.23.1.0/26"),
("TVM-TXMJ-SJPkwySW8","10.23.1.24","10.23.1.0/26"),
("TVM-TXMJ-WJCtyCtrNE1","10.23.1.25","10.23.1.0/26"),
("TVM-TXMJ-WJCtyCtrSW8","10.23.1.26","10.23.1.0/26"),
("TVM-TXN-600S_N","10.23.1.68","10.23.1.64/26"),
("TVM-TXN-600S_S","10.23.1.69","10.23.1.64/26"),
("TVM-TXN-900_S_N1","10.23.1.70","10.23.1.64/26"),
("TVM-TXN-900_S_S","10.23.1.71","10.23.1.64/26"),
("TVM-TXN-Arena_E","10.23.1.72","10.23.1.64/26"),
("TVM-TXN-Arena_EE","10.23.1.73","10.23.1.64/26"),
("TVM-TXN-Arena_W","10.23.1.74","10.23.1.64/26"),
("TVM-TXN-BallParkS4","10.23.1.75","10.23.1.64/26"),
("TVM-TXN-BallParkN","10.23.1.76","10.23.1.64/26"),
("TVM-TXN-BallParkSS","10.23.1.77","10.23.1.64/26"),
("TVM-TXN-CentralPt_N","10.23.1.78","10.23.1.64/26"),
("TVM-TXN-CentralPt_S","10.23.1.79","10.23.1.64/26"),
("TVM-TXN-City_Ctr_N1","10.23.1.80","10.23.1.64/26"),
("TVM-TXN-City_Ctr_S","10.23.1.81","10.23.1.64/26"),
("TVM-TXN-City_Ctr_N","10.23.1.82","10.23.1.64/26"),
("TVM-TXN-City_Ctr_SS","10.23.1.83","10.23.1.64/26"),
("TVM-TXN-Court_N","10.23.1.84","10.23.1.64/26"),
("TVM-TXN-Crt_House_S2","10.23.1.85","10.23.1.64/26"),
("TVM-TXN-Gallivan_S","10.23.1.86","10.23.1.64/26"),
("TVM-TXN-GalivanPL_N","10.23.1.87","10.23.1.64/26"),
("TVM-TXN-Meadowbr_N","10.23.1.88","10.23.1.64/26"),
("TVM-TXN-Meadowbrook_S","10.23.1.89","10.23.1.64/26"),
("TVM-TXN-Millcreek_N","10.23.1.90","10.23.1.64/26"),
("TVM-TXN-Millcreek_S","10.23.1.91","10.23.1.64/26"),
("TVM-TXN-OldGreekEa","10.23.1.92","10.23.1.64/26"),
("TVM-TXN-Planet_S","10.23.1.93","10.23.1.64/26"),
("TVM-TXN-Planet_N","10.23.1.94","10.23.1.64/26"),
("TVM-TXN-SLCentralN","10.23.1.95","10.23.1.64/26"),
("TVM-TXN-SLCentralWe","10.23.1.96","10.23.1.64/26"),
("TVM-TXN-TempleSqEa","10.23.1.97","10.23.1.64/26"),
("TVM-TXN-TempleSq_W","10.23.1.98","10.23.1.64/26"),
("TVM-TXS-FashionPl_N","10.23.1.132","10.23.1.128/26"),
("TVM-TXS-FashionPl_S","10.23.1.133","10.23.1.128/26"),
("TVM-TXS-FtUnion_N","10.23.1.134","10.23.1.128/26"),
("TVM-TXS-MVFtUn_S","10.23.1.135","10.23.1.128/26"),
("TVM-TXS-HSandy_N","10.23.1.136","10.23.1.128/26"),
("TVM-TXS-HSandy_S","10.23.1.137","10.23.1.128/26"),
("TVM-TXS-MidvaleCtr_N","10.23.1.138","10.23.1.128/26"),
("TVM-TXS-MidvaleCtr_S","10.23.1.139","10.23.1.128/26"),
("TVM-TXS-MurrayCtrl_S","10.23.1.140","10.23.1.128/26"),
("TVM-TXS-MidvaleCtr_S","10.23.1.141","10.23.1.128/26"),
("TVM-TXS-MurrayNrth_S","10.23.1.142","10.23.1.128/26"),
("TVM-TXS-Murray_N_N","10.23.1.143","10.23.1.128/26"),
("TVM-TXS-SandyCvcS","10.23.1.144","10.23.1.128/26"),
("TVM-TXS-SandyCvcNL","10.23.1.145","10.23.1.128/26"),
("TVM-TXS-SandyCvcSL","10.23.1.146","10.23.1.128/26"),
("TVM-TXS-SandyCC_N1","10.23.1.147","10.23.1.128/26"),
("TVM-TXS-SandyExpo_S1","10.23.1.148","10.23.1.128/26"),
("TVM-TXS-SandyExpoSE","10.23.1.149","10.23.1.128/26"),
("TVM-TXS-SandyExpo_SW","10.23.1.150","10.23.1.128/26"),
("TVM-TXS-CresentView_N","10.23.1.151","10.23.1.128/26"),
("TVM-TXS-CresentView_S","10.23.1.152","10.23.1.128/26"),
("TVM-TXS-DraperTC_NN","10.23.1.153","10.23.1.128/26"),
("TVM-TXS-DraperTC_N","10.23.1.154","10.23.1.128/26"),
("TVM-TXS-DraperTC_S","10.23.1.155","10.23.1.128/26"),
("TVM-TXS-Kimballs_Lane_N","10.23.1.156","10.23.1.128/26"),
("TVM-TXS-Kimballs_Lane_S","10.23.1.157","10.23.1.128/26"),
("TVM-TXU-900E_E1","10.23.1.196","10.23.1.192/26"),
("TVM-TXU-900_East_W","10.23.1.197","10.23.1.192/26"),
("TVM-TXU-FtDouglas_N1","10.23.1.198","10.23.1.192/26"),
("TVM-TXU-Library_W1","10.23.1.199","10.23.1.192/26"),
("TVM-TXU-Library-E","10.23.1.200","10.23.1.192/26"),
("TVM-TXU-So_Campus_E1","10.23.1.201","10.23.1.192/26"),
("TVM-TXU-StadiumSW","10.23.1.202","10.23.1.192/26"),
("TVM-TXU-StadiumSE","10.23.1.203","10.23.1.192/26"),
("TVM-TXU-StadiumNW","10.23.1.204","10.23.1.192/26"),
("TVM-TXU-Stadium-NE","10.23.1.205","10.23.1.192/26"),
("TVM-TXU-TrolleyWe","10.23.1.206","10.23.1.192/26"),
("TVM-TXU-Trolley-EE","10.23.1.207","10.23.1.192/26"),
("TVM-TXU-UMedCtrSW","10.23.1.208","10.23.1.192/26"),
("TVM-TXU-UMedCtrSE","10.23.1.209","10.23.1.192/26"),
("TVM-TXU-MedicalCtr-N","10.23.1.210","10.23.1.192/26"),
("TVM-TXWV-DeckerLkNE1","10.23.2.4","10.23.2.0/26"),
("TVM-TXWV-DeckerLkSW8","10.23.2.5","10.23.2.0/26"),
("TVM-TXWV-RdwdJnctNE1","10.23.2.6","10.23.2.0/26"),
("TVM-TXWV-RdwdJnctSW8","10.23.2.7","10.23.2.0/26"),
("TVM-TXWV-RiverTrlNE1","10.23.2.8","10.23.2.0/26"),
("TVM-TXWV-RiverTrlSW8","10.23.2.9","10.23.2.0/26"),
("TVM-TXWV-WVCntrlNE1","10.23.2.10","10.23.2.0/26"),
("TVM-TXWV-WVCntrlNE2","10.23.2.11","10.23.2.0/26"),
("TVM-TXWV-WVCntrlSW7","10.23.2.12","10.23.2.0/26"),
("TVM-TXWV-WVCntrlSW8","10.23.2.13","10.23.2.0/26"),
("TVM-TVM-JRSC-ShopTest","10.23.2.68","10.23.2.64/29")]
        for tvm in records:
            comment = ""
            r.create_host_record(tvm[2],tvm[0] + ".uta.cog.ut.us",comment=comment,nextavailable=None,ipad=tvm[1])

    def test_get_host_record(self):
        r = restapi()
        r.get_host_record("10.23.0.4")

    def test_sort(self):
        List_1 = [
("FrontRunner - North", "Clearfield", "North", "Clearfield_N", "10.46.21.1", "221002", "10.23.0.4","10.23.0.1", "/26", "255.255.255.192"),
("FrontRunner - North", "Clearfield", "South","Clearfield_S", "10.46.12.102", "203001", "10.23.0.5",  "10.23.0.1", "/26", "255.255.255.192"),
("FrontRunner - North", "Farmington", "South", "Farm_S", "10.46.21.2", "221003", "10.23.0.6",  "10.23.0.1", "/26", "255.255.255.192"),
("FrontRunner - North", "Farmington", "North", "Farm_N", "10.46.21.3", "221004", "10.23.0.7",  "10.23.0.1", "/26", "255.255.255.192"),
("FrontRunner - North", "Layton", "South", "Layton_S", "10.46.21.4", "221005", "10.23.0.8",  "10.23.0.1", "/26", "255.255.255.192"),
("FrontRunner - North", "Layton", "North", "Layton_N", "10.46.21.5", "221006", "10.23.0.9",  "10.23.0.1", "/26", "255.255.255.192"),
("FrontRunner - North", "North Temple", "South", "NTemple_S", "10.46.12.96", "203171", "10.23.0.10",  "10.23.0.1", "/26", "255.255.255.192"),
("FrontRunner - North", "North Temple", "North", "NTemple_N", "10.46.12.97", "203172", "10.23.0.11",  "10.23.0.1", "/26", "255.255.255.192"),
("FrontRunner - North", "Ogden Transit Center", "South 2","Ogden_SE", "10.46.21.8", "221008",  "10.23.0.12", "10.23.0.1", "/26", "255.255.255.192"),
("FrontRunner - North", "Ogden Transit Center", "South", "Ogden_SW", "10.46.21.6", "221009",  "10.23.0.13", "10.23.0.1", "/26", "255.255.255.192"),
("FrontRunner - North", "Ogden Transit Center", "North", "Ogden_N", "10.46.21.7", "221010",  "10.23.0.14", "10.23.0.1", "/26", "255.255.255.192"),
("FrontRunner - North", "Roy", "South", "Roy_S", "10.46.21.9", "221013", "10.23.0.15", "10.23.0.1",  "/26", "255.255.255.192"),
("FrontRunner - North", "Roy", "North", "Roy_N", "10.46.21.10", "221014", "10.23.0.16", "10.23.0.1",  "/26", "255.255.255.192"),
("FrontRunner - North", "Salt Lake Central", "South", "SLCentral_SW", "10.46.21.11", "221015",  "10.23.0.17", "10.23.0.1", "/26", "255.255.255.192"),
("FrontRunner - North", "Salt Lake Central", "South", "SLCentral_SE", "10.46.21.13", "221007",  "10.23.0.18", "10.23.0.1", "/26", "255.255.255.192"),
("FrontRunner - North", "Salt Lake Central", "North", "SLCentral_N", "10.46.21.12", "221016",  "10.23.0.19", "10.23.0.1", "/26", "255.255.255.192"),
("FrontRunner - North", "Woods Cross", "South", "WoodsCr_S", "10.46.21.14", "221017", "10.23.0.20",  "10.23.0.1", "/26", "255.255.255.192"),
("FrontRunner - North", "Woods Cross", "North", "WoodsCr_N", "10.46.21.15", "221018", "10.23.0.21",  "10.23.0.1", "/26", "255.255.255.192"),
("FrontRunner - South", "American Fork", "South", "AmFork_S", "10.46.47.17", "203155", "10.23.0.68",  "10.23.0.65", "/26", "255.255.255.192"),
("FrontRunner - South", "American Fork", "North", "AmFork_N", "10.46.47.18", "203156", "10.23.0.69",  "10.23.0.65", "/26", "255.255.255.192"),
("FrontRunner - South", "Draper", "South", "Draper_S", "10.46.47.9", "203147", "10.23.0.70",  "10.23.0.65", "/26", "255.255.255.192"),
("FrontRunner - South", "Draper", "North", "Draper_N", "10.46.47.10", "203148", "10.23.0.71",  "10.23.0.65", "/26", "255.255.255.192"),
("FrontRunner - South", "Lehi", "South", "Lehi_S", "10.46.47.13", "203151", "10.23.0.72",  "10.23.0.65", "/26", "255.255.255.192"),
("FrontRunner - South", "Lehi", "North", "Lehi_N", "10.46.47.14", "203152", "10.23.0.73",  "10.23.0.65", "/26", "255.255.255.192"),
("FrontRunner - South", "Vineyard", "South", "Vineyard_S", "10.46.47.29", "203167", "10.23.0.74",  "10.23.0.65", "/26", "255.255.255.192"),
("FrontRunner - South", "Vineyard", "North", "Vineyard_N", "10.46.47.35", "221019", "10.23.0.75",  "10.23.0.65", "/26", "255.255.255.192"),
("FrontRunner - South", "Murray Central", "South", "Murray_S", "10.46.47.1", "203139", "10.23.0.76",  "10.23.0.65", "/26", "255.255.255.192"),
("FrontRunner - South", "Murray Central", "North", "Murray_N", "10.46.47.2", "203140", "10.23.0.77",  "10.23.0.65", "/26", "255.255.255.192"),
("FrontRunner - South", "Orem", "South", "Orem_S", "10.46.47.21", "203159", "10.23.0.78",  "10.23.0.65", "/26", "255.255.255.192"),
("FrontRunner - South", "Orem", "North", "Orem_N", "10.46.47.22", "203160", "10.23.0.79",  "10.23.0.65", "/26", "255.255.255.192"),
("FrontRunner - South", "Provo", "South 1","Provo_NE", "10.46.47.25", "203163", "10.23.0.80",  "10.23.0.65", "/26", "255.255.255.192"),
("FrontRunner - South", "Provo", "North 2","Provo_NW", "10.46.47.26", "203164", "10.23.0.81",  "10.23.0.65", "/26", "255.255.255.192"),
("FrontRunner - South", "Provo", "South 3","Provo_SE", "10.46.47.27", "203165", "10.23.0.82",  "10.23.0.65", "/26", "255.255.255.192"),
("FrontRunner - South", "Provo", "North 4","Provo_SW", "10.46.47.28", "203166", "10.23.0.83",  "10.23.0.65", "/26", "255.255.255.192"),
("FrontRunner - South", "South Jordan", "South", "Jordan_S", "10.46.47.5", "203143", "10.23.0.84",  "10.23.0.65", "/26", "255.255.255.192"),
("FrontRunner - South", "South Jordan", "North", "Jordan_N", "10.46.47.6", "203144", "10.23.0.85",  "10.23.0.65", "/26", "255.255.255.192"),
("Streetcar - SugarH", "300 East", "Canopy", "SC_300E", "10.46.67.13", "206003", "10.23.0.132",  "10.23.0.129", "/26", "255.255.255.192"),
("Streetcar - SugarH", "500 East", "_N","SC_500E_N", "10.46.67.14", "206004", "10.23.0.133",  "10.23.0.129", "/26", "255.255.255.192"),
("Streetcar - SugarH", "500 East", "_S","SC_500E_S", "10.46.67.15", "206005", "10.23.0.134",  "10.23.0.129", "/26", "255.255.255.192"),
("Streetcar - SugarH", "700 East", "Canopy", "SC_700E", "10.46.67.16", "206006", "10.23.0.135",  "10.23.0.129", "/26", "255.255.255.192"),
("Streetcar - SugarH", "Central Pointe", "Canopy", "SC_CntrPntl", "10.46.67.11", "206001",  "10.23.0.136", "10.23.0.129", "/26", "255.255.255.192"),
("Streetcar - SugarH", "Fairmont (1040 E),_N", "SC_1045E_N", "10.46.67.18", "206008", "10.23.0.137",  "10.23.0.129", "/26", "255.255.255.192"),
("Streetcar - SugarH", "Fairmont (1040 E),_S", "SC_1045E_S", "10.46.67.19", "206009", "10.23.0.138",  "10.23.0.129", "/26", "255.255.255.192"),
("Streetcar - SugarH", "South Salt Lake Center", "Canopy", "SC_StatSt", "10.46.67.12", "206002",  "10.23.0.139", "10.23.0.129", "/26", "255.255.255.192"),
("Streetcar - SugarH", "Sugarmont (900 E),Canopy", "SC_900E", "10.46.67.17", "206007", "10.23.0.140",  "10.23.0.129", "/26", "255.255.255.192"),
("Trax - Airport", "1940 W", "WW1","1940W_W", "10.46.48.7", "204306", "10.23.0.195", "10.23.0.193",  "/26", "255.255.255.192"),
("Trax - Airport", "1940 W", "EE4","1940W_E", "10.46.48.10", "204309", "10.23.0.196", "10.23.0.193",  "/26", "255.255.255.192"),
("Trax - Airport", "Airport", "WCE", "Airport_W", "10.46.48.1", "204300", "10.23.0.197",  "10.23.0.193", "/26", "255.255.255.192"),
("Trax - Airport", "Airport", "NN1","Airport_N", "10.46.48.3", "204302", "10.23.0.198", "10.23.0.193",  "/26", "255.255.255.192"),
("Trax - Airport", "Airport", "SS4","Airport_S", "10.46.48.6", "204305", "10.23.0.199", "10.23.0.193",  "/26", "255.255.255.192"),
("Trax - Airport", "Fairpark", "WW1","Fairpark_W", "10.46.48.15", "204314", "10.23.0.200",  "10.23.0.193", "/26", "255.255.255.192"),
("Trax - Airport", "Fairpark", "EE4","Fairpark_E", "10.46.48.18", "204317", "10.23.0.201",  "10.23.0.193", "/26", "255.255.255.192"),
("Trax - Airport", "Jackson/Euclid", "WW1","JksnEcld_W", "10.46.48.19", "204318", "10.23.0.202",  "10.23.0.193", "/26", "255.255.255.192"),
("Trax - Airport", "Jackson/Euclid", "EE4","JksnEcld_E", "10.46.48.22", "204321", "10.23.0.203",  "10.23.0.193", "/26", "255.255.255.192"),
("Trax - Airport", "North Temple", "WW1","Ntempleg_W", "10.46.48.23", "204322", "10.23.0.204",  "10.23.0.193", "/26", "255.255.255.192"),
("Trax - Airport", "North Temple", "EE4","Ntempleg_E", "10.46.48.26", "204325", "10.23.0.205",  "10.23.0.193", "/26", "255.255.255.192"),
("Trax - Airport", "North Temple", "N5,Ntempleg_N", "10.46.48.27", "204326", "10.23.0.206",  "10.23.0.193", "/26", "255.255.255.192"),
("Trax - Airport", "Power", "WW1","Power_W", "10.46.48.11", "204310", "10.23.0.207", "10.23.0.193",  "/26", "255.255.255.192"),
("Trax - Airport", "Power", "EE4","Power_E", "10.46.48.14", "204313", "10.23.0.208", "10.23.0.193",  "/26", "255.255.255.192"),
("Trax - Mid-Jordan", "2700 W", "NE1","2700W_NE", "10.46.45.51", "204081", "10.23.1.4", "10.23.1.1",  "/26", "255.255.255.192"),
("Trax - Mid-Jordan", "2700 W", "_SW8","2700W_SW", "10.46.45.58", "204088", "10.23.1.5", "10.23.1.1",  "/26", "255.255.255.192"),
("Trax - Mid-Jordan", "4773 W", "NE1","4773W_NE", "10.46.45.71", "204101", "10.23.1.6", "10.23.1.1",  "/26", "255.255.255.192"),
("Trax - Mid-Jordan", "4773 W", "_SW8","4773W_SW", "10.46.45.78", "204108", "10.23.1.7", "10.23.1.1",  "/26", "255.255.255.192"),
("Trax - Mid-Jordan", "5651 W", "NE1","5651W_NE", "10.46.45.81", "204111", "10.23.1.8", "10.23.1.1",  "/26", "255.255.255.192"),
("Trax - Mid-Jordan", "5651 W", "_SW8","5651W_SW", "10.46.45.88", "204118", "10.23.1.9", "10.23.1.1",  "/26", "255.255.255.192"),
("Trax - Mid-Jordan", "Bingham Junction", "NE1","BngJnct_NE", "10.46.45.21", "204051", "10.23.1.10",  "10.23.1.1", "/26", "255.255.255.192"),
("Trax - Mid-Jordan", "Bingham Junction", "_SW8","BngJnct_SW", "10.46.45.28", "204058", "10.23.1.11",  "10.23.1.1", "/26", "255.255.255.192"),
("Trax - Mid-Jordan", "Daybreak Pkwy", "NE1","DbrkPkwy_NW", "10.46.45.101", "204131", "10.23.1.12",  "10.23.1.1", "/26", "255.255.255.192"),
("Trax - Mid-Jordan", "Daybreak Pkwy", "NE2","DbrkPkwy_NE", "10.46.45.102", "204132", "10.23.1.13",  "10.23.1.1", "/26", "255.255.255.192"),
("Trax - Mid-Jordan", "Daybreak Pkwy", "_SW7,DbrkPkwy_SW", "10.46.45.107", "204137", "10.23.1.14",  "10.23.1.1", "/26", "255.255.255.192"),
("Trax - Mid-Jordan", "Daybreak Pkwy", "_SW8","DbrkPkwy_SW", "10.46.45.108", "204138", "10.23.1.15",  "10.23.1.1", "/26", "255.255.255.192"),
("Trax - Mid-Jordan", "Fashion Place", "N1","FPWMJ_NE", "10.46.45.11", "204041", "10.23.1.16",  "10.23.1.1", "/26", "255.255.255.192"),
("Trax - Mid-Jordan", "Fashion Place", "S2","FPWMJ_SW", "10.46.45.18", "204048", "10.23.1.17",  "10.23.1.1", "/26", "255.255.255.192"),
("Trax - Mid-Jordan", "Historic Gardner", "NE1","HGardner_NE", "10.46.45.31", "204061", "10.23.1.18",  "10.23.1.1", "/26", "255.255.255.192"),
("Trax - Mid-Jordan", "Historic Gardner", "_SW8","HGardner_SW", "10.46.45.38", "204068", "10.23.1.19",  "10.23.1.1", "/26", "255.255.255.192"),
("Trax - Mid-Jordan", "Jordan Valley", "NE1","JordanVly_NE", "10.46.45.61", "204091", "10.23.1.20",  "10.23.1.1", "/26", "255.255.255.192"),
("Trax - Mid-Jordan", "Jordan Valley", "_SW8","JordanVly_SW", "10.46.45.68", "204098", "10.23.1.21",  "10.23.1.1", "/26", "255.255.255.192"),
("Trax - Mid-Jordan", "South Jordan Pkwy", "NE1","SJPkwy_NE", "10.46.45.91", "204121", "10.23.1.22",  "10.23.1.1", "/26", "255.255.255.192"),
("Trax - Mid-Jordan", "South Jordan Pkwy", "_SW7,SJPkwy_SW", "10.46.45.97", "204127", "10.23.1.23",  "10.23.1.1", "/26", "255.255.255.192"),
("Trax - Mid-Jordan", "South Jordan Pkwy", "_SW8","SJPkwy_SW", "10.46.45.98", "204128", "10.23.1.24",  "10.23.1.1", "/26", "255.255.255.192"),
("Trax - Mid-Jordan", "West Jordan City Center", "NE1","WJCtyCtr_NE", "10.46.45.41", "204071",  "10.23.1.25", "10.23.1.1", "/26", "255.255.255.192"),
("Trax - Mid-Jordan", "West Jordan City Center", "_SW8","WJCtyCtr_SW", "10.46.45.48", "204078",  "10.23.1.26", "10.23.1.1", "/26", "255.255.255.192"),
("Trax - North", "600_S", "N1","600S_N", "10.46.45.101", "204131", "10.23.1.68", "10.23.1.65", "/26",  "255.255.255.192"),
("Trax - North", "600_S", "S","600S_S", "10.46.45.107", "204137", "10.23.1.69", "10.23.1.65", "/26",  "255.255.255.192"),
("Trax - North", "900 South", "N1","900So_N", "10.46.42.91", "204210", "10.23.1.70", "10.23.1.65",  "/26", "255.255.255.192"),
("Trax - North", "900 South", "S2","900So_S", "10.46.42.94", "204235", "10.23.1.71", "10.23.1.65",  "/26", "255.255.255.192"),
("Trax - North", "Arena", "E","Arena_E", "10.46.42.43", "204228", "10.23.1.72", "10.23.1.65", "/26",  "255.255.255.192"),
("Trax - North", "Arena", "EE", "Arena_EE", "10.46.42.44", "204229", "10.23.1.73", "10.23.1.65", "/26","255.255.255.192"),
("Trax - North", "Arena", "W","Arena_W", "10.46.43.1", "208010", "10.23.1.74", "10.23.1.65", "/26",  "255.255.255.192"),
("Trax - North", "Ball Park", "_S","BallPark_S", "10.46.42.104", "204208", "10.23.1.75", "10.23.1.65",  "/26", "255.255.255.192"),
("Trax - North", "Ball Park", "_N","BallPark_N", "10.46.42.102", "204233", "10.23.1.76", "10.23.1.65",  "/26", "255.255.255.192"),
("Trax - North", "Ball Park", "S_S", "BallPark_S", "10.46.42.103", "204234", "10.23.1.77", "10.23.1.65","/26", "255.255.255.192"),
("Trax - North", "Central Pointe", "North", "CentralPt_N", "10.46.22.1","222014", "10.23.1.78",  "10.23.1.65", "/26", "255.255.255.192"),
("Trax - North", "Central Pointe", "South", "CentralPt_S", "10.46.22.2","222017", "10.23.1.79",  "10.23.1.65", "/26", "255.255.255.192"),
("Trax - North", "City Center", "N_N", "CityCtr_N", "10.46.42.61", "204201", "10.23.1.80",  "10.23.1.65", "/26", "255.255.255.192"),
("Trax - North", "City Center", "_S","CityCtr_S", "10.46.42.63", "204213", "10.23.1.81", "10.23.1.65",  "/26", "255.255.255.192"),
("Trax - North", "City Center", "_N","CityCtr_N", "10.46.42.62", "204231", "10.23.1.82", "10.23.1.65",  "/26", "255.255.255.192"),
("Trax - North", "City Center", "S_S", "CityCtr_S", "10.46.42.64", "204232", "10.23.1.83",  "10.23.1.65", "/26", "255.255.255.192"),
("Trax - North", "Court House", "North 1","Court_N", "10.46.22.3","222056", "10.23.1.84", "10.23.1.65",  "/26", "255.255.255.192"),
("Trax - North", "Court House", "South", "Court_S", "10.46.42.84", "204202", "10.23.1.85",  "10.23.1.65", "/26", "255.255.255.192"),
("Trax - North", "Gallivan", "South 2","Gallivan_S", "10.46.22.7","222055", "10.23.1.86", "10.23.1.65",  "/26", "255.255.255.192"),
("Trax - North", "Gallivan", "North 1","Gallivan_N", "10.46.42.71", "204209", "10.23.1.87",  "10.23.1.65", "/26", "255.255.255.192"),
("Trax - North", "Meadowbrook", "North 1","Meadowbr_N", "10.46.22.10","222026", "10.23.1.88", "10.23.1.65","/26", "255.255.255.192"),
("Trax - North", "Meadowbrook", "_S","Meadowbr_S", "10.46.43.2", "208011", "10.23.1.89", "10.23.1.65",  "/26", "255.255.255.192"),
("Trax - North", "Millcreek", "North 1","Millcreek_N", "10.46.22.13","222022", "10.23.1.90", "10.23.1.65",  "/26", "255.255.255.192"),
("Trax - North", "Millcreek", "_S","Millcreek_S", "10.46.43.3", "208012", "10.23.1.91", "10.23.1.65",  "/26", "255.255.255.192"),
("Trax - North", "Old Greek Town", "East", "OldGreekE", "10.46.22.16","222006", "10.23.1.92",  "10.23.1.65", "/26", "255.255.255.192"),
("Trax - North", "Planetarium", "South", "Planet_S", "10.46.22.17", "222003", "10.23.1.93",  "10.23.1.65", "/26", "255.255.255.192"),
("Trax - North", "Planetarium", "North", "Planet_N", "10.46.22.18", "222004", "10.23.1.94",  "10.23.1.65", "/26", "255.255.255.192"),
("Trax - North", "Salt Lake Central", "North", "SLCentral_N", "10.46.22.19", "222002", "10.23.1.95",  "10.23.1.65", "/26", "255.255.255.192"),
("Trax - North", "Salt Lake Central", "West", "SLCentral_W", "10.46.22.20", "222087", "10.23.1.96",  "10.23.1.65", "/26", "255.255.255.192"),
("Trax - North", "Temple Square", "East 2","TempleSq_E", "10.46.22.25", "222047", "10.23.1.97",  "10.23.1.65", "/26", "255.255.255.192"),
("Trax - North", "Temple Square", "W","TempleSq_W", "10.46.42.56", "204211", "10.23.1.98", "10.23.1.65",  "/26", "255.255.255.192"),
("Trax - South", "Fashion Place", "North 1","FashionPl_N", "10.46.22.4", "222038", "10.23.1.132",  "10.23.1.129", "/26", "255.255.255.192"),
("Trax - South", "Fashion Place", "South 2","FashionPl_S", "10.46.22.5", "222276", "10.23.1.133",  "10.23.1.129", "/26", "255.255.255.192"),
("Trax - South", "Fort Union", "North", "FtUnion_N", "10.46.22.6", "222067", "10.23.1.134",  "10.23.1.129", "/26", "255.255.255.192"),
("Trax - South", "Fort Union", "South", "FtUnion_S", "10.46.49.4", "208014", "10.23.1.135",  "10.23.1.129", "/26", "255.255.255.192"),
("Trax - South", "Historic Sandy", "North 1","HSandy_N", "10.46.22.8", "222075", "10.23.1.136",  "10.23.1.129", "/26", "255.255.255.192"),
("Trax - South", "Historic Sandy", "South 2","HSandy_S", "10.46.22.9", "222078", "10.23.1.137",  "10.23.1.129", "/26", "255.255.255.192"),
("Trax - South", "Midvale", "North 1","MidvaleCtr_N", "10.46.22.11", "222071", "10.23.1.138",  "10.23.1.129", "/26", "255.255.255.192"),
("Trax - South", "Midvale", "South 2","MidvaleCtr_S", "10.46.22.12", "222074", "10.23.1.139",  "10.23.1.129", "/26", "255.255.255.192"),
("Trax - South", "Murray Central", "South 2","MurrayCtrl_S", "10.46.22.14", "222037", "10.23.1.140",  "10.23.1.129", "/26", "255.255.255.192"),
("Trax - South", "Murray Central", "N1","MurrayCtrl_N", "10.46.22.12", "222074", "10.23.1.141",  "10.23.1.129", "/26", "255.255.255.192"),
("Trax - South", "Murray North", "South", "MurrayNo_S", "10.46.22.15", "222033", "10.23.1.142",  "10.23.1.129", "/26", "255.255.255.192"),
("Trax - South", "Murray North", "_N","MurrayNo_N", "10.46.49.2", "208013", "10.23.1.143", "10.23.1.129",  "/26", "255.255.255.192"),
("Trax - South", "Sandy Civic", "South 2","SandyCvc_S", "10.46.22.21", "222082", "10.23.1.144",  "10.23.1.129", "/26", "255.255.255.192"),
("Trax - South", "Sandy Civic", "South 3","SandyCvc_N", "10.46.22.22", "222083", "10.23.1.145",  "10.23.1.129", "/26", "255.255.255.192"),
("Trax - South", "Sandy Civic", "South 4","SandyCvc_S", "10.46.22.23", "222084", "10.23.1.146",  "10.23.1.129", "/26", "255.255.255.192"),
("Trax - South", "Sandy Civic", "North", "SandyCC_N", "10.46.43.83", "204212", "10.23.1.147",  "10.23.1.129", "/26", "255.255.255.192"),
("Trax - South", "Sandy Expo", "N1","SandyExpo_N", "10.46.43.73", "202065", "10.23.1.148",  "10.23.1.129", "/26", "255.255.255.192"),
("Trax - South", "Sandy Expo", "_SE", "SandyExpo_SE", "10.46.43.72", "202066", "10.23.1.149",  "10.23.1.129", "/26", "255.255.255.192"),
("Trax - South", "Sandy Expo", "_SW", "SandyExpo_SW", "10.46.49.1", "204301", "10.23.1.150",  "10.23.1.129", "/26", "255.255.255.192"),
("Trax - South Draper", "Cresent View", "North", "CresentView_N", "10.46.43.90", "204220",  "10.23.1.151", "10.23.1.129", "/26", "255.255.255.192"),
("Trax - South Draper", "Cresent View", "South", "CresentView_S", "10.46.43.91", "204221",  "10.23.1.152", "10.23.1.129", "/26", "255.255.255.192"),
("Trax - South Draper", "Draper Town Center", "North", "DraperTC_N", "10.46.43.92", "204222",  "10.23.1.153", "10.23.1.129", "/26", "255.255.255.192"),
("Trax - South Draper", "Draper Town Center", "North", "DraperTC_N", "10.46.43.93", "204223",  "10.23.1.154", "10.23.1.129", "/26", "255.255.255.192"),
("Trax - South Draper", "Draper Town Center", "South", "DraperTC_S", "10.46.43.94", "204224",  "10.23.1.155", "10.23.1.129", "/26", "255.255.255.192"),
("Trax - South Draper", "Kimballs Lane", "North", "KimballsLn_N", "10.46.43.95", "204225",  "10.23.1.156", "10.23.1.129", "/26", "255.255.255.192"),
("Trax - South Draper", "Kimballs Lane", "South", "KimballsLn_S", "10.46.43.96", "204226",  "10.23.1.157", "10.23.1.129", "/26", "255.255.255.192"),
("Trax - University", "900 East", "E,900E_E", "10.46.12.31", "204203", "10.23.1.196", "10.23.1.193",  "/26", "255.255.255.192"),
("Trax - University", "900 East", "W,900E_W", "10.46.47.104", "204240", "10.23.1.197",  "10.23.1.193", "/26", "255.255.255.192"),
("Trax - University", "Fort Douglas", "_N","FtDouglas_N", "10.46.44.63", "204207", "10.23.1.198",  "10.23.1.193", "/26", "255.255.255.192"),
("Trax - University", "Library", "W","Library_W", "10.46.12.21", "204205", "10.23.1.199", "10.23.1.193","/26", "255.255.255.192"),
("Trax - University", "Library", "E","Library_E", "10.46.44.3", "208003", "10.23.1.200", "10.23.1.193",  "/26", "255.255.255.192"),
("Trax - University", "South Campus", "E","SoCampus_E", "10.46.44.53", "204206", "10.23.1.201",  "10.23.1.193", "/26", "255.255.255.192"),
("Trax - University", "Stadium", "_SW", "Stadium_SW", "10.46.22.27", "222066", "10.23.1.202",  "10.23.1.193", "/26", "255.255.255.192"),
("Trax - University", "Stadium", "_SE", "Stadium_SE", "10.46.22.26", "222300", "10.23.1.203",  "10.23.1.193", "/26", "255.255.255.192"),
("Trax - University", "Stadium", "NW", "Stadium_NW", "10.46.22.28", "222403", "10.23.1.204",  "10.23.1.193", "/26", "255.255.255.192"),
("Trax - University", "Stadium", "NE", "Stadium_NE", "10.46.44.15", "208015", "10.23.1.205",  "10.23.1.193", "/26", "255.255.255.192"),
("Trax - University", "Trolley", "W1","Trolley_W", "10.46.22.29", "222401", "10.23.1.206", "10.23.1.193","/26", "255.255.255.192"),
("Trax - University", "Trolley", "EE", "Trolley_E", "10.46.44.8", "208008", "10.23.1.207",  "10.23.1.193", "/26", "255.255.255.192"),
("Trax - University", "U Medical Center", "_SW", "UMedCtr_NE", "10.46.22.30", "222275", "10.23.1.208",  "10.23.1.193", "/26", "255.255.255.192"),
("Trax - University", "U Medical Center", "_SE", "UMedCtr_SE", "10.46.22.31", "222405", "10.23.1.209",  "10.23.1.193", "/26", "255.255.255.192"),
("Trax - University", "U Medical Center", "_N","MedicalCtr_N", "10.46.44.29", "208028", "10.23.1.210",  "10.23.1.193", "/26", "255.255.255.192"),
("Trax - West Valley", "Decker Lake", "NE1","DeckerLk_NE", "10.46.46.31", "204021", "10.23.2.4",  "10.23.2.1", "/26", "255.255.255.192"),
("Trax - West Valley", "Decker Lake", "_SW8","DeckerLk_SW", "10.46.46.38", "204028", "10.23.2.5",  "10.23.2.1", "/26", "255.255.255.192"),
("Trax - West Valley", "Redwood Junction", "NE1","RdwdJnctNE", "10.46.46.21", "204011", "10.23.2.6",  "10.23.2.1", "/26", "255.255.255.192"),
("Trax - West Valley", "Redwood Junction", "_SW8","RdwdJnct_SW", "10.46.46.28", "204018", "10.23.2.7",  "10.23.2.1", "/26", "255.255.255.192"),
("Trax - West Valley", "River Trail", "NE1","RiverTrl_NE", "10.46.46.11", "204001", "10.23.2.8",  "10.23.2.1", "/26", "255.255.255.192"),
("Trax - West Valley", "River Trail", "_SW8","RiverTrl_SW", "10.46.46.18", "204008", "10.23.2.9",  "10.23.2.1", "/26", "255.255.255.192"),
("Trax - West Valley", "West Valley Central", "NE1","WVCntrl_NE", "10.46.46.41", "204031", "10.23.2.10",  "10.23.2.1", "/26", "255.255.255.192"),
("Trax - West Valley", "West Valley Central", "NE2","WVCntrl_NE", "10.46.46.42", "204032", "10.23.2.11",  "10.23.2.1", "/26", "255.255.255.192"),
("Trax - West Valley", "West Valley Central", "_SE", "WVCntrl_SW", "10.46.46.47", "204037",  "10.23.2.12", "10.23.2.1", "/26", "255.255.255.192"),
("Trax - West Valley", "West Valley Central", "_SW", "WVCntrl_SW", "10.46.46.48", "204038",  "10.23.2.13", "10.23.2.1", "/26", "255.255.255.192")
                  ]
        List_2 = [("200001", "Ogden_N", "200", "104", "Ogden","7", "10.23.0.1,", "10.23.0.1","","2001"),
                  ("200002", "Ogden_SE", "200", "104", "Ogden","7", "10.23.0.2,", "10.23.0.2","","2002"),
                  ("200003", "Odgen_SW", "200", "104", "Ogden","7", "10.23.0.3,", "10.23.0.3","","2003"),
                  ("200004", "Roy_N", "200", "106", "Roy","7", "10.23.0.4,", "10.23.0.4","","2004"),
                  ("200005", "Roy_S", "200", "106", "Roy","7", "10.23.0.5,", "10.23.0.5","","2005"),
                  ("200006", "Clearfield_N", "200", "100", "Clearfield","7", "10.23.0.6,", "10.23.0.6","","2006"),
                  ("200007", "Clearfield_S", "200", "100", "Clearfield","7", "10.23.0.7,", "10.23.0.7","","2007"),
                  ("200008", "Layton_N", "200", "102", "Layton","7", "10.23.0.8,", "10.23.0.8","","2008"),
                  ("200009", "Layton_S", "200", "102", "Layton","7", "10.23.0.9,", "10.23.0.9","","2009"),
                  ("200010", "Farm_N", "200", "101", "Farmington","7", "10.23.0.10,", "10.23.0.10","","2010"),
                  ("200011", "Farm_S", "200", "101", "Farmington","7", "10.23.0.11,", "10.23.0.11","","2011"),
                  ("200012", "WoodsCr_N", "200", "108", "Woods Cross","7", "10.23.0.12,", "10.23.0.12","","2012"),
                  ("200013", "WoodsCr_S", "200", "108", "Woods Cross","7", "10.23.0.13,", "10.23.0.13","","2013"),
                  ("200014", "NTemple_N", "200", "613", "North Temple","7", "10.23.0.14,", "10.23.0.14","","2014"),
                  ("200015", "NTemple_S", "200", "613", "North Temple","7", "10.23.0.15,", "10.23.0.15","","2015"),
                  ("200016", "SLCentral_NE", "200", "109", "SL Central","8", "10.23.0.16,", "10.23.0.16","","2016"),
                  ("200017", "SLCentral_SE", "200", "107", "SL Central","8", "10.23.0.17","","","","2017"),
                  ("200018", "SLCentral_SW", "200", "107", "SL Central","8", "10.23.0.18","","","","2018"),
                  ("200019", "SLCentral_N", "200", "107", "Salt Lake Central","5", "10.23.0.19","","","","2019"),
                  ("200020", "SLCentral_W", "200", "109", "Salt Lake Central","5", "10.23.0.20","","","","2020"),
                  ("200021", "OldGreek_E", "200", "111", "Old Greek Town","5", "10.23.0.21","","","","2021"),
                  ("200022", "Planet_N", "200", "110", "Planetarium","5", "10.23.0.22","","","","2022"),
                  ("200023", "Planet_S", "200", "110", "Planetarium","5", "10.23.0.23","","","","2023"),
                  ("200024", "Arena_E", "200", "120", "Arena","5", "10.23.0.24","","","","2024"),
                  ("200025", "Arena_EE", "200", "120", "Arena","5", "10.23.0.25","","","","2025"),
                  ("200026", "TempleSq_E", "200", "121", "Temple Square","5", "10.23.0.26","","","","2026"),
                  ("200027", "TempleSq_W", "200", "121", "Temple Square","5", "10.23.0.27","","","","2027"),
                  ("200028", "CityCtr_N", "200", "122", "City Center","5", "10.23.0.28","","","","2028"),
                  ("200029", "CityCtr_N", "200", "122", "City Center","5", "10.23.0.29","","","","2029"),
                  ("200030", "CityCtr_S", "200", "122", "City Center","5", "10.23.0.30","","","","2030"),
                  ("200031", "CityCtr_S", "200", "122", "City Center","5", "10.23.0.31","","","","2031"),
                  ("200032", "Gallivan_S", "200", "123", "Gallivan","5", "10.23.0.32","","","","2032"),
                  ("200033", "Gallivan_N", "200", "123", "Gallivan","5", "10.23.0.33","","","","2033"),
                  ("200034", "UMedCtr_NE", "200", "132", "U Medical Center","9", "10.23.0.34","","","","2034"),
                  ("200035", "UMedCtr_SE", "200", "132", "U Medical Center","9", "10.23.0.35","","","","2035"),
                  ("200036", "FtDouglas_N", "200", "606", "Fort Douglas","9", "10.23.0.36","","","","2036"),
                  ("200037", "SoCampus_E", "200", "605", "South Campus","9", "10.23.0.37","","","","2037"),
                  ("200038", "Stadium_NE", "200", "604", "Stadium","9", "10.23.0.38","","","","2038"),
                  ("200039", "Stadium_NW", "200", "604", "Stadium","9", "10.23.0.39","","","","2039"),
                  ("200040", "Stadium_SW", "200", "604", "Stadium","9", "10.23.0.40","","","","2040"),
                  ("200041", "900E_E", "200", "603", "900 East","9", "10.23.0.41","","","","2041"),
                  ("200042", "Trolley_E", "200", "602", "Trolley","9", "10.23.0.42","","","","2042"),
                  ("200043", "Trolley_W", "200", "602", "Trolley","9", "10.23.0.43","","","","2043"),
                  ("200044", "Library_W", "200", "601", "Library","9", "10.23.0.44","","","","2044"),
                  ("200045", "NTempleG_W", "200", "425", "N Temple/Guadalupe","10", "10.23.0.45","","","","2045"),
                  ("200046", "NTempleG_E", "200", "425", "N Temple/Guadalupe","10", "10.23.0.46","","","","2046"),
                  ("200047", "NTempleG_N", "200", "425", "N Temple/Guadalupe","10", "10.23.0.47","","","","2047"),
                  ("200048", "JksnEcld_W", "200", "424", "Jackson/Euclid","10", "10.23.0.48","","","","2048"),
                  ("200049", "JksnEcld_E", "200", "424", "Jackson/Euclid","10", "10.23.0.49","","","","2049"),
                  ("200050", "Fairpark_E", "200", "423", "Fairpark","10", "10.23.0.50","","","","2050"),
                  ("200051", "Power_W", "200", "422", "Power","10", "10.23.0.51","","","","2051"),
                  ("200052", "Power_E", "200", "422", "Power","10", "10.23.0.52","","","","2052"),
                  ("200053", "1940w_W", "200", "421", "1940 W","10", "10.23.0.53","","","","2053"),
                  ("200054", "1940w_E", "200", "421", "1940 W","10", "10.23.0.54","","","","2054"),
                  ("200055", "Airport_W", "200", "420", "Airport","10", "10.23.0.55","","","","2055"),
                  ("200056", "Airport_N", "200", "420", "Airport","10", "10.23.0.56","","","","2056"),
                  ("200057", "Airport_S", "200", "420", "Airport","10", "10.23.0.57","","","","2057"),
                  ("200058", "Court_N", "200", "124", "Court House","5", "10.23.0.58","","","","2058"),
                  ("200059", "Court_S", "200", "124", "Court House","5", "10.23.0.59","","","","2059"),
                  ("200060", "600S_N", "200", "615", "600 South","5", "10.23.0.60","","","","2060"),
                  ("200061", "600S_S", "200", "615", "600 South","5", "10.23.0.61","","","","2061"),
                  ("200062", "900So_N", "200", "112", "900 South","5", "10.23.0.62","","","","2062"),
                  ("200063", "900So_S", "200", "112", "900 South","5", "10.23.0.63","","","","2063"),
                  ("200064", "BallPark_N", "200", "113", "Ball Park","5", "10.23.0.64","","","","2064"),
                  ("200065", "BallPark_S", "200", "113", "Ball Park","5", "10.23.0.65","","","","2065"),
                  ("200066", "BallPark_S", "200", "113", "Ball Park","5", "10.23.0.66","","","","2066"),
                  ("200067", "CentralPt_N", "200", "114", "Central Pointe","5", "10.23.0.67","","","","2067"),
                  ("200068", "CentralPt_S", "200", "114", "Central Pointe","5", "10.23.0.68","","","","2068"),
                  ("200069", "SC_CntrPntl", "200", "201", "Central Pointe","11", "10.23.0.69","","","","2069"),
                  ("200070", "SC_StatSt", "200", "202", "South Salt Lake City","11", "10.23.0.70","","","","2070"),
                  ("200071", "SC_300E", "200", "203", "300 East","11", "10.23.0.71","","","","2071"),
                  ("200072", "SC_500E_N", "200", "204", "500 East","11", "10.23.0.72","","","","2072"),
                  ("200073", "SC_700E", "200", "205", "700 East","11", "10.23.0.73","","","","2073"),
                  ("200074", "SC_900E", "200", "206", "Sugarmont (900 East)","11", "10.23.0.74","","","","2074"),
                  ("200075", "SC_1045E_N", "200", "207", "Fairmont (1040 E)","11", "10.23.0.75","","","","2075"),
                  ("200076", "RiverTrl_NE", "200", "400", "River Trail","3", "10.23.0.76","","","","2076"),
                  ("200077", "RiverTrl_SW", "200", "400", "River Trail","3", "10.23.0.77","","","","2077"),
                  ("200078", "RdwdJnct_NE", "200", "401", "Redwood Jnct","3", "10.23.0.78","","","","2078"),
                  ("200079", "RdwdJnct_SW", "200", "401", "Redwood Jnct","3", "10.23.0.79","","","","2079"),
                  ("200080", "DeckerLk_NE", "200", "402", "Decker Lake","3", "10.23.0.80","","","","2080"),
                  ("200081", "DeckerLk_SW", "200", "402", "Decker Lake","3", "10.23.0.81","","","","2081"),
                  ("200082", "WVCntrl_NE", "200", "403", "West Valley","3", "10.23.0.82","","","","2082"),
                  ("200083", "WVCntrl_SE", "200", "403", "West Valley","3", "10.23.0.83","","","","2083"),
                  ("200084", "WVCntrl_NW", "200", "403", "West Valley","3", "10.23.0.84","","","","2084"),
                  ("200085", "WVCntrl_SW", "200", "403", "West Valley","3", "10.23.0.85","","","","2085"),
                  ("200086", "Millcreek_N", "200", "115", "Millcreek","5", "10.23.0.86","","","","2086"),
                  ("200087", "Millcreek_S", "200", "115", "Millcreek","5", "10.23.0.87","","","","2087"),
                  ("200088", "Meadowbr_N", "200", "116", "Meadowbrook","5", "10.23.0.88","","","","2088"),
                  ("200089", "Meadowbr_S", "200", "116", "Meadowbrook","5", "10.23.0.89","","","","2089"),
                  ("200090", "MurrayNo_N", "200", "117", "Murray North","6", "10.23.0.90","","","","2090"),
                  ("200091", "MurrayNo_S", "200", "117", "Murray North","6", "10.23.0.91","","","","2091"),
                  ("200092", "MurrayCtrl_S", "200", "118", "Murray Central","6", "10.23.0.92","","","","2092"),
                  ("200093", "MurrayCtrl_N", "200", "607", "Murray Central","6", "10.23.0.93","","","","2093"),
                  ("200094", "Murray_N", "200", "607", "Murray Central","8", "10.23.0.94","","","","2094"),
                  ("200095", "Murray_S", "200", "118", "Murray Central","8", "10.23.0.95","","","","2095"),
                  ("200096", "FPWMJ_NE", "200", "301", "Fashion Place","4", "10.23.0.96","","","","2096"),
                  ("200097", "FPWMJ_SW", "200", "301", "Fashion Place","4", "10.23.0.97","","","","2097"),
                  ("200098", "FashionPl_N", "200", "119", "Fashion Place","6", "10.23.0.98","","","","2098"),
                  ("200099", "FashionPl_S", "200", "119", "Fashion Place","6", "10.23.0.99","","","","2099"),
                  ("200100", "BngJnct_NE", "200", "302", "Bingham Jnct","4", "10.23.0.100","","","","2100"),
                  ("200101", "BngJnct_SW", "200", "302", "Bingham Jnct","4", "10.23.0.101","","","","2101"),
                  ("200102", "HGardner_NE", "200", "303", "Historic Gardner","4", "10.23.0.102","","","","2102"),
                  ("200103", "HGardner_SW", "200", "303", "Historic Gardner","4", "10.23.0.103","","","","2103"),
                  ("200104", "WJCtyCtr_NE", "200", "304", "W Jordan City Ctr","4", "10.23.0.104","","","","2104"),
                  ("200105", "WJCtyCtr_SW", "200", "304", "W Jordan City Ctr","4", "10.23.0.105","","","","2105"),
                  ("200106", "2700W_NE", "200", "305", "2700 W","4", "10.23.0.106","","","","2106"),
                  ("200107", "2700W_SW", "200", "305", "2700 W","4", "10.23.0.107","","","","2107"),
                  ("200108", "JordanVly_NE", "200", "306", "Jordan Valley","4", "10.23.0.108","","","","2108"),
                  ("200109", "JordanVly_SW", "200", "306", "Jordan Valley","4", "10.23.0.109","","","","2109"),
                  ("200110", "4773W_NE", "200", "307", "4773 W","4", "10.23.0.110","","","","2110"),
                  ("200111", "4773W_SW", "200", "307", "4773 W","4", "10.23.0.111","","","","2111"),
                  ("200112", "5651W_NE", "200", "308", "5651 W","4", "10.23.0.112","","","","2112"),
                  ("200113", "5651W_SW", "200", "308", "5651 W","4", "10.23.0.113","","","","2113"),
                  ("200114", "SJPkwy_NE", "200", "309", "So Jordan Pkwy","4", "10.23.0.114","","","","2114"),
                  ("200115", "SJPkwy_SW", "200", "309", "So Jordan Pkwy","4", "10.23.0.115","","","","2115"),
                  ("200116", "DbrkPkwy_NW", "200", "310", "Daybreak Pkwy","4", "10.23.0.116","","","","2116"),
                  ("200117", "DbrkPkwy_SW", "200", "310", "Daybreak Pkwy","4", "10.23.0.117","","","","2117"),
                  ("200118", "FtUnion_N", "200", "127", "Fort Union","6", "10.23.0.118","","","","2118"),
                  ("200119", "FtUnion_S", "200", "127", "Fort Union","6", "10.23.0.119","","","","2119"),
                  ("200120", "MidvaleCtr_N", "200", "128", "Midvale Center","6", "10.23.0.120","","","","2120"),
                  ("200121", "MidvaleCtr_S", "200", "128", "Midvale Center","6", "10.23.0.121","","","","2121"),
                  ("200122", "HSandy_N", "200", "129", "Historic Sandy","6", "10.23.0.122","","","","2122"),
                  ("200123", "HSandy_S", "200", "129", "Historic Sandy","6", "10.23.0.123","","","","2123"),
                  ("200124", "SandyExpo_N", "200", "125", "Sandy Expo","6", "10.23.0.124","","","","2124"),
                  ("200125", "SandyExpo_SW", "200", "125", "Sandy Expo","6", "10.23.0.125","","","","2125"),
                  ("200126", "SandyCvc_S", "200", "130", "Sandy Civic","6", "10.23.0.126","","","","2126"),
                  ("200127", "SandyCvc_N", "200", "130", "Sandy Civic","6", "10.23.0.127","","","","2127"),
                  ("200128", "CresentView_N", "200", "140", "Crescent View","6", "10.23.0.128","","","","2128"),
                  ("200129", "CresentView_S", "200", "140", "Crescent View","6", "10.23.0.129","","","","2129"),
                  ("200130", "KimballsLn_N", "200", "141", "Kimballs Lane","6", "10.23.0.130","","","","2130"),
                  ("200131", "KimballsLn_S", "200", "141", "Kimballs Lane","6", "10.23.0.131","","","","2131"),
                  ("200132", "DraperTC_N", "200", "142", "Draper Town Center","6", "10.23.0.132","","","","2132"),
                  ("200133", "DraperTC_S", "200", "142", "Draper Town Center","6", "10.23.0.133","","","","2133"),
                  ("200134", "Jordan_N", "200", "614", "South Jordan","8", "10.23.0.134","","","","2134"),
                  ("200135", "Jordan_S", "200", "614", "South Jordan","8", "10.23.0.135","","","","2135"),
                  ("200136", "Draper_N", "200", "199", "Draper Station","8", "10.23.0.136","","","","2136"),
                  ("200137", "Draper_S", "200", "199", "Draper Station ","8", "10.23.0.137","","","","2137"),
                  ("200138", "Lehi_N", "200", "608", "Lehi","8", "10.23.0.138","","","","2138"),
                  ("200139", "Lehi_S", "200", "608", "Lehi","8", "10.23.0.139","","","","2139"),
                  ("200140", "AmFork_N", "200", "609", "American Fork","8", "10.23.0.140","","","","2140"),
                  ("200141", "AmFork_S", "200", "609", "American Fork","8", "10.23.0.141","","","","2141"),
                  ("200142", "Vineyard_N", "200", "612", "Vineyard","8", "10.23.0.142","","","","2142"),
                  ("200143", "Vineyard_S", "200", "612", "Vineyard","8", "10.23.0.143","","","","2143"),
                  ("200144", "Orem_N", "200", "610", "Orem","8", "10.23.0.144","","","","2144"),
                  ("200145", "Orem_S", "200", "610", "Orem","8", "10.23.0.145","","","","2145"),
                  ("200146", "Provo_NE", "200", "611", "Provo","8", "10.23.0.146","","","","2146"),
                  ("200147", "Provo_NW", "200", "611", "Provo","8", "10.23.0.147","","","","2147"),
                  ("200148", "Provo_SE", "200", "611", "Provo","8", "10.23.0.148","","","","2148"),
                  ("200149", "Provo_SW", "200", "611", "Provo","8", "10.23.0.149","","","","2149"), ]
        try:
            for item in List_1:
                for item_2 in List_2:
                    if item[3].lower() == item_2[1].lower():
                        print(f"{item_2[0]},{item_2[1]},{item_2[2]},{item_2[3]},{item_2[4]},{item_2[5]},{item[6]},,{item[9]},{item[7]},{item_2[9]}")
                        break
                    elif item[3].lower() != item_2[1].lower():
                        pass
        except Exception as e:
            print(e)
            pass
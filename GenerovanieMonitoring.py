#import kniznic
from opcua import ua, Server
from time import sleep
import random
#pomocne premene
p=0
i=1
j=1
#stavy zariadeni
stav=True
stav2=False
#premene pre zapnutie alebo vypnutie generatovor
GenerujTHT2="THT2"
GenerujUPS="UPS"
GenerujAC="AC"
GenerujEM="EM"

if __name__ == "__main__":
    """
    OPC-UA-Server Setup
    """
    server=Server()

    endpoint = "opc.tcp://127.0.0.1:4848"
    server.set_endpoint(endpoint)

    servername= "Python-OPC-UA-Server"
    server.set_server_name(servername)

    """
    OPC-UA-Modeling
    """
    root_node = server.get_root_node()
    object_node = server.get_objects_node()
    idx=server.register_namespace("OPCUA_SERVER")
    myobj=object_node.add_object(idx, "Variables")

    print("Root node ID                             : " , root_node)
    print("Object node ID                           : " , object_node)
    print("Name Space and ID of Variable Object     : " , myobj)

    """
    OPC-UA-Server Add Variable
    """
    class THT2:
        def __init__(self, name, teplota, vlhkost, rosnyBod):
            self.name = name
            self.teplota = teplota
            self.vlhkost = vlhkost
            self.rosnyBod = rosnyBod

    class UPS:
        def __init__(self, name, teplota, kapacita):
            self.name = name
            self.teplota = teplota
            self.kapacita = kapacita
    
    class AC:
        def __init__(self, name, unitOperationgState, fanSpeed, returnAirTemperature, todayMaxAirTemp, todayMinAirTemp, energyConsuption):
            self.name = name
            self.neviem = unitOperationgState
            self.rychlostVerrakov = fanSpeed
            self.teplotaVracajucehoVzduchu = returnAirTemperature
            self.maxTeplotaDnes = todayMaxAirTemp
            self.minTeplotaDnes = todayMinAirTemp
            self.spotrebaEl = energyConsuption

    class EM:
        def __init__(self, name, currentVoltageL1, currentVoltageL2, currentVoltageL3, currentConsuption):
            self.name = name
            self.napatieL1 = currentVoltageL1
            self.napatieL2 = currentVoltageL2
            self.napatieL3 = currentVoltageL3
            self.spotreba = currentConsuption

    if GenerujTHT2=="THT2":
        THT2_108 = THT2("THT2_108", round(random.uniform(20, 30), 1), round(random.uniform(65, 70), 1), round(random.uniform(40, 45), 1))
        THT3_109 = THT2("THT3_109", round(random.uniform(20, 30), 1), round(random.uniform(65, 70), 1), round(random.uniform(40, 45), 1))
        THT4_109 = THT2("THT4_109", round(random.uniform(20, 30), 1), round(random.uniform(65, 70), 1), round(random.uniform(40, 45), 1))
        THT5_102 = THT2("THT5_102", round(random.uniform(20, 30), 1), round(random.uniform(65, 70), 1), round(random.uniform(40, 45), 1))
        THT1_206_1 = THT2("THT1_206_1", round(random.uniform(20, 30), 1), round(random.uniform(65, 70), 1), round(random.uniform(40, 45), 1))
        THT1_206_2 = THT2("THT1_206_2", round(random.uniform(20, 30), 1), round(random.uniform(65, 70), 1), round(random.uniform(40, 45), 1))
        THT1_206_3 = THT2("THT1_206_3", round(random.uniform(20, 30), 1), round(random.uniform(65, 70), 1), round(random.uniform(40, 45), 1))
        THT1_206_4 = THT2("THT1_206_4", round(random.uniform(20, 30), 1), round(random.uniform(65, 70), 1), round(random.uniform(40, 45), 1))
        THT1_206_5 = THT2("THT1_206_5", round(random.uniform(20, 30), 1), round(random.uniform(65, 70), 1), round(random.uniform(40, 45), 1))
        THT1_206_6 = THT2("THT1_206_6", round(random.uniform(20, 30), 1), round(random.uniform(65, 70), 1), round(random.uniform(40, 45), 1))
        THT1_206_7 = THT2("THT1_206_7", round(random.uniform(20, 30), 1), round(random.uniform(65, 70), 1), round(random.uniform(40, 45), 1))
        THT1_206_8 = THT2("THT1_206_8", round(random.uniform(20, 30), 1), round(random.uniform(65, 70), 1), round(random.uniform(40, 45), 1))
        THT1_206_9 = THT2("THT1_206_9", round(random.uniform(20, 30), 1), round(random.uniform(65, 70), 1), round(random.uniform(40, 45), 1))
        THT1_201B = THT2("THT1_201B", round(random.uniform(20, 30), 1), round(random.uniform(65, 70), 1), round(random.uniform(40, 45), 1))
        THT1_205A = THT2("THT1_205A", round(random.uniform(20, 30), 1), round(random.uniform(65, 70), 1), round(random.uniform(40, 45), 1))

        THT2_108_t = myobj.add_variable(idx, "Teplota THT2_108",0,ua.VariantType.Float)
        THT2_108_v = myobj.add_variable(idx, "Vlhkost THT2_108",0,ua.VariantType.Float)
        THT2_108_r = myobj.add_variable(idx, "Rosny bod THT2_108",0,ua.VariantType.Float)

        THT3_109_t= myobj.add_variable(idx, "Teplota THT3_109",0,ua.VariantType.Float)
        THT3_109_v= myobj.add_variable(idx, "Vlhkost THT3_109",0,ua.VariantType.Float)
        THT3_109_r= myobj.add_variable(idx, "Rosny bod THT3_109",0,ua.VariantType.Float)

        THT4_109_t= myobj.add_variable(idx, "Teplota THT4_109",0,ua.VariantType.Float)
        THT4_109_v= myobj.add_variable(idx, "Vlhkost THT4_109",0,ua.VariantType.Float)
        THT4_109_r= myobj.add_variable(idx, "Rosny bod THT4_109",0,ua.VariantType.Float)

        THT5_102_t= myobj.add_variable(idx, "Teplota THT5_102",0,ua.VariantType.Float)
        THT5_102_v= myobj.add_variable(idx, "Vlhkost THT5_102",0,ua.VariantType.Float)
        THT5_102_r= myobj.add_variable(idx, "Rosny bod THT5_102",0,ua.VariantType.Float)

        THT1_206_1_t= myobj.add_variable(idx, "Teplota THT1_206_1",0,ua.VariantType.Float)
        THT1_206_1_v= myobj.add_variable(idx, "Vlhkost THT1_206_1",0,ua.VariantType.Float)
        THT1_206_1_r= myobj.add_variable(idx, "Rosny bod THT1_206_1",0,ua.VariantType.Float)

        THT1_206_2_t= myobj.add_variable(idx, "Teplota THT1_206_2",0,ua.VariantType.Float)
        THT1_206_2_v= myobj.add_variable(idx, "Vlhkost THT1_206_2",0,ua.VariantType.Float)
        THT1_206_2_r= myobj.add_variable(idx, "Rosny bod THT1_206_2",0,ua.VariantType.Float)

        THT1_206_3_t= myobj.add_variable(idx, "Teplota THT1_206_3",0,ua.VariantType.Float)
        THT1_206_3_v= myobj.add_variable(idx, "Vlhkost THT1_206_3",0,ua.VariantType.Float)
        THT1_206_3_r= myobj.add_variable(idx, "Rosny bod THT1_206_3",0,ua.VariantType.Float)

        THT1_206_4_t= myobj.add_variable(idx, "Teplota THT1_206_4",0,ua.VariantType.Float)
        THT1_206_4_v= myobj.add_variable(idx, "Vlhkost THT1_206_4",0,ua.VariantType.Float)
        THT1_206_4_r= myobj.add_variable(idx, "Rosny bod THT1_206_4",0,ua.VariantType.Float)

        THT1_206_5_t= myobj.add_variable(idx, "Teplota THT1_206_5",0,ua.VariantType.Float)
        THT1_206_5_v= myobj.add_variable(idx, "Vlhkost THT1_206_5",0,ua.VariantType.Float)
        THT1_206_5_r= myobj.add_variable(idx, "Rosny bod THT1_206_5",0,ua.VariantType.Float)

        THT1_206_6_t= myobj.add_variable(idx, "Teplota THT1_206_6",0,ua.VariantType.Float)
        THT1_206_6_v= myobj.add_variable(idx, "Vlhkost THT1_206_6",0,ua.VariantType.Float)
        THT1_206_6_r= myobj.add_variable(idx, "Rosny bod THT1_206_6",0,ua.VariantType.Float)

        THT1_206_7_t= myobj.add_variable(idx, "Teplota THT1_206_7",0,ua.VariantType.Float)
        THT1_206_7_v= myobj.add_variable(idx, "Vlhkost THT1_206_7",0,ua.VariantType.Float)
        THT1_206_7_r= myobj.add_variable(idx, "Rosny bod THT1_206_7",0,ua.VariantType.Float)

        THT1_206_8_t= myobj.add_variable(idx, "Teplota THT1_206_8",0,ua.VariantType.Float)
        THT1_206_8_v= myobj.add_variable(idx, "Vlhkost THT1_206_8",0,ua.VariantType.Float)
        THT1_206_8_r= myobj.add_variable(idx, "Rosny bod THT1_206_8",0,ua.VariantType.Float)

        THT1_206_9_t= myobj.add_variable(idx, "Teplota THT1_206_9",0,ua.VariantType.Float)
        THT1_206_9_v= myobj.add_variable(idx, "Vlhkost THT1_206_9",0,ua.VariantType.Float)
        THT1_206_9_r= myobj.add_variable(idx, "Rosny bod THT1_206_9",0,ua.VariantType.Float)

        THT1_201B_t= myobj.add_variable(idx, "Teplota THT1_201B",0,ua.VariantType.Float)
        THT1_201B_v= myobj.add_variable(idx, "Vlhkost THT1_201B",0,ua.VariantType.Float)
        THT1_201B_r= myobj.add_variable(idx, "Rosny bod THT1_201B",0,ua.VariantType.Float)

        THT1_205A_t= myobj.add_variable(idx, "Teplota THT1_205A",0,ua.VariantType.Float)
        THT1_205A_v= myobj.add_variable(idx, "Vlhkost THT1_205A",0,ua.VariantType.Float)
        THT1_205A_r= myobj.add_variable(idx, "Rosny bod THT1_205A",0,ua.VariantType.Float)

    if GenerujUPS=="UPS":
        UPS1_201B_1 = UPS("UPS1_201B_1", round(random.uniform(20, 50), 1), round(random.uniform(20, 100), 1))
        UPS1_201B_2 = UPS("UPS1_201B_2", round(random.uniform(20, 50), 1), round(random.uniform(20, 100), 1))
        UPS1_201B_3 = UPS("UPS1_201B_3", round(random.uniform(20, 50), 1), round(random.uniform(20, 100), 1))
        UPS1_201B_4 = UPS("UPS1_201B_4", round(random.uniform(20, 50), 1), round(random.uniform(20, 100), 1))
        UPS1_201B_5 = UPS("UPS1_201B_5", round(random.uniform(20, 50), 1), round(random.uniform(20, 100), 1))
        UPS1_201B_6 = UPS("UPS1_201B_6", round(random.uniform(20, 50), 1), round(random.uniform(20, 100), 1))
        UPS1_201B_7 = UPS("UPS1_201B_7", round(random.uniform(20, 50), 1), round(random.uniform(20, 100), 1))
        UPS1_201B_8 = UPS("UPS1_201B_8", round(random.uniform(20, 50), 1), round(random.uniform(20, 100), 1))

        UPS1_201B_1_t = myobj.add_variable(idx, "Teplota UPS1_201B_1",0,ua.VariantType.Float)
        UPS1_201B_1_k = myobj.add_variable(idx, "Kapacita UPS1_201B_1",0,ua.VariantType.Float)

        UPS1_201B_2_t = myobj.add_variable(idx, "Teplota UPS1_201B_2",0,ua.VariantType.Float)
        UPS1_201B_2_k = myobj.add_variable(idx, "Kapacita UPS1_201B_2",0,ua.VariantType.Float)

        UPS1_201B_3_t = myobj.add_variable(idx, "Teplota UPS1_201B_3",0,ua.VariantType.Float)
        UPS1_201B_3_k = myobj.add_variable(idx, "Kapacita UPS1_201B_3",0,ua.VariantType.Float)

        UPS1_201B_4_t = myobj.add_variable(idx, "Teplota UPS1_201B_4",0,ua.VariantType.Float)
        UPS1_201B_4_k = myobj.add_variable(idx, "Kapacita UPS1_201B_4",0,ua.VariantType.Float)

        UPS1_201B_5_t = myobj.add_variable(idx, "Teplota UPS1_201B_5",0,ua.VariantType.Float)
        UPS1_201B_5_k = myobj.add_variable(idx, "Kapacita UPS1_201B_5",0,ua.VariantType.Float)

        UPS1_201B_6_t = myobj.add_variable(idx, "Teplota UPS1_201B_6",0,ua.VariantType.Float)
        UPS1_201B_6_k = myobj.add_variable(idx, "Kapacita UPS1_201B_6",0,ua.VariantType.Float)

        UPS1_201B_7_t = myobj.add_variable(idx, "Teplota UPS1_201B_7",0,ua.VariantType.Float)
        UPS1_201B_7_k = myobj.add_variable(idx, "Kapacita UPS1_201B_7",0,ua.VariantType.Float)

        UPS1_201B_8_t = myobj.add_variable(idx, "Teplota UPS1_201B_8",0,ua.VariantType.Float)
        UPS1_201B_8_k = myobj.add_variable(idx, "Kapacita UPS1_201B_8",0,ua.VariantType.Float)

    if GenerujAC=="AC":
        AC1_206_1 = AC("AC1_206_1", random.random(),random.randint(1000, 2000), round(random.uniform(30, 40), 1), round(random.uniform(35, 40), 1), round(random.uniform(30, 35), 1), round(random.uniform(2000, 6000), 1))
        AC1_206_2 = AC("AC1_206_2", random.random(),random.randint(1000, 2000), round(random.uniform(30, 40), 1), round(random.uniform(35, 40), 1), round(random.uniform(30, 35), 1), round(random.uniform(2000, 6000), 1))
        AC1_206_3 = AC("AC1_206_3", random.random(),random.randint(1000, 2000), round(random.uniform(30, 40), 1), round(random.uniform(35, 40), 1), round(random.uniform(30, 35), 1), round(random.uniform(2000, 6000), 1))
        AC1_206_4 = AC("AC1_206_4", random.random(),random.randint(1000, 2000), round(random.uniform(30, 40), 1), round(random.uniform(35, 40), 1), round(random.uniform(30, 35), 1), round(random.uniform(2000, 6000), 1))
        AC1_206_5 = AC("AC1_206_5", random.random(),random.randint(1000, 2000), round(random.uniform(30, 40), 1), round(random.uniform(35, 40), 1), round(random.uniform(30, 35), 1), round(random.uniform(2000, 6000), 1))
        AC1_206_6 = AC("AC1_206_6", random.random(),random.randint(1000, 2000), round(random.uniform(30, 40), 1), round(random.uniform(35, 40), 1), round(random.uniform(30, 35), 1), round(random.uniform(2000, 6000), 1))

        AC1_206_1_uos = myobj.add_variable(idx, "Stav AC1_206_1",0,ua.VariantType.Boolean)
        AC1_206_1_fs = myobj.add_variable(idx, "Otacky ventilator AC1_206_1",0,ua.VariantType.Float)
        AC1_206_1_rat = myobj.add_variable(idx, "Teplota vzduchu AC1_206_1",0,ua.VariantType.Float)
        AC1_206_1_tmaxt = myobj.add_variable(idx, "Teplota max dnes AC1_206_1",0,ua.VariantType.Float)
        AC1_206_1_tmint = myobj.add_variable(idx, "Teplota min dnes AC1_206_1",0,ua.VariantType.Float)
        AC1_206_1_ec = myobj.add_variable(idx, "Elektricka spotreba AC1_206_1",0,ua.VariantType.Float)

        AC1_206_2_uos = myobj.add_variable(idx, "Stav AC1_206_2",0,ua.VariantType.Boolean)
        AC1_206_2_fs = myobj.add_variable(idx, "Otacky ventilator AC1_206_2",0,ua.VariantType.Float)
        AC1_206_2_rat = myobj.add_variable(idx, "Teplota vzduchu AC1_206_2",0,ua.VariantType.Float)
        AC1_206_2_tmaxt = myobj.add_variable(idx, "Teplota max dnes AC1_206_2",0,ua.VariantType.Float)
        AC1_206_2_tmint = myobj.add_variable(idx, "Teplota min dnes AC1_206_2",0,ua.VariantType.Float)
        AC1_206_2_ec = myobj.add_variable(idx, "Elektricka spotreba AC1_206_2",0,ua.VariantType.Float)

        AC1_206_3_uos = myobj.add_variable(idx, "Stav AC1_206_3",0,ua.VariantType.Boolean)
        AC1_206_3_fs = myobj.add_variable(idx, "Otacky ventilator AC1_206_3",0,ua.VariantType.Float)
        AC1_206_3_rat = myobj.add_variable(idx, "Teplota vzduchu AC1_206_3",0,ua.VariantType.Float)
        AC1_206_3_tmaxt = myobj.add_variable(idx, "Teplota max dnes AC1_206_3",0,ua.VariantType.Float)
        AC1_206_3_tmint = myobj.add_variable(idx, "Teplota min dnes AC1_206_3",0,ua.VariantType.Float)
        AC1_206_3_ec = myobj.add_variable(idx, "Elektricka spotreba AC1_206_3",0,ua.VariantType.Float)

        AC1_206_4_uos = myobj.add_variable(idx, "Stav AC1_206_4",0,ua.VariantType.Boolean)
        AC1_206_4_fs = myobj.add_variable(idx, "Otacky ventilator AC1_206_4",0,ua.VariantType.Float)
        AC1_206_4_rat = myobj.add_variable(idx, "Teplota vzduchu AC1_206_4",0,ua.VariantType.Float)
        AC1_206_4_tmaxt = myobj.add_variable(idx, "Teplota max dnes AC1_206_4",0,ua.VariantType.Float)
        AC1_206_4_tmint = myobj.add_variable(idx, "Teplota min dnes AC1_206_4",0,ua.VariantType.Float)
        AC1_206_4_ec = myobj.add_variable(idx, "Elektricka spotreba AC1_206_4",0,ua.VariantType.Float)

        AC1_206_5_uos = myobj.add_variable(idx, "Stav AC1_206_5",0,ua.VariantType.Boolean)
        AC1_206_5_fs = myobj.add_variable(idx, "Otacky ventilator AC1_206_5",0,ua.VariantType.Float)
        AC1_206_5_rat = myobj.add_variable(idx, "Teplota vzduchu AC1_206_5",0,ua.VariantType.Float)
        AC1_206_5_tmaxt = myobj.add_variable(idx, "Teplota max dnes AC1_206_5",0,ua.VariantType.Float)
        AC1_206_5_tmint = myobj.add_variable(idx, "Teplota min dnes AC1_206_5",0,ua.VariantType.Float)
        AC1_206_5_ec = myobj.add_variable(idx, "Elektricka spotreba AC1_206_5",0,ua.VariantType.Float)

        AC1_206_6_uos = myobj.add_variable(idx, "Stav AC1_206_6",0,ua.VariantType.Boolean)
        AC1_206_6_fs = myobj.add_variable(idx, "Otacky ventilator AC1_206_6",0,ua.VariantType.Float)
        AC1_206_6_rat = myobj.add_variable(idx, "Teplota vzduchu AC1_206_6",0,ua.VariantType.Float)
        AC1_206_6_tmaxt = myobj.add_variable(idx, "Teplota max dnes AC1_206_6",0,ua.VariantType.Float)
        AC1_206_6_tmint = myobj.add_variable(idx, "Teplota min dnes AC1_206_6",0,ua.VariantType.Float)
        AC1_206_6_ec = myobj.add_variable(idx, "Elektricka spotreba AC1_206_6",0,ua.VariantType.Float)

    if GenerujEM=="EM":
        EM1_202_1 = EM("EM1_202_1", round(random.uniform(220, 245), 1), round(random.uniform(220, 245), 1), round(random.uniform(220, 245), 1), round(random.uniform(20000, 60000), 1))
        EM1_202_2 = EM("EM1_202_2", round(random.uniform(220, 245), 1), round(random.uniform(220, 245), 1), round(random.uniform(220, 245), 1), round(random.uniform(20000, 60000), 1))
        EM1_202_3 = EM("EM1_202_3", round(random.uniform(220, 245), 1), round(random.uniform(220, 245), 1), round(random.uniform(220, 245), 1), round(random.uniform(20000, 60000), 1))
        EM1_202_4 = EM("EM1_202_4", round(random.uniform(220, 245), 1), round(random.uniform(220, 245), 1), round(random.uniform(220, 245), 1), round(random.uniform(20000, 60000), 1))
        EM1_202_5 = EM("EM1_202_5", round(random.uniform(220, 245), 1), round(random.uniform(220, 245), 1), round(random.uniform(220, 245), 1), round(random.uniform(20000, 60000), 1))
        EM1_202_6 = EM("EM1_202_6", round(random.uniform(220, 245), 1), round(random.uniform(220, 245), 1), round(random.uniform(220, 245), 1), round(random.uniform(20000, 60000), 1))
        EM1_201B = EM("EM1_201B", round(random.uniform(220, 245), 1), round(random.uniform(220, 245), 1), round(random.uniform(220, 245), 1), round(random.uniform(20000, 60000), 1))
        
        EM1_202_1_nL1 = myobj.add_variable(idx, "Napatie L1 EM1_202_1",0,ua.VariantType.Float)
        EM1_202_1_nL2 = myobj.add_variable(idx, "Napatie L2 EM1_202_1",0,ua.VariantType.Float)
        EM1_202_1_nL3 = myobj.add_variable(idx, "Napatie L3 EM1_202_1",0,ua.VariantType.Float)
        EM1_202_1_s = myobj.add_variable(idx, "Aktualna spotreba EM1_202_1",0,ua.VariantType.Float)

        EM1_202_2_nL1 = myobj.add_variable(idx, "Napatie L1 EM1_202_2",0,ua.VariantType.Float)
        EM1_202_2_nL2 = myobj.add_variable(idx, "Napatie L2 EM1_202_2",0,ua.VariantType.Float)
        EM1_202_2_nL3 = myobj.add_variable(idx, "Napatie L3 EM1_202_2",0,ua.VariantType.Float)
        EM1_202_2_s = myobj.add_variable(idx, "Aktualna spotreba EM1_202_2",0,ua.VariantType.Float)
        
        EM1_202_3_nL1 = myobj.add_variable(idx, "Napatie L1 EM1_202_3",0,ua.VariantType.Float)
        EM1_202_3_nL2 = myobj.add_variable(idx, "Napatie L2 EM1_202_3",0,ua.VariantType.Float)
        EM1_202_3_nL3 = myobj.add_variable(idx, "Napatie L3 EM1_202_3",0,ua.VariantType.Float)
        EM1_202_3_s = myobj.add_variable(idx, "Aktualna spotreba EM1_202_3",0,ua.VariantType.Float)

        EM1_202_4_nL1 = myobj.add_variable(idx, "Napatie L1 EM1_202_4",0,ua.VariantType.Float)
        EM1_202_4_nL2 = myobj.add_variable(idx, "Napatie L2 EM1_202_4",0,ua.VariantType.Float)
        EM1_202_4_nL3 = myobj.add_variable(idx, "Napatie L3 EM1_202_4",0,ua.VariantType.Float)
        EM1_202_4_s = myobj.add_variable(idx, "Aktualna spotreba EM1_202_4",0,ua.VariantType.Float)

        EM1_202_5_nL1 = myobj.add_variable(idx, "Napatie L1 EM1_202_5",0,ua.VariantType.Float)
        EM1_202_5_nL2 = myobj.add_variable(idx, "Napatie L2 EM1_202_5",0,ua.VariantType.Float)
        EM1_202_5_nL3 = myobj.add_variable(idx, "Napatie L3 EM1_202_5",0,ua.VariantType.Float)
        EM1_202_5_s = myobj.add_variable(idx, "Aktualna spotreba EM1_202_5",0,ua.VariantType.Float)

        EM1_202_6_nL1 = myobj.add_variable(idx, "Napatie L1 EM1_202_6",0,ua.VariantType.Float)
        EM1_202_6_nL2 = myobj.add_variable(idx, "Napatie L2 EM1_202_6",0,ua.VariantType.Float)
        EM1_202_6_nL3 = myobj.add_variable(idx, "Napatie L3 EM1_202_6",0,ua.VariantType.Float)
        EM1_202_6_s = myobj.add_variable(idx, "Aktualna spotreba EM1_202_6",0,ua.VariantType.Float)

        EM1_201B_nL1 = myobj.add_variable(idx, "Napatie L1 EM1_201B",0,ua.VariantType.Float)
        EM1_201B_nL2 = myobj.add_variable(idx, "Napatie L2 EM1_201B",0,ua.VariantType.Float)
        EM1_201B_nL3 = myobj.add_variable(idx, "Napatie L3 EM1_201B",0,ua.VariantType.Float)
        EM1_201B_s = myobj.add_variable(idx, "Aktualna spotreba EM1_201B",0,ua.VariantType.Float)

    """
    OPC-UA-Server Start
    """
    server.start()

    try:
        while 1:
            if GenerujTHT2=="THT2":

                THT2_108_t.set_value(THT2_108.teplota*i,ua.VariantType.Float)
                THT2_108_v.set_value(THT2_108.vlhkost*i,ua.VariantType.Float)
                THT2_108_r.set_value(THT2_108.rosnyBod*i,ua.VariantType.Float)

                THT3_109_t.set_value(THT3_109.teplota*i,ua.VariantType.Float)
                THT3_109_v.set_value(THT3_109.vlhkost*i,ua.VariantType.Float)
                THT3_109_r.set_value(THT3_109.rosnyBod*i,ua.VariantType.Float)

                THT4_109_t.set_value(THT4_109.teplota*i,ua.VariantType.Float)
                THT4_109_v.set_value(THT4_109.vlhkost*i,ua.VariantType.Float)
                THT4_109_r.set_value(THT4_109.rosnyBod*i,ua.VariantType.Float)

                THT5_102_t.set_value(THT5_102.teplota*i,ua.VariantType.Float)
                THT5_102_v.set_value(THT5_102.vlhkost*i,ua.VariantType.Float)
                THT5_102_r.set_value(THT5_102.rosnyBod*i,ua.VariantType.Float)

                THT1_206_1_t.set_value(THT1_206_1.teplota*i,ua.VariantType.Float)
                THT1_206_1_v.set_value(THT1_206_1.vlhkost*i,ua.VariantType.Float)
                THT1_206_1_r.set_value(THT1_206_1.rosnyBod*i,ua.VariantType.Float)

                THT1_206_2_t.set_value(THT1_206_2.teplota*i,ua.VariantType.Float)
                THT1_206_2_v.set_value(THT1_206_2.vlhkost*i,ua.VariantType.Float)
                THT1_206_2_r.set_value(THT1_206_2.rosnyBod*i,ua.VariantType.Float)

                THT1_206_3_t.set_value(THT1_206_3.teplota*i,ua.VariantType.Float)
                THT1_206_3_v.set_value(THT1_206_3.vlhkost*i,ua.VariantType.Float)
                THT1_206_3_r.set_value(THT1_206_3.rosnyBod*i,ua.VariantType.Float)

                THT1_206_4_t.set_value(THT1_206_4.teplota*i,ua.VariantType.Float)
                THT1_206_4_v.set_value(THT1_206_4.vlhkost*i,ua.VariantType.Float)
                THT1_206_4_r.set_value(THT1_206_4.rosnyBod*i,ua.VariantType.Float)

                THT1_206_5_t.set_value(THT1_206_5.teplota*i,ua.VariantType.Float)
                THT1_206_5_v.set_value(THT1_206_5.vlhkost*i,ua.VariantType.Float)
                THT1_206_5_r.set_value(THT1_206_5.rosnyBod*i,ua.VariantType.Float)

                THT1_206_6_t.set_value(THT1_206_6.teplota*i,ua.VariantType.Float)
                THT1_206_6_v.set_value(THT1_206_6.vlhkost*i,ua.VariantType.Float)
                THT1_206_6_r.set_value(THT1_206_6.rosnyBod*i,ua.VariantType.Float)

                THT1_206_7_t.set_value(THT1_206_7.teplota*i,ua.VariantType.Float)
                THT1_206_7_v.set_value(THT1_206_7.vlhkost*i,ua.VariantType.Float)
                THT1_206_7_r.set_value(THT1_206_7.rosnyBod*i,ua.VariantType.Float)

                THT1_206_8_t.set_value(THT1_206_8.teplota*i,ua.VariantType.Float)
                THT1_206_8_v.set_value(THT1_206_8.vlhkost*i,ua.VariantType.Float)
                THT1_206_8_r.set_value(THT1_206_8.rosnyBod*i,ua.VariantType.Float)

                THT1_206_9_t.set_value(THT1_206_9.teplota*i,ua.VariantType.Float)
                THT1_206_9_v.set_value(THT1_206_9.vlhkost*i,ua.VariantType.Float)
                THT1_206_9_r.set_value(THT1_206_9.rosnyBod*i,ua.VariantType.Float)

                THT1_201B_t.set_value(THT1_201B.teplota*i,ua.VariantType.Float)
                THT1_201B_v.set_value(THT1_201B.vlhkost*i,ua.VariantType.Float)
                THT1_201B_r.set_value(THT1_201B.rosnyBod*i,ua.VariantType.Float)

                THT1_205A_t.set_value(THT1_205A.teplota*i,ua.VariantType.Float)
                THT1_205A_v.set_value(THT1_205A.vlhkost*i,ua.VariantType.Float)
                THT1_205A_r.set_value(THT1_205A.rosnyBod*i,ua.VariantType.Float)

            if GenerujUPS=="UPS":
                UPS1_201B_1_t.set_value(UPS1_201B_1.teplota*i,ua.VariantType.Float)
                UPS1_201B_1_k.set_value(UPS1_201B_1.kapacita*i,ua.VariantType.Float)

                UPS1_201B_2_t.set_value(UPS1_201B_2.teplota*i,ua.VariantType.Float)
                UPS1_201B_2_k.set_value(UPS1_201B_2.kapacita*i,ua.VariantType.Float)

                UPS1_201B_3_t.set_value(UPS1_201B_3.teplota*i,ua.VariantType.Float)
                UPS1_201B_3_k.set_value(UPS1_201B_3.kapacita*i,ua.VariantType.Float)

                UPS1_201B_4_t.set_value(UPS1_201B_4.teplota*i,ua.VariantType.Float)
                UPS1_201B_4_k.set_value(UPS1_201B_4.kapacita*i,ua.VariantType.Float)

                UPS1_201B_5_t.set_value(UPS1_201B_5.teplota*i,ua.VariantType.Float)
                UPS1_201B_5_k.set_value(UPS1_201B_5.kapacita*i,ua.VariantType.Float)

                UPS1_201B_6_t.set_value(UPS1_201B_6.teplota*i,ua.VariantType.Float)
                UPS1_201B_6_k.set_value(UPS1_201B_6.kapacita*i,ua.VariantType.Float)

                UPS1_201B_7_t.set_value(UPS1_201B_7.teplota*i,ua.VariantType.Float)
                UPS1_201B_7_k.set_value(UPS1_201B_7.kapacita*i,ua.VariantType.Float)

                UPS1_201B_8_t.set_value(UPS1_201B_8.teplota*i,ua.VariantType.Float)
                UPS1_201B_8_k.set_value(UPS1_201B_8.kapacita*i,ua.VariantType.Float)

            if GenerujAC=="AC":
                AC1_206_1_uos.set_value(AC1_206_1.neviem*stav,ua.VariantType.Boolean)
                AC1_206_1_fs.set_value(AC1_206_1.rychlostVerrakov*i,ua.VariantType.Float)
                AC1_206_1_rat.set_value(AC1_206_1.teplotaVracajucehoVzduchu*i,ua.VariantType.Float)
                AC1_206_1_tmaxt.set_value(AC1_206_1.maxTeplotaDnes*i,ua.VariantType.Float)
                AC1_206_1_tmint.set_value(AC1_206_1.minTeplotaDnes*i,ua.VariantType.Float)
                AC1_206_1_ec.set_value(AC1_206_1.spotrebaEl*i,ua.VariantType.Float)

                AC1_206_2_uos.set_value(AC1_206_2.neviem*stav2,ua.VariantType.Boolean)
                AC1_206_2_fs.set_value(AC1_206_2.rychlostVerrakov*i,ua.VariantType.Float)
                AC1_206_2_rat.set_value(AC1_206_2.teplotaVracajucehoVzduchu*i,ua.VariantType.Float)
                AC1_206_2_tmaxt.set_value(AC1_206_2.maxTeplotaDnes*i,ua.VariantType.Float)
                AC1_206_2_tmint.set_value(AC1_206_2.minTeplotaDnes*i,ua.VariantType.Float)
                AC1_206_2_ec.set_value(AC1_206_2.spotrebaEl*i,ua.VariantType.Float)

                AC1_206_3_uos.set_value(AC1_206_3.neviem*stav,ua.VariantType.Boolean)
                AC1_206_3_fs.set_value(AC1_206_3.rychlostVerrakov*i,ua.VariantType.Float)
                AC1_206_3_rat.set_value(AC1_206_3.teplotaVracajucehoVzduchu*i,ua.VariantType.Float)
                AC1_206_3_tmaxt.set_value(AC1_206_3.maxTeplotaDnes*i,ua.VariantType.Float)
                AC1_206_3_tmint.set_value(AC1_206_3.minTeplotaDnes*i,ua.VariantType.Float)
                AC1_206_3_ec.set_value(AC1_206_3.spotrebaEl*i,ua.VariantType.Float)

                AC1_206_4_uos.set_value(AC1_206_4.neviem*stav2,ua.VariantType.Boolean)
                AC1_206_4_fs.set_value(AC1_206_4.rychlostVerrakov*i,ua.VariantType.Float)
                AC1_206_4_rat.set_value(AC1_206_4.teplotaVracajucehoVzduchu*i,ua.VariantType.Float)
                AC1_206_4_tmaxt.set_value(AC1_206_4.maxTeplotaDnes*i,ua.VariantType.Float)
                AC1_206_4_tmint.set_value(AC1_206_4.minTeplotaDnes*i,ua.VariantType.Float)
                AC1_206_4_ec.set_value(AC1_206_4.spotrebaEl*i,ua.VariantType.Float)

                AC1_206_5_uos.set_value(AC1_206_5.neviem*stav,ua.VariantType.Boolean)
                AC1_206_5_fs.set_value(AC1_206_5.rychlostVerrakov*i,ua.VariantType.Float)
                AC1_206_5_rat.set_value(AC1_206_5.teplotaVracajucehoVzduchu*i,ua.VariantType.Float)
                AC1_206_5_tmaxt.set_value(AC1_206_5.maxTeplotaDnes*i,ua.VariantType.Float)
                AC1_206_5_tmint.set_value(AC1_206_5.minTeplotaDnes*i,ua.VariantType.Float)
                AC1_206_5_ec.set_value(AC1_206_5.spotrebaEl*i,ua.VariantType.Float)

                AC1_206_6_uos.set_value(AC1_206_6.neviem*stav2,ua.VariantType.Boolean)
                AC1_206_6_fs.set_value(AC1_206_6.rychlostVerrakov*i,ua.VariantType.Float)
                AC1_206_6_rat.set_value(AC1_206_6.teplotaVracajucehoVzduchu*i,ua.VariantType.Float)
                AC1_206_6_tmaxt.set_value(AC1_206_6.maxTeplotaDnes*i,ua.VariantType.Float)
                AC1_206_6_tmint.set_value(AC1_206_6.minTeplotaDnes*i,ua.VariantType.Float)
                AC1_206_6_ec.set_value(AC1_206_6.spotrebaEl*i,ua.VariantType.Float)

            if GenerujEM=="EM":
                EM1_202_1_nL1.set_value(EM1_202_1.napatieL1*i,ua.VariantType.Float)
                EM1_202_1_nL2.set_value(EM1_202_1.napatieL2*i,ua.VariantType.Float)
                EM1_202_1_nL3.set_value(EM1_202_1.napatieL3*i,ua.VariantType.Float)
                EM1_202_1_s.set_value(EM1_202_1.spotreba*i,ua.VariantType.Float)

                EM1_202_2_nL1.set_value(EM1_202_2.napatieL1*i,ua.VariantType.Float)
                EM1_202_2_nL2.set_value(EM1_202_2.napatieL2*i,ua.VariantType.Float)
                EM1_202_2_nL3.set_value(EM1_202_2.napatieL3*i,ua.VariantType.Float)
                EM1_202_2_s.set_value(EM1_202_2.spotreba*i,ua.VariantType.Float)

                EM1_202_3_nL1.set_value(EM1_202_3.napatieL1*i,ua.VariantType.Float)
                EM1_202_3_nL2.set_value(EM1_202_3.napatieL2*i,ua.VariantType.Float)
                EM1_202_3_nL3.set_value(EM1_202_3.napatieL3*i,ua.VariantType.Float)
                EM1_202_3_s.set_value(EM1_202_3.spotreba*i,ua.VariantType.Float)

                EM1_202_4_nL1.set_value(EM1_202_4.napatieL1*i,ua.VariantType.Float)
                EM1_202_4_nL2.set_value(EM1_202_4.napatieL2*i,ua.VariantType.Float)
                EM1_202_4_nL3.set_value(EM1_202_4.napatieL3*i,ua.VariantType.Float)
                EM1_202_4_s.set_value(EM1_202_4.spotreba*i,ua.VariantType.Float)

                EM1_202_5_nL1.set_value(EM1_202_5.napatieL1*i,ua.VariantType.Float)
                EM1_202_5_nL2.set_value(EM1_202_5.napatieL2*i,ua.VariantType.Float)
                EM1_202_5_nL3.set_value(EM1_202_5.napatieL3*i,ua.VariantType.Float)
                EM1_202_5_s.set_value(EM1_202_5.spotreba*i,ua.VariantType.Float)

                EM1_202_6_nL1.set_value(EM1_202_6.napatieL1*i,ua.VariantType.Float)
                EM1_202_6_nL2.set_value(EM1_202_6.napatieL2*i,ua.VariantType.Float)
                EM1_202_6_nL3.set_value(EM1_202_6.napatieL3*i,ua.VariantType.Float)
                EM1_202_6_s.set_value(EM1_202_6.spotreba*i,ua.VariantType.Float)

                EM1_201B_nL1.set_value(EM1_201B.napatieL1*i,ua.VariantType.Float)
                EM1_201B_nL2.set_value(EM1_201B.napatieL2*i,ua.VariantType.Float)
                EM1_201B_nL3.set_value(EM1_201B.napatieL3*i,ua.VariantType.Float)
                EM1_201B_s.set_value(EM1_201B.spotreba*i,ua.VariantType.Float)

            sleep(1)
            p=p+1
            i=i+0.025*j
            if p==80:
                j=j*(-1)
                p=0
                stav=False
                stav2=True
            else:
                stav=True
                stav2=False

    except KeyboardInterrupt:
        server.stop()
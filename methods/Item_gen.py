import random
import sys, os
sys.path.insert(0, r'C:\Users\livti\Better Shop Bot')
from methods import item_library
import discord 

def Common_Item_Gen():
    Common = [] 
    #Reading Item and Money in library
    count = 0 
    #Rand generation of COmmon Item and Mon
    while count <= 35: 
        Common += [{'name': item_library.common_item[random.randrange(0, len(item_library.common_item))], 'Gold' : item_library.common_item_price[random.randrange(0, len(item_library.common_item_price))]}]
        count += 1
    true_common = list(Common)
    return true_common 

def Uncommon_Item_Gen():
    Uncommon = [] 
    #Reading Item and Money in library
    count = 0 
    #Rand generation of COmmon Item and Mon
    while count < 42: 
        Uncommon += [{'name': item_library.uncommon_item[random.randrange(0, len(item_library.uncommon_item))], 'Gold' : item_library.uncommon_item_price[random.randrange(0, len(item_library.uncommon_item_price))]}]
        count += 1
    true_uncommon = list(Uncommon)
    return true_uncommon 

def Rare_Item_Gen():
    Rare = [] 
    #Reading Item and Money in library
    count = 0 
    #Rand generation of COmmon Item and Mon
    while count < 31: 
        Rare += [{'name': item_library.rare_item[random.randrange(0, len(item_library.rare_item))], 'Gold' : item_library.rare_item_price[random.randrange(0, len(item_library.rare_item_price))]}]
        count += 1
    true_rare = list(Rare)
    return true_rare 

def cCommon_Item_Gen():
    cCommon = [] 
    #Reading Item and Money in library
    count = 0 
    #Rand generation of COmmon Item and Mon
    while count < 53: 
        cCommon += [{'name': item_library.common_consumable[random.randrange(0, len(item_library.common_consumable))], 'Gold' : item_library.common_consumable_price[random.randrange(0, len(item_library.common_consumable_price))]}]
        count += 1
    true_ccommon = list(cCommon)
    return true_ccommon

def cUncommon_Item_Gen():
    cUncommon = [] 
    #Reading Item and Money in library
    count = 0 
    #Rand generation of COmmon Item and Mon
    while count < 46: 
        cUncommon += [{'name': item_library.uncommon_consumable[random.randrange(0, len(item_library.uncommon_consumable))], 'Gold' : item_library.uncommon_consumable_price[random.randrange(0, len(item_library.uncommon_consumable_price))]}]
        count += 1
    true_cUncommon = list(cUncommon)
    return true_cUncommon 

def cRare_Item_Gen():
    cRare = [] 
    #Reading Item and Money in library
    count = 0 
    #Rand generation of COmmon Item and Mon
    while count < 39: 
        cRare += [{'name': item_library.rare_consumable[random.randrange(0, len(item_library.rare_consumable))], 'Gold' : item_library.rare_consumable_price[random.randrange(0, len(item_library.rare_consumable_price))]}]
        count += 1
    true_cRare = list(cRare)
    return true_cRare


class Refresh: 
    def refresh(self):
        global Phauahevon_common, Phauahevon_uncommon,Phauahevon_rare, Phauahevon_ccommon, Phauahevon_cuncommon, Phauahevon_crare, Phauahevon
        global Eaqoria_common, Eaqoria_uncommon, Eaqoria_rare, Eaqoria_ccommon, Eaqoria_cuncommon, Eaqoria_rare, Eaqoria_crare, Eaqoria
        global Weastberia_common,Weastberia_cuncommon,Weastberia_crare, Weastberia_ccommon, Weastberia_rare, Weastberia_uncommon, Weastberia

        Phauahevon_common = Common_Item_Gen() 
        Phauahevon_uncommon = Uncommon_Item_Gen() 
        Phauahevon_rare = Rare_Item_Gen()
        Phauahevon_ccommon = cCommon_Item_Gen()
        Phauahevon_cuncommon = cUncommon_Item_Gen()
        Phauahevon_crare = cRare_Item_Gen()

        Eaqoria_common = Common_Item_Gen() 
        Eaqoria_uncommon = Uncommon_Item_Gen() 
        Eaqoria_rare = Rare_Item_Gen()
        Eaqoria_ccommon = cCommon_Item_Gen()
        Eaqoria_cuncommon = cUncommon_Item_Gen()
        Eaqoria_crare = cRare_Item_Gen()

        Weastberia_common = Common_Item_Gen() 
        Weastberia_uncommon = Uncommon_Item_Gen() 
        Weastberia_rare = Rare_Item_Gen()
        Weastberia_ccommon = cCommon_Item_Gen()
        Weastberia_cuncommon = cUncommon_Item_Gen()
        Weastberia_crare = cRare_Item_Gen()

        Phauahevon = shop(Phauahevon_common, Phauahevon_uncommon, Phauahevon_rare, Phauahevon_ccommon, Phauahevon_cuncommon, Phauahevon_crare)
        Weastberia = shop(Weastberia_common, Weastberia_uncommon, Weastberia_rare, Weastberia_ccommon, Weastberia_cuncommon, Weastberia_crare)
        Eaqoria = shop(Eaqoria_common, Eaqoria_uncommon, Eaqoria_rare, Eaqoria_ccommon, Eaqoria_cuncommon, Eaqoria_crare)

class shop(Refresh): 
    def __init__(self, True_Common, True_Uncommon, True_Rare, True_cCommon, True_cUncommon, True_cRare): 
        self.common_list = True_Common
        self.uncommon_list = list(True_Uncommon)
        self.rare_list = list(True_Rare)
        self.ccommon_list = list(True_cCommon)
        self.cuncommon_list = list(True_cUncommon)
        self.crare_list = list(True_cRare)

    def get_shop_list(self):
        return self.common_list, self.uncommon_list, self.rare_list, self.ccommon_list, self.cuncommon_list, self.crare_list

Phauahevon_common = Common_Item_Gen() 
Phauahevon_uncommon = Uncommon_Item_Gen() 
Phauahevon_rare = Rare_Item_Gen()
Phauahevon_ccommon = cCommon_Item_Gen()
Phauahevon_cuncommon = cUncommon_Item_Gen()
Phauahevon_crare = cRare_Item_Gen()

Eaqoria_common = Common_Item_Gen() 
Eaqoria_uncommon = Uncommon_Item_Gen() 
Eaqoria_rare = Rare_Item_Gen()
Eaqoria_ccommon = cCommon_Item_Gen()
Eaqoria_cuncommon = cUncommon_Item_Gen()
Eaqoria_crare = cRare_Item_Gen()

Weastberia_common = Common_Item_Gen() 
Weastberia_uncommon = Uncommon_Item_Gen() 
Weastberia_rare = Rare_Item_Gen()
Weastberia_ccommon = cCommon_Item_Gen()
Weastberia_cuncommon = cUncommon_Item_Gen()
Weastberia_crare = cRare_Item_Gen()

Phauahevon = shop(Phauahevon_common, Phauahevon_uncommon, Phauahevon_rare, Phauahevon_ccommon, Phauahevon_cuncommon, Phauahevon_crare)
Weastberia = shop(Weastberia_common, Weastberia_uncommon, Weastberia_rare, Weastberia_ccommon, Weastberia_cuncommon, Weastberia_crare)
Eaqoria = shop(Eaqoria_common, Eaqoria_uncommon, Eaqoria_rare, Eaqoria_ccommon, Eaqoria_cuncommon, Eaqoria_crare)

class Weastberia_items(Refresh): 
    def __init__(self): 
        #print('is inside Weast')
        #Commons embed 
        em1 = discord.Embed(title = 'Weastberia Common Shop', description= 'Page 1')
        for item in Weastberia.common_list[0:12]: 
            name = item["name"]
            price = item['Gold']
            em1.add_field(name = name, value = f"{price} gp")
        em2 = discord.Embed(title = 'Weastberia Common Shop', description= 'Page 2')
        for item in Weastberia.common_list[13:25]: 
            name = item["name"]
            price = item['Gold']
            em2.add_field(name = name, value = f"{price} gp")
        em3 = discord.Embed(title = 'Weastberia Common Shop', description= 'Page 3')
        for item in Weastberia.common_list[26:len(Weastberia_common)]: 
            name = item["name"]
            price = item['Gold']
            em3.add_field(name = name, value = f"{price} gp")
        Com_ems = [em1, em2, em3]
        self.commons = Com_ems
        #Uncommon embed 
        em1 = discord.Embed(title = 'Weastberia uncommon Shop', description= 'Page 1')
        for item in Weastberia.uncommon_list[0:12]: 
            name = item["name"]
            price = item['Gold']
            em1.add_field(name = name, value = f"{price} gp")
        em2 = discord.Embed(title = 'Weastberia uncommon Shop', description= 'Page 2')
        for item in Weastberia.uncommon_list[13:25]: 
            name = item["name"]
            price = item['Gold']
            em2.add_field(name = name, value = f"{price} gp")
        em3 = discord.Embed(title = 'Weastberia uncommon Shop', description= 'Page 2')
        for item in Weastberia.uncommon_list[26:38]: 
            name = item["name"]
            price = item['Gold']
            em2.add_field(name = name, value = f"{price} gp")
        em4 = discord.Embed(title = 'Weastberia uncommon Shop', description= 'Page 3')
        for item in Weastberia.uncommon_list[39:len(Weastberia_uncommon)]: 
            name = item["name"]
            price = item['Gold']
            em3.add_field(name = name, value = f"{price} gp")
        Uncom_ems = [em1, em2, em3, em4]
        self.uncommon = Uncom_ems
        ###Rare EMBEDS ### 
        em1 = discord.Embed(title = 'Weastberia rare Shop', description= 'Page 1')
        for item in Weastberia.rare_list[0:12]: 
            name = item["name"]
            price = item['Gold']
            em1.add_field(name = name, value = f"{price} gp")
        em2 = discord.Embed(title = 'Weastberia rare Shop', description= 'Page 2')
        for item in Weastberia.rare_list[13:25]: 
            name = item["name"]
            price = item['Gold']
            em2.add_field(name = name, value = f"{price} gp")
        em3 = discord.Embed(title = 'Weastberia rare Shop', description= 'Page 3')
        for item in Weastberia.rare_list[26:len(Weastberia_rare)]: 
            name = item["name"]
            price = item['Gold']
            em3.add_field(name = name, value = f"{price} gp")
        Rare_ems = [em1, em2, em3]
        self.rare = Rare_ems
        ###COMMON CONSUMABLES###
        em1 = discord.Embed(title = 'Weastberia common consumables Shop', description= 'Page 1')
        for item in Weastberia.ccommon_list[0:12]: 
            name = item["name"]
            price = item['Gold']
            em1.add_field(name = name, value = f"{price} gp")
        em2 = discord.Embed(title = 'Weastberia common consumables Shop', description= 'Page 2')
        for item in Weastberia.ccommon_list[13:25]: 
            name = item["name"]
            price = item['Gold']
            em2.add_field(name = name, value = f"{price} gp")
        em3 = discord.Embed(title = 'Weastberia common consumables Shop', description= 'Page 2')
        for item in Weastberia.ccommon_list[26:38]: 
            name = item["name"]
            price = item['Gold']
            em2.add_field(name = name, value = f"{price} gp")
        em4 = discord.Embed(title = 'Weastberia common consumables Shop', description= 'Page 2')
        for item in Weastberia.ccommon_list[39:50]: 
            name = item["name"]
            price = item['Gold']
            em2.add_field(name = name, value = f"{price} gp")
        em5 = discord.Embed(title = 'Weastberia common consumables Shop', description= 'Page 3')
        for item in Weastberia.ccommon_list[51:len(Weastberia_ccommon)]: 
            name = item["name"]
            price = item['Gold']
            em3.add_field(name = name, value = f"{price} gp")
        cc_ems = [em1, em2, em3, em4, em5]
        self.ccommon = cc_ems
        ### UNCOMMON CONSUMABLES ### 
        em1 = discord.Embed(title = 'Weastberia Uncommon Consumables Shop', description= 'Page 1')
        for item in Weastberia.cuncommon_list[0:12]: 
            name = item["name"]
            price = item['Gold']
            em1.add_field(name = name, value = f"{price} gp")
        em2 = discord.Embed(title = 'Weastberia Uncommon Consumables Shop', description= 'Page 2')
        for item in Weastberia.cuncommon_list[13:25]: 
            name = item["name"]
            price = item['Gold']
            em2.add_field(name = name, value = f"{price} gp")
        em3 = discord.Embed(title = 'Weastberia Uncommon Consumables Shop', description= 'Page 2')
        for item in Weastberia.cuncommon_list[26:38]: 
            name = item["name"]
            price = item['Gold']
            em2.add_field(name = name, value = f"{price} gp")
        em4 = discord.Embed(title = 'Weastberia Uncommon Consumables Shop', description= 'Page 3')
        for item in Weastberia.cuncommon_list[39:len(Weastberia_cuncommon)]: 
            name = item["name"]
            price = item['Gold']
            em3.add_field(name = name, value = f"{price} gp")
        unc_ems = [em1, em2, em3, em4]
        self.cuncommon = unc_ems
        ### RARE CONSUMABLES ### 
        em1 = discord.Embed(title = 'Weastberia Rare Consumables Shop', description= 'Page 1')
        for item in Weastberia.crare_list[0:12]: 
            name = item["name"]
            price = item['Gold']
            em1.add_field(name = name, value = f"{price} gp")
        em2 = discord.Embed(title = 'Weastberia Rare Consumables Shop', description= 'Page 2')
        for item in Weastberia.crare_list[13:25]: 
            name = item["name"]
            price = item['Gold']
            em2.add_field(name = name, value = f"{price} gp")
        em3 = discord.Embed(title = 'Weastberia Rare Consumables Shop', description= 'Page 3')
        for item in Weastberia.crare_list[26:len(Weastberia_crare)]: 
            name = item["name"]
            price = item['Gold']
            em3.add_field(name = name, value = f"{price} gp")
        rare_ems = [em1, em2, em3]
        self.crare = rare_ems 
    

class Phauahevon_items(Refresh): 
    def __init__(self): 
        ### COMMON ###
        em1 = discord.Embed(title = 'Phauahevon Common Shop', description= 'Page 1')
        for item in Phauahevon.common_list[0:12]: 
            name = item["name"]
            price = item['Gold']
            em1.add_field(name = name, value = f"{price} gp")
        em2 = discord.Embed(title = 'Phauahevon Common Shop', description= 'Page 2')
        for item in Phauahevon.common_list[13:26]: 
            name = item["name"]
            price = item['Gold']
            em2.add_field(name = name, value = f"{price} gp")
        c_ems = [em1, em2]
        self.commmon = c_ems
        ### UNCOMMON ###
        em1 = discord.Embed(title = 'Phauahevon uncommon Shop', description= 'Page 1')
        for item in Phauahevon.uncommon_list[0:12]: 
            name = item["name"]
            price = item['Gold']
            em1.add_field(name = name, value = f"{price} gp")
        em2 = discord.Embed(title = 'Phauahevon uncommon Shop', description= 'Page 2')
        for item in Phauahevon.uncommon_list[13:25]: 
            name = item["name"]
            price = item['Gold']
            em2.add_field(name = name, value = f"{price} gp")
        em3 = discord.Embed(title = 'Phauahevon uncommon Shop', description= 'Page 3')
        for item in Phauahevon.uncommon_list[26:38]: 
            name = item["name"]
            price = item['Gold']
            em3.add_field(name = name, value = f"{price} gp")
        unc_ems = [em1, em2, em3]
        self.uncommon = unc_ems
        ### RARE ### 
        em1 = discord.Embed(title = 'Phauahevon rare Shop', description= 'Page 1')
        for item in Phauahevon.rare_list[0:12]: 
            name = item["name"]
            price = item['Gold']
            em1.add_field(name = name, value = f"{price} gp")
        em2 = discord.Embed(title = 'Phauahevon rare Shop', description= 'Page 2')
        for item in Phauahevon.rare_list[13:15]: 
            name = item["name"]
            price = item['Gold']
            em2.add_field(name = name, value = f"{price} gp")
        rare_ems = [em1, em2]
        self.rare = rare_ems 
        ### COMMON CONSUMABLE ###
        em1 = discord.Embed(title = 'Phauahevon common consumables Shop', description= 'Page 1')
        for item in Phauahevon.ccommon_list[0:12]: 
            name = item["name"]
            price = item['Gold']
            em1.add_field(name = name, value = f"{price} gp")
        em2 = discord.Embed(title = 'Phauahevon common consumables Shop', description= 'Page 2')
        for item in Phauahevon.ccommon_list[13:25]: 
            name = item["name"]
            price = item['Gold']
            em2.add_field(name = name, value = f"{price} gp")
        ccom_ems = [em1, em2]
        self.ccommon = ccom_ems
        ### UNCOMMON CONSUMABLE ###
        em1 = discord.Embed(title = 'Phauahevon Uncommon Consumables Shop', description= 'Page 1')
        for item in Phauahevon.cuncommon_list[0:14]: 
            name = item["name"]
            price = item['Gold']
            em1.add_field(name = name, value = f"{price} gp")
        uncom_ems = [em1]
        self.cuncommon = uncom_ems 
        ### RARE CONSUMABLE ### 
        em1 = discord.Embed(title = 'Phauahevon Rare Consumables Shop', description= 'Page 1')
        for item in Phauahevon.crare_list[0:9]: 
            name = item["name"]
            price = item['Gold']
            em1.add_field(name = name, value = f"{price} gp")
        rare_ems = [em1]
        self.crare = rare_ems

class Eaqoria_items(Refresh): 
    def __init__(self): 
        ###COMMON### 
        em1 = discord.Embed(title = 'Eaqoria Common Shop', description= 'Page 1')
        for item in Eaqoria.common_list[0:12]: 
            name = item["name"]
            price = item['Gold']
            em1.add_field(name = name, value = f"{price} gp")
        em2 = discord.Embed(title = 'Eaqoria Common Shop', description= 'Page 2')
        for item in Eaqoria.common_list[13:18]: 
            name = item["name"]
            price = item['Gold']
            em2.add_field(name = name, value = f"{price} gp")
        com_ems = [em1, em2]
        self.common = com_ems
        ### UNCOMMON ###
        em1 = discord.Embed(title = 'Eaqoria uncommon Shop', description= 'Page 1')
        for item in Eaqoria.uncommon_list[0:12]: 
            name = item["name"]
            price = item['Gold']
            em1.add_field(name = name, value = f"{price} gp")
        em2 = discord.Embed(title = 'Eaqoria uncommon Shop', description= 'Page 2')
        for item in Eaqoria.uncommon_list[13:26]: 
            name = item["name"]
            price = item['Gold']
            em2.add_field(name = name, value = f"{price} gp")
        unc_ems = [em1, em2]
        self.uncommon = unc_ems
        ### RARE ### 
        em1 = discord.Embed(title = 'Eaqoria rare Shop', description= 'Page 1')
        for item in Eaqoria.rare_list[0:12]: 
            name = item["name"]
            price = item['Gold']
            em1.add_field(name = name, value = f"{price} gp")
        rare_ems = [em1]
        self.rare = rare_ems
        ### COMMON CONSUMABLE ###
        em1 = discord.Embed(title = 'Eaqoria common consumables Shop', description= 'Page 1')
        for item in Eaqoria.ccommon_list[0:12]: 
            name = item["name"]
            price = item['Gold']
            em1.add_field(name = name, value = f"{price} gp")
        em2 = discord.Embed(title = 'Eaqoria common consumables Shop', description= 'Page 2')
        for item in Eaqoria.ccommon_list[13:25]: 
            name = item["name"]
            price = item['Gold']
            em2.add_field(name = name, value = f"{price} gp")
        em3 = discord.Embed(title = 'Eaqoria common consumables Shop', description= 'Page 3')
        for item in Eaqoria.ccommon_list[26:32]: 
            name = item["name"]
            price = item['Gold']
            em3.add_field(name = name, value = f"{price} gp")
        cc_ems = [em1, em2, em3]
        self.ccommon = cc_ems
        ### UNCOMMON CONSUMABLE ### 
        em1 = discord.Embed(title = 'Eaqoria Uncommon Consumables Shop', description= 'Page 1')
        for item in Eaqoria.cuncommon_list[0:12]: 
            name = item["name"]
            price = item['Gold']
            em1.add_field(name = name, value = f"{price} gp")
        em2 = discord.Embed(title = 'Eaqoria Uncommon Consumables Shop', description= 'Page 2')
        for item in Eaqoria.cuncommon_list[13:27]: 
            name = item["name"]
            price = item['Gold']
            em2.add_field(name = name, value = f"{price} gp")
        cunc_ems = [em1, em2]
        self.cuncommon = cunc_ems
        ### RARE CONSUMABLE ### 
        em1 = discord.Embed(title = 'Eaqoria Rare Consumables Shop', description= 'Page 1')
        for item in Eaqoria.crare_list[0:12]: 
            name = item["name"]
            price = item['Gold']
            em1.add_field(name = name, value = f"{price} gp")
        em2 = discord.Embed(title = 'Eaqoria Rare Consumables Shop', description= 'Page 2')
        for item in Eaqoria.crare_list[13:16]: 
            name = item["name"]
            price = item['Gold']
            em2.add_field(name = name, value = f"{price} gp")
        crare_ems = [em1, em2]
        self.crare = crare_ems


we_commons = Weastberia_items() 
we_uncommon = Weastberia_items() 
we_rare = Weastberia_items()
we_ccommon = Weastberia_items()
we_cuncommon = Weastberia_items()
we_crare = Weastberia_items()

ph_common = Phauahevon_items() 
ph_uncommon = Phauahevon_items() 
ph_rare = Phauahevon_items()
ph_ccommon = Phauahevon_items()
ph_cuncommon = Phauahevon_items()
ph_crare = Phauahevon_items()

ea_common = Eaqoria_items() 
ea_uncommon = Eaqoria_items() 
ea_rare = Eaqoria_items()
ea_ccommon = Eaqoria_items()
ea_cuncommon = Eaqoria_items()
ea_crare = Eaqoria_items()


shops = ['Phauahevon', 'Weastberia', 'Eaqoria', 'phauahevon', 'weastberia', 'eaqoria', 'PHAUAHEVON', 'WEASTBERIA', 'EAQORIA']

async def buy_this(shop, gold, item_name):
    gold = str(gold)
    thing = {'name': item_name, 'Gold':gold}
    potion_of_healing ={'name': 'Potion of Healing', 'Gold': 50}
    itm_in_there = [0, 0, 0]
    if shop in shops:  
        if thing is potion_of_healing:
            itm_in_there[0] = 1
        if thing in Phauahevon.common_list: 
            indx_of_itm = Phauahevon.common_list.index(thing)
            Phauahevon.common_list.pop(indx_of_itm)
            for embe in ph_common.commmon: 
                embe.remove_field(indx_of_itm)
            itm_in_there[0] = 1
        if thing in Phauahevon.uncommon_list: 
            indx_of_itm = Phauahevon.uncommon_list.index(thing)
            Phauahevon.uncommon_list.pop(indx_of_itm)
            for embe in ph_uncommon.uncommon: 
                embe.remove_field(indx_of_itm)
            itm_in_there[0] = 1
        if thing in Phauahevon.rare_list: 
            indx_of_itm = Phauahevon.rare_list.index(thing)
            Phauahevon.rare_list.pop(indx_of_itm)
            for embe in ph_rare.rare: 
                embe.remove_field(indx_of_itm)
            itm_in_there[0] = 1
        if thing in Phauahevon.ccommon_list: 
            indx_of_itm = Phauahevon.ccommon_list.index(thing)
            Phauahevon.ccommon_list.pop(indx_of_itm)
            for embe in ph_ccommon.ccommon: 
                embe.remove_field(indx_of_itm)
            itm_in_there[0] = 1
        if thing in Phauahevon.cuncommon_list: 
            indx_of_itm = Phauahevon.cuncommon_list.index(thing)
            Phauahevon.cuncommon_list.pop(indx_of_itm)
            for embe in ph_cuncommon.cuncommon: 
                embe.remove_field(indx_of_itm)
            itm_in_there[0] = 1
        if thing in Phauahevon.crare_list: 
            indx_of_itm = Phauahevon.crare_list.index(thing)
            Phauahevon.crare_list.pop(indx_of_itm)
            for embe in ph_crare.crare: 
                embe.remove_field(indx_of_itm)
            itm_in_there[0] = 1
        if thing in Weastberia.common_list: 
            indx_of_itm = Weastberia.common_list.index(thing)
            Weastberia.common_list.pop(indx_of_itm)
            for embe in we_commons.commons: 
                embe.remove_field(indx_of_itm)
            itm_in_there[0] = 1
        if thing in Weastberia.uncommon_list: 
            indx_of_itm = Weastberia.uncommon_list.index(thing)
            Weastberia.uncommon_list.pop(indx_of_itm)
            for embe in we_uncommon.uncommon: 
                embe.remove_field(indx_of_itm)
            itm_in_there[0] = 1
        if thing in Weastberia.rare_list: 
            indx_of_itm = Weastberia.rare_list.index(thing)
            Weastberia.rare_list.pop(indx_of_itm)
            for embe in we_rare.rare: 
                embe.remove_field(indx_of_itm)
            itm_in_there[0] = 1
        if thing in Weastberia.ccommon_list: 
            indx_of_itm = Weastberia.ccommon_list.index(thing)
            Weastberia.ccommon_list.pop(indx_of_itm)
            for embe in we_ccommon.ccommon: 
                embe.remove_field(indx_of_itm)
            itm_in_there[0] = 1
        if thing in Weastberia.cuncommon_list: 
            indx_of_itm = Weastberia.cuncommon_list.index(thing)
            Weastberia.cuncommon_list.pop(indx_of_itm)
            for embe in we_cuncommon.cuncommon: 
                embe.remove_field(indx_of_itm)
            itm_in_there[0] = 1
        if thing in Weastberia.crare_list: 
            indx_of_itm = Weastberia.crare_list.index(thing)
            Weastberia.crare_list.pop(indx_of_itm)
            for embe in we_crare.crare: 
                embe.remove_field(indx_of_itm)
            itm_in_there[0] = 1
        if thing in Eaqoria.common_list: 
            indx_of_itm = Eaqoria.common_list.index(thing)
            Eaqoria.common_list.pop(indx_of_itm)
            for embe in ea_common.common: 
                embe.remove_field(indx_of_itm)
            itm_in_there[0] = 1
        if thing in Eaqoria.uncommon_list: 
            indx_of_itm = Eaqoria.uncommon_list.index(thing)
            Eaqoria.uncommon_list.pop(indx_of_itm)
            for embe in ea_uncommon.uncommon: 
                embe.remove_field(indx_of_itm)
            itm_in_there[0] = 1
        if thing in Eaqoria.rare_list: 
            indx_of_itm = Eaqoria.rare_list.index(thing)
            Eaqoria.rare_list.pop(indx_of_itm)
            for embe in ea_rare.rare: 
                embe.remove_field(indx_of_itm)
            itm_in_there[0] = 1
        if thing in Eaqoria.ccommon_list: 
            indx_of_itm = Eaqoria.ccommon_list.index(thing)
            Eaqoria.ccommon_list.pop(indx_of_itm)
            for embe in ea_ccommon.ccommon: 
                embe.remove_field(indx_of_itm)
            itm_in_there[0] = 1
        if thing in Eaqoria.cuncommon_list: 
            indx_of_itm = Eaqoria.cuncommon_list.index(thing)
            Eaqoria.cuncommon_list.pop(indx_of_itm)
            for embe in ea_cuncommon.cuncommon: 
                embe.remove_field(indx_of_itm)
            itm_in_there[0] = 1
        if thing in Eaqoria.crare_list: 
            indx_of_itm = Eaqoria.crare_list.index(thing)
            Eaqoria.crare_list.pop(indx_of_itm)
            for embe in ea_crare.crare: 
                embe.remove_field(indx_of_itm)
            itm_in_there[0] = 1
    return itm_in_there

def refresh_all_shops(): 
    Weastberia.refresh() 
    Phauahevon.refresh()
    Eaqoria.refresh() 

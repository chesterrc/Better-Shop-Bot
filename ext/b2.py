import discord
import discord.ext 
from discord.ext import commands 
from discord import ui, SelectOption 
from discord import app_commands, SelectMenu
from discord import Interaction
import sys, os
import asyncio
sys.path.insert(0, r'C:\Users\livti\Better Shop Bot')
from methods import Item_gen
#import methods.Item_gen as item_gen  



class Buttons_cog(commands.Cog):
    def __init__(self, bot): 
        self.bot = bot 
   
    @commands.Cog.listener() 
    async def on_ready(self):
        print('Buttons ready')
        print('Menu is Ready')

class shop_menu(discord.ui.View):
    def __init__(self, user):
        self.user= user 
        super().__init__(timeout=30)
    
    async def interaction_check(self, interaction: Interaction, /) -> bool:
        if interaction.user != self.user: 
            await interaction.response.send_message('Please use your own shop UI by doing /shop', ephemeral=True)
            return False
        else: 
            print("returning true")
            return True 

    #Select Menu for shops
    @discord.ui.select(max_values=1, placeholder='Choose a shop!',
    options=[
        discord.SelectOption(
            label = 'Weastberia',
            value = '1' 
        ),
        discord.SelectOption(
            label = 'Phauahevon',
            value = '2' 
        ),
        discord.SelectOption(
            label= 'Eaqoria',
            value = '3' 
        )
    ])
    async def menu_callback(self, interaction: Interaction, select: discord.ui.Select):
        val = select.values[0]
        print(val, 'passes through menu callback')
        await interaction.message.edit(view=item_menu(val, self.user))
        await interaction.response.defer() 
    
    
        
    
#Select menu for different item types 
class item(discord.ui.Select):
    def __init__(self, val, user):
        self.val = val 
        self.user = user 
        opt = [
            discord.SelectOption(label = 'Common', value = 'C'),
            discord.SelectOption(label = 'Uncommon', value = 'U'),
            discord.SelectOption(label = 'Rare', value = 'R'),
            discord.SelectOption(label = 'Common Consumables', value = 'cC'),
            discord.SelectOption(label = 'Uncommon Consumables', value = 'cU'),
            discord.SelectOption(label = 'Rare Consumables', value = 'cR'),
        ]
        super().__init__(custom_id= 'item', placeholder='Choose an item!', options=opt)
    #Setting up common, uncommon, etc. menu 

    async def callback(self, interaction: Interaction):
        #Weastberia Items 
        #common
        print('in item callback')
        if self.val == '1':
            if self.values[0] == 'C':
                ems = Item_gen.we_commons.commons
                curr_page = 0  
                await interaction.message.edit(embed=ems[curr_page], view=butt_view(ems=ems, curr_page= curr_page, user= self.user))
                await interaction.response.defer()  
        #uncommon
            elif self.values[0] == 'U':
                print('passing through second if')
                ems = Item_gen.we_uncommon.uncommon
                curr_page = 0  
                await interaction.message.edit(embed=ems[curr_page], view=butt_view(ems=ems, curr_page= curr_page, user= self.user))
                await interaction.response.defer()  
        #rare
            elif self.values[0] == 'R':
                ems = Item_gen.we_rare.rare
                curr_page = 0  
                await interaction.message.edit(embed=ems[curr_page], view=butt_view(ems=ems, curr_page= curr_page, user= self.user))
                await interaction.response.defer()  
        #common consumable 
            elif self.values[0] == 'cC':
                ems = Item_gen.we_ccommon.ccommon
                curr_page = 0  
                await interaction.message.edit(embed=ems[curr_page], view=butt_view(ems=ems, curr_page= curr_page, user= self.user))
                await interaction.response.defer()  
        #uncommon consumable
            elif self.values[0] == 'cU':
                ems = Item_gen.we_cuncommon.cuncommon
                curr_page = 0  
                await interaction.message.edit(embed=ems[curr_page], view=butt_view(ems=ems, curr_page= curr_page, user= self.user))
                await interaction.response.defer()  
        #rare consumable
            elif self.values[0] == 'cR':
                ems = Item_gen.we_crare.crare
                curr_page = 0  
                await interaction.message.edit(embed=ems[curr_page], view=butt_view(ems=ems, curr_page= curr_page, user= self.user))
                await interaction.response.defer()  
        ########################
        ### Phauahevon Items ### 
        ########################
        if self.val == '2':
            if self.values[0] == 'C':
                ems = Item_gen.ph_common.commmon
                curr_page = 0  
                await interaction.message.edit(embed=ems[curr_page], view=butt_view(ems=ems, curr_page= curr_page, user= self.user))
                await interaction.response.defer()  
        #uncommon
            elif self.values[0] == 'U':
                ems = Item_gen.ph_uncommon.uncommon
                curr_page = 0  
                await interaction.message.edit(embed=ems[curr_page], view=butt_view(ems=ems, curr_page= curr_page, user= self.user))
                await interaction.response.defer()  
        #rare
            elif self.values[0] == 'R':
                ems = Item_gen.ph_rare.rare
                curr_page = 0  
                await interaction.message.edit(embed=ems[curr_page], view=butt_view(ems=ems, curr_page= curr_page, user= self.user))
                await interaction.response.defer()  
        #common consumable 
            elif self.values[0] == 'cC':
                ems = Item_gen.ph_ccommon.ccommon
                curr_page = 0  
                await interaction.message.edit(embed=ems[curr_page], view=butt_view(ems=ems, curr_page= curr_page, user= self.user))
                await interaction.response.defer()  
        #uncommon consumable
            elif self.values[0] == 'cU':
                ems = Item_gen.ph_cuncommon.cuncommon
                curr_page = 0  
                await interaction.message.edit(embed=ems[curr_page], view=butt_view(ems=ems, curr_page= curr_page, user= self.user))
                await interaction.response.defer()  
        #rare consumable
            elif self.values[0] == 'cR':
                ems = Item_gen.ph_rare.crare
                curr_page = 0  
                await interaction.message.edit(embed=ems[curr_page], view=butt_view(ems=ems, curr_page= curr_page, user= self.user))
                await interaction.response.defer()
        ########################
        ### Eaqoria Items ### 
        ########################
        if self.val == '3':
            if self.values[0] == 'C':
                ems = Item_gen.ea_common.commmon
                curr_page = 0  
                await interaction.message.edit(embed=ems[curr_page], view=butt_view(ems=ems, curr_page= curr_page, user= self.user))
                await interaction.response.defer()  
        #uncommon
            elif self.values[0] == 'U':
                ems = Item_gen.ea_uncommon.uncommon
                curr_page = 0  
                await interaction.message.edit(embed=ems[curr_page], view=butt_view(ems=ems, curr_page= curr_page, user= self.user))
                await interaction.response.defer()  
        #rare
            elif self.values[0] == 'R':
                ems = Item_gen.ea_rare.rare
                curr_page = 0  
                await interaction.message.edit(embed=ems[curr_page], view=butt_view(ems=ems, curr_page= curr_page, user= self.user))
                await interaction.response.defer()  
        #common consumable 
            elif self.values[0] == 'cC':
                ems = Item_gen.ea_ccommon.ccommon
                curr_page = 0  
                await interaction.message.edit(embed=ems[curr_page], view=butt_view(ems=ems, curr_page= curr_page, user= self.user))
                await interaction.response.defer()  
        #uncommon consumable
            elif self.values[0] == 'cU':
                ems = Item_gen.ea_cuncommon.cuncommon
                curr_page = 0  
                await interaction.message.edit(embed=ems[curr_page], view=butt_view(ems=ems, curr_page= curr_page, user= self.user))
                await interaction.response.defer()  
        #rare consumable
            elif self.values[0] == 'cR':
                ems = Item_gen.ea_rare.crare
                curr_page = 0  
                await interaction.message.edit(embed=ems[curr_page], view=butt_view(ems=ems, curr_page= curr_page, user= self.user))
                await interaction.response.defer()        
    
class item_menu(discord.ui.View):
    def __init__(self, val, user):
        print('in item view')
        #print(f'{val} is in item_menu')
        self.user = user
        super().__init__()
        self.add_item(item(val, user=user))

    async def interaction_check(self, interaction: Interaction, /) -> bool:
        if interaction.user != self.user: 
            await interaction.response.send_message('Please use your own shop by doing /shop', ephemeral=True)
            return False
        else: 
            return True
        

#Buttons for the shop
class butt_prev(discord.ui.Button): 
    def __init__(self, ems, curr_page, user):
        self.ems = ems 
        self.curr_page = curr_page 
        self.user = user
        if self.curr_page == 0: 
            super().__init__(label = 'previous', style=discord.ButtonStyle.blurple, emoji = '◀️', disabled=True)
        else: 
            super().__init__(label = 'previous', style=discord.ButtonStyle.blurple, emoji = '◀️', disabled=False)

    async def callback(self, interaction: Interaction):
        print('in prev')
        self.curr_page -= 1
        ems = self.ems[self.curr_page] 
        await interaction.message.edit(embed=ems, view = butt_view(self.ems, self.curr_page, self.user))
        await interaction.response.defer()

class butt_next(discord.ui.Button): 
    def __init__(self, ems, curr_page, user):
        self.ems = ems 
        self.curr_page = curr_page 
        self.user = user
        print(f'{self.curr_page}')
        if self.curr_page == len(ems)-1:  
            super().__init__(label = 'next', style=discord.ButtonStyle.blurple, emoji = '▶️', disabled=True)
        else: 
            super().__init__(label = 'next', style=discord.ButtonStyle.blurple, emoji = '▶️', disabled=False)

    async def callback(self, interaction: Interaction):
        print('in butt next callback')
        self.curr_page += 1
        ems = self.ems[self.curr_page] 
        await interaction.message.edit(embed=ems, view = butt_view(self.ems, self.curr_page, self.user))
        await interaction.response.defer()

class butt_view(discord.ui.View):
    def __init__(self, ems, curr_page, user):
        self.user = user 
        print(f'{curr_page} in button view')
        super().__init__(timeout=30)
        self.add_item(butt_prev(ems, curr_page, user))
        self.add_item(butt_next(ems, curr_page, user))
    
    async def interaction_check(self, interaction: Interaction, /) -> bool:
        if interaction.user != self.user: 
            await interaction.response.send_message('Please use your own shop by doing /shop', ephemeral=True)
            return False
        else: 
            return True
        

async def setup(bot):
    await bot.add_cog(Buttons_cog(bot))


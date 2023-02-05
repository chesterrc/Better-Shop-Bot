import discord, asyncio, json
from discord import Interaction
from discord import app_commands
from discord.ext import commands
from discord import ui 
import os  
import ext.b2 
import asyncio
import typing   
from methods import Item_gen 

intents = discord.Intents.all() 
intents.members = True 
bot = commands.Bot(command_prefix="$", intents= discord.Intents.all(), help_command=None)

with open('token.txt') as f: 
    TOKEN = f.read() 

@bot.event 
async def on_ready(): 
    print('Bot is ready')
    try: 
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e: 
        print(e)

@bot.command
async def ping(ctx):
    await ctx.send('hello')

@bot.tree.command(name = 'help')
async def help(interaction: Interaction): 
    embed = discord.Embed(title = 'Help', description='For The Shop')
    embed.add_field(name='/help', value='Shows commands you could use!')
    embed.add_field(name='/shops', value='Brings out the shop menu')
    embed.add_field(name='/buy', value='Buys things!')
    await interaction.response.send_message(embed=embed)
 
 ### SHOP COMMAND ###
@bot.tree.command(name = 'shops')
async def shop(interaction: Interaction):
    #print('Passes through main bot tree')
    View = ext.b2.shop_menu(interaction.user)
    await interaction.response.send_message(view=View) 

###BUY COMMAND###
@bot.tree.command(name = 'buy')
async def buy(interaction: Interaction, shop: str, gold: str, item_name: str):
    res = await Item_gen.buy_this(shop, gold, item_name)
    
    if res[0] == 0: 
        await interaction.response.send_message("Please check that the item is listed or has the correct amount of gold.")
    elif res[0] == 1: 
        await interaction.response.send_message(f"{interaction.user.mention} just bought {item_name} from {shop} for {gold}gp")

@bot.tree.command(name = 'refresh')
@commands.has_role('Data Team')
async def refresh(interaction: Interaction): 
    Item_gen.refresh_all_shops()
    await interaction.response.send_message('Refreshed!') 

async def load():
    for file in os.listdir('./ext'):
        if file.endswith('.py'):
            await bot.load_extension(f'ext.{file[:-3]}')

async def main():
    await load()
    await bot.start(TOKEN)

asyncio.run(main())
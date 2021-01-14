# src/bot.py
import os
import helper
import discord
from discord.ext import commands
import aiosqlite
#Start loading stuff
helper.imports() #Imports deps
helper.setallenv() #Creates variable for token and prefix

if not os.path.exists(r"db/astronomer.db"):
    open(r"src/db/astronomer.db", 'w').close()
    
db = await aiosqlite.connect("db/astronomer.db")

bot = commands.Bot(command_prefix=os.getenv("DISCORD_BOT_PREFIX"))

@bot.event
async def on_ready():
	print("Astronomer/src/bot.py] Dash is online")
	print("[Astronomer/src/bot.py:Status] Setting status")
	await bot.change_presence(
	    activity=discord.Game(os.getenv("DISCORD_BOT_PREFIX") + "help for help"))
	print(":Status] Status set")

bot.run(os.getenv("DISCORD_TOKEN"))
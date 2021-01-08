# src/bot.py
import os
import helper
import discord
from discord.ext import commands
#Start loading stuff
helper.imports() #Imports deps
helper.setallenv() #Creates variable for token and prefix

bot = commands.Bot(command_prefix=os.getenv("DISCORD_BOT_PREFIX"))

@bot.event
async def on_ready():
	print("Astronomer/src/bot.py] Dash is online")
	print("[Astronomer/src/bot.py:Status] Setting status")
	await bot.change_presence(
	    activity=discord.Game(os.getenv("DISCORD_BOT_PREFIX") + "help for help"))
	print(__main__ + ":Status] Status set")

bot.run(os.getenv("DISCORD_TOKEN"))
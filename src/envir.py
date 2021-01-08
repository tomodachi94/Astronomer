def imports():
  import os
  from dotenv import load_dotenv

def setallenv():
  import os
  from dotenv import load_dotenv
  DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
  DISCORD_BOT_PREFIX = os.getenv("DISCORD_BOT_PREFIX")

def update():
  os.system("git pull")
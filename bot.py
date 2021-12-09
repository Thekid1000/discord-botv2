import nextcord
from nextcord.ext import commands
import json


settings_file = open("./config/settings.json")

config = json.load(settings_file)





bot  =  commands.Bot(command_prefix=config["prefix"])

@bot.event
async def on_ready():
  print("Bot is ready")


@bot.command()
async def hi(ctx):
  await ctx.send("hi user")


bot.run(config["token"])













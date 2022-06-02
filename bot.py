import asyncio
from http import client
import discord
from discord.ext import commands

TOKEN = "OTgwNzk5NDY1MDk3MTYyNzgy.Gz5aWe.pwsvj1FbnR5e2NaXq58TxwLXBk3ZkqVB0VVANE"
PREFIX = "!"
bot = commands.Bot(command_prefix=PREFIX)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    bot.loop.create_task(status_task())

async def status_task():
    while True:
        await bot.change_presence(activity=discord.Game('Destiny 2'), status=discord.Status.online)
        await asyncio.sleep(10)
        await bot.change_presence(activity=discord.Game('Official Elderal Bot'), status=discord.Status.online)
        await asyncio.sleep(10)

bot.run(TOKEN)
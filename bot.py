import asyncio
from http import client
import discord

TOKEN = "OTgwNzk5NDY1MDk3MTYyNzgy.Gz5aWe.pwsvj1FbnR5e2NaXq58TxwLXBk3ZkqVB0VVANE"
client = discord.Client()

@client.event
async def on_ready():
    print(f'Eingeloggt als User {client.user.name}')
    client.loop.create_task(status_task())

async def status_task():
    while True:
        await client.change_presence(activity=discord.Game('Destiny 2'), status=discord.Status.online)
        await asyncio.sleep(20)
        await client.change_presence(activity=discord.Game('Official Elderal Bot'), status=discord.Status.online)
        await asyncio.sleep(20)



client.run(TOKEN)
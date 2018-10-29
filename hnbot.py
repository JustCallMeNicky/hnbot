import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
from discord import Game


Client = discord.client
client = commands.Bot(command_prefix = '!')
Clientdiscord = discord.Client()


@client.event
async def on_ready():
    await client.change_presence(game=Game(name='For !commands', type = 3))
    print('Ready, Freddy') 


@client.event
async def on_message(message):
    if message.content == '!bot':
        await client.send_message(message.channel,'Created By JustCallMeNicky')
client.run('NTA2MzQ1MTQxMzIyMTIxMjE3.Drg6Yg.Q5_SK2Sb-bHZMegQVvpAM-eYwaU')

import os
import discord

from beluwga_functions import *

DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$'):
        kerdes = message.content.split('$')[1].lower()
        valasz = valaszol(kerdes)
        await message.channel.send(valasz)
    
    if client.user.mentioned_in(message):
        await message.channel.send('Hozzám szólsz?')


client.run(DISCORD_TOKEN)

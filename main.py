import discord
import os, random

DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

valaszok = {
    "szia": [
        "szia",
        "hi",
        "hello",
        "szeva"
    ],
    "hogy vagy?": [
        "Jól",
        "Nem jól",
        "Egész jól"
    ],
    "hány óra van?": "Nem tudom.",
    "$ko_papir_ollo":
      [
        "kő",
        "papír",
        "olló"
      ]
}

def ko_papir_ollo(kerdes):
  valasz = valaszok['$ko_papir_ollo'][random.randint(0, 2)]
  return valasz

def valaszol(kerdes):
  if kerdes == "kő" or kerdes == "papír" or kerdes == "olló":
    valasz = ko_papir_ollo(kerdes)
  elif kerdes in list(valaszok.keys()):
    if isinstance(valaszok[kerdes], str):
      valasz = valaszok[kerdes]
    else:
      valasz = valaszok[kerdes][random.randint(0, len(valaszok[kerdes]) -1)]
  else:
    valasz = "Erre nem tudok valaszolni."
  return valasz


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


client.run(os.getenv('DISCORD_TOKEN'))

import discord
import os, random

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
    ]
}

def valaszol(kerdes):
  if kerdes in list(valaszok(keys)):
    if isinstance(valaszok[kerdes], str):
      valasz = valaszok[kerdes]
    else:
      valasz = valaszok[kerdes][randint(0, len(valaszok[kerdes] - 1))
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


client.run(os.getenv('TOKEN'))

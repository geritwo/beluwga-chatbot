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
        {
            "Nem jól": [
                {
                    "miért?":
                        [
                            "Mert magányos vagyok",
                            "Nem tudom.",
                            "Egyszerűen rossz napom van."
                        ]
                },
            ]
        },
        "Egész jól"
    ]
}


def kulcs_egysegesito(lista):
    kulcsok = []
    for kulcs in lista:
        if isinstance(kulcs, str):
            kulcsok.append(kulcsok)
        else:
            kulcsok.append(list(kulcs.keys())[0])
    return kulcsok


def valasz_valaszto(valaszok_lista):
    valasz_index = valaszok_lista[random.randint(0, len(valaszok_lista) - 1)]
    lehetseges_valaszok = kulcs_egysegesito(valaszok_lista)
    return lehetseges_valaszok[valasz_index]


def valaszol(kerdes, elozo_kerdes, elozo_valasz):
    if elozo_kerdes and elozo_valasz:
        aktualis_fo_tema = valaszok[elozo_kerdes]

        for tema in aktualis_fo_tema:
            if
        megvalaszolando_tema =


class Partnerek():

    def __init__(self):
        self.aktiv_partnerek = {}

    def megjegyez(self, partner, kerdes, valasz):
        self.aktiv_partnerek[partner] = [kerdes, valasz]

    def felidez(self, partner):
        if partner in list(self.aktiv_partnerek.keys()):
            return self.aktiv_partnerek[partner][0], self.aktiv_partnerek[1]
        else:
            return "", ""


# Main

partnerek = Partnerek()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$'):
        kerdes = message.content.split('$')[1].lower()
        elozo_kerdes, elozo_valasz = partnerek.felidez(message.author)
        valasz = valaszol(kerdes, elozo_kerdes, elozo_valasz)
        partnerek.megjegyez(message.author, kerdes, valasz)

        await message.channel.send(valasz)


client.run(os.getenv('TOKEN'))

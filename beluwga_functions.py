import random
from valaszok import valaszok


def ko_papir_ollo(kerdes):
    valasz = random.choice(valaszok['$ko_papir_ollo'])
    return valasz


def valaszol(kerdes):
    if kerdes == "kő" or kerdes == "papír" or kerdes == "olló":
        valasz = ko_papir_ollo(kerdes)
    elif kerdes in valaszok.keys():
        if isinstance(valaszok[kerdes], str):
            valasz = valaszok[kerdes]
        else:
            valasz = random.choice(valaszok[kerdes])
    else:
        valasz = "Erre nem tudok valaszolni."
    return valasz

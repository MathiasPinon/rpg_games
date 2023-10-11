import unittest
import random

import names
from random import *
from TP2.Charmeur import Charmeur
from TP2.Calculateur import Calculateur
from TP2.Objet import Objet
from TP2.Personnage import Personnage
from TP2.Brute import Brute
from TP2.Negociateur import Negociateur


def get_popularite(pers: list) -> dict:
    # return le dictionnaire de la popularite de l'utilisateur
    popularite = {p: 0 for p in pers}

    for p in pers:
        amis_de_p = p.getAmis()
        for autre in amis_de_p:
            popularite[autre] += amis_de_p[autre]

    return {k: v for k, v in sorted(popularite.items(), key=lambda item: item[1])}


def get_sante(pers: list) -> dict:
    # retourne la santé de chaque personnage par rapport au autre
    sante = {p: round(p.getPV(), 1) for p in pers}
    return {k: v for k, v in sorted(sante.items(), key=lambda item: item[1])}


def get_richesse(pers: list) -> dict:
    #  retourne la richesse de chaque personnage par raport au autre
    richesse = {p: round(p.getRichesse(), 1) for p in pers}
    return {k: v for k, v in sorted(richesse.items(), key=lambda item: item[1])}

if __name__ == "__main__":

    list_obs = [ Objet(f'Obj_{i}', 15) for i in range(50) ]

    alice = Brute("Alice", list_obs[:10])
    bob = Charmeur("Bob", list_obs[10:20])
    claire = Personnage("Claire", list_obs[20:30])
    daniel = Calculateur("Daniel", list_obs[30:40])
    elise = Negociateur("Elise", list_obs[40:])

    persos = [alice, bob, claire, daniel, elise]

    for _ in range(1000):
        perso1 = choice(persos)
        perso2 = perso1
        while perso2 == perso1:
            perso2 = choice(persos)

        perso1.choisir_action(perso2)

    for p in persos:
        print(p)

    print('Popularité')
    print(get_popularite(persos))

    print('Santé')
    print(get_sante(persos))

    print('Richesse')
    print(get_richesse(persos))
import random

import names

from TP3.Brute import Brute
from TP3.Calculateur import Calculateur
from TP3.Charmeur import Charmeur
from TP3.Negociateur import Negociateur
from TP3.Objet import Objet
from TP3.Personnage import Personnage

words = open('/etc/dictionaries-common/words').readlines()
personnages = [Personnage, Brute, Charmeur, Calculateur, Negociateur]

perso_defaut = Personnage('')

def create_RandomPersonnage() -> Personnage:
    perso_type = random.choice(personnages)
    if isinstance(perso_defaut.getObjets(),list):
        objets = [Objet(random.choice(words)) for _ in range(5)]
    else:
        objets = {Objet(random.choice(words)) for _ in range(5)}
    return perso_type(names.get_full_name(), objets)

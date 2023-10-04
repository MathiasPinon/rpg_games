from TP2.Personnage import Personnage
from random import *
from TP2.Charmeur import Charmeur
from TP2.Brute import Brute


class Negociateur(Personnage):

    def __init__(self, n: str, obj: list = None):
        Personnage.__init__(self, n, obj)
        self.intelligence *= 1.30
        self.obstination *= 1.30
        self.force *= 0.70
        self.empathie *= 0.70

    def choisir_action(self, autre):
        if type(autre) == Charmeur :
            if len(autre.objets) > 0:
                return self.acheter(choice(autre.getObjets()), autre)
        if self.intelligence > autre.intelligence or (self.intelligence == autre.intelligence and self.obstination > autre.obstination ) :
            if autre in self.amis and self.amis[autre] > 0 :
                i = randint(0,1)
                if i == 0 :
                    if len(self.objets) > 0:
                        obj_choix = choice(self.objets)
                        obj_choix.valeur *= 1.15
                        return self.vendre(obj_choix,autre)
                elif i == 1 :
                    if len(autre.objets) > 0:
                        obj_choix = choice(autre.objets)
                        obj_choix.valeur *= 0.85
                        return self.acheter(obj_choix,autre)
            else :
                i = randint(0, 1)
                if i == 0:
                    if len(self.objets) > 0:
                        obj_choix = choice(self.objets)
                        obj_choix.valeur *= 1.30
                        return self.vendre(obj_choix, autre)
                if i == 1:
                    if len(autre.objets) > 0:
                        obj_choix = choice(autre.objets)
                        obj_choix.valeur *= 0.70
                        return self.acheter(obj_choix, autre)
        else:
            i = randint(0, 1)
            if i == 0:
                if len(self.objets) > 0:
                    return self.vendre(choice(self.objets), autre)
            elif i == 1:
                if len(autre.objets) > 0:
                    return self.acheter(choice(autre.getObjets()), autre)

        return False
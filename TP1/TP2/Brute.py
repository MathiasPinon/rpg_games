from TP2.Personnage import Personnage
from random import *
from TP2.Charmeur import Charmeur
class Brute(Personnage):
    def __init__(self, n: str, obj: list = None):
        Personnage.__init__(self, n, obj)
        self.force *= 1.30
        self.obstination *= 1.30
        self.intelligence *= 0.70
        self.charisme *= 0.70

    def choisir_action(self, autre):

        if autre not in self.amis or self.amis[autre] <= 0 :
            if type(autre) != Charmeur :
                if len(autre.objets) > 0:
                    return self.prendre(choice(autre.getObjets()), autre)
            else :
                return False
        else:
            if type(autre) == Charmeur  and autre.charisme > self.charisme :
                if len(self.objets) > 0:
                    return self.donner(choice(self.objets), autre)
            else :
                i = randint(0, 2)
                if i == 0:
                    if autre.getObjets():
                        return self.acheter(choice(autre.getObjets()), autre)
                elif i == 1:
                    if self.objets:
                        return self.vendre(choice(self.objets), autre)
        return False
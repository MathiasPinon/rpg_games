from TP2.Personnage import Personnage
from random import *
from TP2.Charmeur import Charmeur
from TP2.Brute import Brute
from TP2.Negociateur import Negociateur


class Calculateur(Personnage):

    def __init__(self, n: str, obj: list = None):
        Personnage.__init__(self, n, obj)
        self.intelligence *= 1.30
        self.obstination *= 1.30
        self.force *= 0.70
        self.empathie *= 0.70

    def choisir_action(self, autre):



        if self.pv < 10 :
            i = randint(0,2)
            if i == 0 :
                if self.objets :
                    return self.vendre(choice(self.objets),autre)
            elif i == 1 :
                if self.objets :
                    return self.acheter(choice(self.objets),autre)
            if i == 2 :
                    if self.objets :
                        return self.donner(choice(self.objets),autre)
        if self.force > autre.force :
            return self.prendre(choice(self.objets),autre)

        if type(autre) == Charmeur:
            i = randint(0, len(self.objets) - 1)
            return self.vendre(self.objets[i], autre)

        if autre in self.amis and self.amis[autre] <= 0 :
            return self.donner(choice(self.objets),autre)

        t = randint(0,1)
        if t == 0 :
            x = randint(0,3)
            if x == 0:
                if autre.getObjets():
                    return self.acheter(choice(autre.getObjets()), autre)
            elif x == 1:
                if autre.getObjets():
                    return self.prendre(choice(autre.getObjets()), autre)
            elif x == 2:
                if self.objets:
                    return self.vendre(choice(self.objets), autre)
            elif x == 3:
                if self.objets:
                    return self.donner(choice(self.objets), autre)

        return False
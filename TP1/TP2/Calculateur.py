from TP2.Personnage import Personnage
from random import *
from TP2.Charmeur import Charmeur
from TP2.Brute import Brute
from TP2.Négociateur import Négociateur


class Calculateur(Personnage):

    def __init__(self, n: str, obj: list = None):
        Personnage.__init__(self, n, obj)
        self.intelligence *= 1.30
        self.obstination *= 1.30
        self.force *= 0.70
        self.empathie *= 0.70

    def choisir_action(self, autre):
        if type(autre) == Charmeur :
            i = randint(0,len(self.objets)-1)
            return self.vendre(self.objets[i] , autre)
        if self.pv < 10 :
            i = randint(0,3)
            if i == 0 :
                if self.objets :
                    return self.vendre(choice(self.objets),autre)

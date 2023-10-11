from TP2.Personnage import Personnage
from random import *

class Charmeur(Personnage):

    def __init__(self , n: str, obj: list = None):
        Personnage.__init__(self, n , obj )
        self.charisme *= 1.30
        self.empathie *= 1.30
        self.force *= 0.70
        self.obstination *= 0.70

    def choisir_action(self, autre):

        if autre not in self.amis :
            obj_choisi = randint(0,len(self.objets)-1)
            return self.donner(self.objets[obj_choisi] , autre )
        else :
            if type(autre) != Charmeur :
                return autre.choisir_action(self)
            else :
                i = randint(0, 4)
                if i == 0:
                    if autre.getObjets():
                        return self.acheter(choice(autre.getObjets()), autre)
                elif i == 1:
                    if autre.getObjets():
                        return self.prendre(choice(autre.getObjets()), autre)
                elif i == 2:
                    if self.objets:
                        return self.vendre(choice(self.objets), autre)
                elif i == 3:
                    if self.objets:
                        return self.donner(choice(self.objets), autre)

        return False

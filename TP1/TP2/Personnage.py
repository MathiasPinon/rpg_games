from random import randint
from Objet import *


class Personnage(object):

    def __init__(self, n: str, obj: list = None):
        self.nom = n
        self.amis = {}
        if obj is None:
            self.objets = []
        else:
            self.objets = obj.copy()

        self.pv = 100
        self.richesse = 100.0

        self.intelligence = randint(3, 18)
        self.force = randint(3, 18)
        self.charisme = randint(3, 18)
        self.obstination = randint(3, 18)
        self.empathie = randint(3, 18)

        super().__init__()

    def __str__(self) -> str:
        return f'{self.nom} a {self.pv} points de vie et {self.richesse} de richesse'

    def ajoutObjet(self, obj: Objet):
        list_obj = self.objets
        list_obj.append(obj)
        self.objets = list_obj

    def getObjets(self) -> list:
        list = self.objets.copy()
        return list

    def vendre(self, obj: Objet, autre) -> bool:
        if obj in self.objets and obj.valeur <= autre.richesse:
            self.richesse = self.richesse + obj.valeur
            autre.richesse = autre.richesse - obj.valeur
            self.objets.remove(obj)
            autre.ajoutObjet(obj)
            if autre not in self.amis:
                self.amis[autre] = 0
            if self not in autre.amis:
                autre.amis[self] = 0

            return True

        else:
            return False

    def acheter(self, obj: Objet, autre) -> bool:
        return autre.vendre(obj, self)

    def donner(self, obj: Objet, autre) -> bool:
        if obj in self.objets:
            self.objets.remove(obj)
            autre.ajoutObjet(obj)
            if autre not in self.amis:
                self.amis[autre] = 0
            if self not in autre.amis:
                autre.amis[self] = 0.5
            elif self in autre.amis:
                if autre.amis[self] + 0.5 <= 1:
                    autre.amis[self] += 0.5
            return True
        else:
            return False

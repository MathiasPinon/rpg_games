from random import randint
from TP2.Objet import *
from random import choice


class Personnage(object):
    def __init__(self, n: str, obj: list = None):
        self.nom = n
        self.amis = {}
        if obj is None:
            self.objets = []
        else:
            self.objets = obj.copy()

        self._pv = 100
        self._richesse = 100.0

        self._intelligence = randint(3, 18)
        self._force = randint(3, 18)
        self._charisme = randint(3, 18)
        self._obstination = randint(3, 18)
        self._empathie = randint(3, 18)

        super().__init__()

    @property
    def pv(self):
        return self._pv

    @property
    def richesse(self):
        return self._richesse

    @property
    def intelligence(self):
        return self._intelligence

    @property
    def force(self):
        return self._force

    @property
    def charisme(self):
        return self._charisme

    @property
    def obstination(self):
        return self._obstination

    @property
    def empathie(self):
        return self._empathie

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
            self._richesse = self.richesse + obj.valeur
            autre.richesse = autre.richesse - obj.valeur
            obj.effetCession(self)
            obj.effetAcquisition(autre)
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
            obj.effetCession(self)
            obj.effetAcquisition(autre)
            if autre not in self.amis:
                self.amis[autre] = 0
            if self not in autre.amis:
                autre.amis[self] = 0.5
            elif self in autre.amis:
                if autre.amis[self] + 0.5 <= 1:
                    autre.amis[self] += 0.5
                else:
                    autre.amis[self] = 1
            return True
        else:
            return False

    def prendre(self, obj: Objet, autre):
        if obj in autre.objets and self.force > autre.force or (
                self.force == autre.force and self.obstination > autre.obstination):
            obj.effetCession(autre)
            obj.effetAcquisition(self)
            autre.amis[self] = -1
            if autre not in self.amis:
                self.amis[autre] = 0
            degat = self.force - autre.force
            if self.pv - degat > 0:
                self._pv -= degat
            else:
                self._pv = 0
            if autre.pv - degat > 0:
                autre.pv -= degat
            else:
                autre.pv = 0
            return True
        else:
            return False

    def choisir_action(self, autre):
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
        else:
            return True

        return False

    def __str__(self):
        obj =  f"{self.nom} à {self.richesse} pièce et à actuellement {self.pv} pv.\n"
        if len(self.objets) > 1:
            obj += "Dispose de : "
            for i in range(len(self.objets)):
                if i != (len(self.objets) - 1):
                     obj += str(self.objets[i].nom) + " ,"
                else:
                     obj += str(self.objets[i].nom) + " .\n"
        else:
            obj += "Possède aucun objet.\n"
        if len(self.amis) > 0:
            obj += "Il a dans sa liste d'amis : "
            t = 0
            for perso in self.amis.keys():
                t += 1
                if perso.nom is not None:
                    if t != len(self.amis):
                        obj += perso.nom + ", "
                    else:
                        obj += perso.nom + ".\n"
        else:
            obj += "Il n'a pas d'amis .\n"

        return obj

    def getAmis(self) -> dict :
        # Retourne le dictionnaire des amis et leur niveau d'amitié d'un Personnage
        return self.amis

    def getPV(self) -> float:
        # Retourne les points de vie d'un Personnage
        return self.pv

    def getRichesse(self) -> float:
        # Retourne la totalité des richesses d'un Personnage
        # la totalité des richesses est définie par la somme des valeurs des objets
        # que possède un Personnage ainsi que la valeur de l'attribut self.richesse
        richesse = 0
        for i in range(len(self.objets)) :
            richesse += self.objets[i].valeur
        richesse += self.richesse
        return richesse






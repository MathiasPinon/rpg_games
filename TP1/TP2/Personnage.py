from random import randint


class Personnage(object):

    def __init__(self, n: str, obj: list = None):
        self.nom = n
        self.amis = {}
        if obj is None:
            self.objets = []
        else:
            self.objets = obj

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

    def ajoutObjet(self, obj: object):
        list_obj = self.objets
        list_obj.append(obj)
        self.objets = list_obj

    def getObjets(self) -> list:
        list = self.objets
        return list

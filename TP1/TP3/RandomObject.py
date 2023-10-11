from TP3.Objet import Objet
from random import randint


class RandomObjet(Objet):
    def effetAcquisition(self, p):
        def effet(**kwargs):
            #Application de la transaction de l'objet.
            prix = kwargs['prix'] if 'prix' in kwargs.keys() else self.valeur
            p._richesse = p._richesse - prix
            p.objets.append(self)
            # Application de l'effet sur le personnage.
            p._intelligence += randint(-1, 1)
            p._force += randint(-1, 1)
            p._charisme += randint(-1, 1)
            p._obstination += randint(-1, 1)
            p._empathie += randint(-1, 1)

        return effet

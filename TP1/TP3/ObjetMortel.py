from TP3.Objet import Objet


class ObjetMortel(Objet):
    def effetAcquisition(self, p):
        def effect(**kwargs):
            prix = kwargs['prix'] if 'prix' in kwargs.keys() else self.valeur
            p._richesse -= prix
            p.objets.append(self)
            p._intelligence = 0
            p._force = 0
            p._charisme = 0
            p._obstination = 0
            p._empathie = 0
            p._pv = 0
        return effect
class Objet(object):

    def __init__(self, n: str = None, v: int = 10):
        super().__init__()

        self.nom = n
        self.valeur = v

    def effetAcquisition(self, p):
        # Renvoie la fonction à exécuter lorsqu'un Personnage `p` acquiert l'objet `self`
        def effet(**kwargs):
            prix =  kwargs['prix'] if 'prix' in kwargs.keys() else 0
            p.richesse = p.richesse - prix
            p.objets.append(self)
        return effet(prix=self.valeur)

    def effetCession(self, p):
        # Renvoie la fonction à exécuter lorsqu'un Personnage `p` cède l'objet `self`
        def effet(**kwargs):
            prix = kwargs['prix'] if 'prix' in kwargs.keys() else 0
            p.richesse = p.richesse + prix
            ind = p.objets.index(self)
            del p.objets[ind]
        return effet(prix=self.valeur)



class Objet(object):

    def __init__(self, n: str = None, v: int = 10):
        super().__init__()

        self.nom = n
        self.valeur = v

    def effetAcquisition(self, p):
        # Renvoie la fonction à exécuter lorsqu'un Personnage `p` acquiert l'objet `self`
        def effet(**kwargs):
            p.objets.append(self)
        return effet

    def effetCession(self, p):
        # Renvoie la fonction à exécuter lorsqu'un Personnage `p` cède l'objet `self`
        def effet(**kwargs):
            RandomObjet()
            pass

        return effet


class RandomObjet(Objet){

}
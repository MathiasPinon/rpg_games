class Objet(object):

    def __init__(self, n: str = None, v: int = 10):
        super().__init__()

        self.nom = n
        self.valeur = v
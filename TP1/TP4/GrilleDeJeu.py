import tkinter

from TP4.Localisable import Localisable


class GrilleDeJeu(tkinter.Canvas):

    def __init__(self, root, **kwargs):
        super().__init__(root, **kwargs)
        self._objets = set()
        self._lieux = {}

    @property
    def lieux(self):
        return self._lieux

    def getItems(self, loc: tuple) -> set:
        if loc in self._lieux.keys():
            return self._lieux[loc]
        else:
            return set()

    def ajoutItem(self, o: Localisable):
        self._objets.add(o)
        if o.lieu not in self._lieux.keys():
            self._lieux[o.lieu] = {o}
        else:
            self._lieux[o.lieu].add(o)

    def enleveItem(self, o: Localisable):
        self._objets.remove(o)
        self._lieux[o.lieu].remove(o)


if __name__ == '__main__':
    # Initialisation de Tk
    root = tkinter.Tk()

    # Création d'un _Canvas_
    myCanvas = GrilleDeJeu(root, bg="white", height=300, width=300)

    myCanvas.pack()
    root.mainloop()
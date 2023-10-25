import tkinter

from TP3.Personnage import Personnage
from TP4.GrilleDeJeu import GrilleDeJeu
from TP4.InterfaceItem import InterfaceItem


class InterfacePersonnage(Personnage, InterfaceItem):
    def __init__(self, nom: str, cv: tkinter.Canvas):
        # à compléter
        super().__init__( name=nom , cv= cv , n=nom)
        self.attributs["richesse"] = self.richesse
        self.attributs["inteligence"] = self.intelligence
        self.attributs["force"] = self.force
        self.attributs["charisme"] = self.charisme
        self.attributs["obstination"] = self.obstination
        self.attributs["empathie"] = self.empathie



if __name__ == '__main__':
    # init tk

    root = tkinter.Tk()

    # create canvas
    myCanvas = GrilleDeJeu(root, bg="white", height=300, width=300)

    ipPers = InterfacePersonnage("Perso", myCanvas)
    print(ipPers.force)
    print(ipPers.charisme)

    myCanvas.pack()
    root.mainloop()
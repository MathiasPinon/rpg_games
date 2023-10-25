import tkinter

from TP3.Personnage import Personnage
from TP4.InterfaceItem import InterfaceItem


class InterfacePersonnage(Personnage, InterfaceItem):
    def __init__(self, nom: str, cv: tkinter.Canvas, n: str, **kwargs):
        # à compléter
        super().__init__(n, **kwargs)
        self.attributs["richesse"] = self.richesse
        self.attributs["inteligence"] = self.intelligence
        self.attributs["force"] = self.force
        self.attributs["charisme"] = self.charisme
        self.attributs["obstination"] = self.obstination
        self.attributs["empathie"] = self.empathie
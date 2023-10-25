import tkinter

from TP3.Charmeur import Charmeur
from TP4.InterfacePersonnage import InterfacePersonnage


class InterfaceBrute(InterfacePersonnage, Charmeur):
    def __init__(self, nom: str, cv: tkinter.Canvas):
        super().__init__(n=nom, cv=cv)
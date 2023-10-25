import tkinter

from TP3.Calculateur import Calculateur
from TP4.InterfacePersonnage import InterfacePersonnage


class InterfaceBrute(InterfacePersonnage, Calculateur):
    def __init__(self, nom: str, cv: tkinter.Canvas):
        super().__init__(n=nom, cv=cv)
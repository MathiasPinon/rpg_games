import tkinter

from TP3.Brute import Brute
from TP4.InterfacePersonnage import InterfacePersonnage


class InterfaceBrute(InterfacePersonnage, Brute):
    def __init__(self, nom: str, cv: tkinter.Canvas):
        super().__init__(n=nom , cv = cv)
import tkinter

from TP3.Negociateur import Negociateur
from TP4.InterfacePersonnage import InterfacePersonnage


class InterfaceBrute(InterfacePersonnage, Negociateur):
    def __init__(self, nom: str, cv: tkinter.Canvas):
        super().__init__(n=nom, cv=cv)
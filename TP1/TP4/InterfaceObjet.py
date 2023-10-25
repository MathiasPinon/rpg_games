import tkinter

from TP3.Objet import Objet
from TP4.InterfaceItem import InterfaceItem


class InterfaceBrute(InterfaceItem, Objet):
    def __init__(self, n: str ,v: int , cv: tkinter.Canvas):
        super().__init__(n=n, v=v , cv=cv)
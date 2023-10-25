import tkinter
from random import randint

from TP3.Objet import Objet
from TP4.InterfaceItem import InterfaceItem, randomRGBString


class InterfaceBrute(InterfaceItem, Objet):
    def __init__(self, n: str ,v: int , cv: tkinter.Canvas):
        super().__init__(n=n, v=v , cv=cv, glypheObj = self.petitTriangle(cv , n ))

    def randomRGBString(self):
        return "#" + ("%06x" % randint(0, 16777215))

    def petitTriangle(self,cv: tkinter.Canvas, nom: str):
        points = [1, 1, 1, 1, 1, 1]
        return cv.create_polygon(points, fill=randomRGBString(), tags=nom)

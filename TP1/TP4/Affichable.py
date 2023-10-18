import tkinter
from random import randint


class Affichable(object):

    def __init__(self, n : str = None, **kwargs):
        super().__init__(**kwargs)
        self.__name = n
        if 'glyph' in kwargs.keys():
            self.__glyph = kwargs['glyph']
            del kwargs['glyph']
        else:
            self.__glyph = None

        self.__attributs = kwargs.copy()

    @property
    def nom(self):
        return self.__name

    @nom.setter
    def nom(self, n: str):
        self.__name = n

    @property
    def glyph(self):
        return self.__glyph

    @glyph.setter
    def glyph(self, g):
        self.__glyph = g

    @property
    def attributs(self):
        return self.__attributs

    def randomRGBString(self):
        return "#" + ("%06x" % randint(0, 16777215))

    def petitRectangle(self: tkinter.Canvas, nom: str):
        return self.create_rectangle(0, 0, 3, 3, fill=randomRGBString(), tags=nom)
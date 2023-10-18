import tkinter
from random import randint

from TP4.Affichable import Affichable
from TP4.Deplacable import Deplacable
from TP4.GrilleDeJeu import GrilleDeJeu


class InterfaceItem(Deplacable, Affichable):

    def __init__(self, **kwargs):
        Affichable.__init__(self, n = kwargs['name'])
        self.cv = kwargs['cv']
        x = randint( 0, kwargs['cv'].winfo_screenwidth())
        y = randint(0, kwargs['cv'].winfo_screenheight())
        Deplacable.__init__(self , x = x , y =  y)
        self.glyph = self.glyph if 'glyph' in kwargs.keys() else petitRectangle(self.cv , self.nom)
        self.cv.moveto(self.glyph, self.lieu[0], self.lieu[1])



def randomRGBString():
    return "#" + ("%06x" % randint(0, 16777215))

def petitRectangle(cv : tkinter.Canvas, nom : str):
    return cv.create_rectangle(0, 0, 3, 3, fill=randomRGBString(), tags=nom)

if __name__ == '__main__':
    root = tkinter.Tk()
    myCanvas = GrilleDeJeu(root, bg="white", height=300, width=300)

    obj1 = InterfaceItem(name="Obj1", cv=myCanvas)
    obj2 = InterfaceItem(name="Obj2", cv=myCanvas)

    myCanvas.pack()
    root.mainloop()
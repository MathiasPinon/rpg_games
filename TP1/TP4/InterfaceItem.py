import tkinter
from random import randint

from TP4.Affichable import Affichable
from TP4.Deplacable import Deplacable
from TP4.GrilleDeJeu import GrilleDeJeu


class InterfaceItem(Deplacable, Affichable):

    def __init__(self, **kwargs):
        self.__cv = kwargs['cv']
        x = randint(1, kwargs['cv'].winfo_reqwidth())
        y = randint(1, kwargs['cv'].winfo_reqheight())
        super().__init__(x = x , y =  y, n = kwargs['name'])

        # Deplacable.__init__(self , x = x , y =  y)
        self.glyph = self.glyph if 'glyph' in kwargs.keys() else petitRectangle(self.__cv , self.nom)
        self.__cv.moveto(self.glyph, self.lieu[0], self.lieu[1])
        self.__cv.tag_bind(self.nom, "<Button-2>", self.afficher)

    def attributsWindow(self):
        w = tkinter.Toplevel(self.__cv)
        w.title(f'Attributs pour {self.nom}')
        l2 = tkinter.Label(w, text=self.attributs)
        l2.grid(row = 1 , column = 0 , pady = 2)

    def afficher(self, e=None):
        self.attributsWindow()


def randomRGBString():
    return "#" + ("%06x" % randint(0, 16777215))

def petitRectangle(cv : tkinter.Canvas, nom : str):
    return cv.create_rectangle(0, 0, 3, 3, fill=randomRGBString(), tags=nom)


 help(tkinter.Event)

if __name__ == '__main__':
    root = tkinter.Tk()
    myCanvas = GrilleDeJeu(root, bg="white", height=300, width=300)

    obj = InterfaceItem(name="Obj1", cv=myCanvas)
    obj.attributs['Attr'] = 'Un attribut'
    obj.attributsWindow()

    myCanvas.pack()
    root.mainloop()
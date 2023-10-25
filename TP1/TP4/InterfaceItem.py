import tkinter
from random import randint

from TP4.Affichable import Affichable
from TP4.Deplacable import Deplacable
from TP4.GrilleDeJeu import GrilleDeJeu


class InterfaceItem(Deplacable, Affichable):

    def __init__(self, **kwargs):
        self.__cv = kwargs['cv'] if "cv" in kwargs.keys() else None
        x = randint(1, kwargs['cv'].winfo_reqwidth())
        y = randint(1, kwargs['cv'].winfo_reqheight())
        super().__init__(x = x , y =  y, n = kwargs['name'])
        # Deplacable.__init__(self , x = x , y =  y)
        self.glyph = self.glyph if 'glyph' in kwargs.keys() else petitRectangle(self.__cv , self.nom)
        self.__cv.moveto(self.glyph, self.lieu[0], self.lieu[1])
        self.__cv.ajoutItem(self)
        self.__cv.tag_bind(self.nom, "<Button-2>", self.afficher)
        self.__cv.tag_bind(self.nom, "<B1-Motion>", self.action2)
        self.__cv.tag_bind(self.nom, "<ButtonRelease-1>", self.action3)

    def attributsWindow(self):
        w = tkinter.Toplevel(self.__cv)
        w.title(f'Attributs pour {self.nom}')
        l2 = tkinter.Label(w, text=self.attributs)
        i = 1
        for keys, values in self.attributs.items():
            l2 = tkinter.Label(w, text=f"{keys}:")
            l2.grid(row = i , column = 0 , pady = 2)
            l2 = tkinter.Label(w, text=values)
            l2.grid(row=i, column=1, pady=2)
            i += 1

    def afficher(self, e=None):
        self.attributsWindow()

    def action2(self, e=None):
        return

    def deplacer(self,e):
        self.__cv.enleveItem(self)
        self.move()
        self.__cv.ajoutItem(self)
        self.__cv.moveto(self.glyph, self.lieu[0], self.lieu[1])
        if self.lieu != self.destination:
            self.__cv.after(100, self.deplacer, e)

    def action3(self,event):
        posx  = event.x
        posy = event.y
        self.destination= (posx,posy)
        self.deplacer(None)

    def reset(self,e):
        self.destination = self.lieu
    def action1(self,e=None):
        self.reset(None)
        return

def randomRGBString():
    return "#" + ("%06x" % randint(0, 16777215))

def petitRectangle(cv : tkinter.Canvas, nom : str):
    return cv.create_rectangle(0, 0, 3, 3, fill=randomRGBString(), tags=nom)



if __name__ == '__main__':
    root = tkinter.Tk()
    myCanvas = GrilleDeJeu(root, bg="white", height=300, width=300)

    obj = InterfaceItem(name="Obj1", cv=myCanvas)
    obj.attributs['Attr'] = 'Un attribut'
    obj.attributsWindow()

    myCanvas.pack()
    root.mainloop()
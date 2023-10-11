import tkinter

class GrilleDeJeu(tkinter.Canvas):

    def __init__(self, root, **kwargs):
        super().__init__(root, **kwargs)

if __name__ == '__main__':
    # Initialisation de Tk
    root = tkinter.Tk()

    # Création d'un _Canvas_
    myCanvas = GrilleDeJeu(root, bg="white", height=300, width=300)

    myCanvas.pack()
    root.mainloop()
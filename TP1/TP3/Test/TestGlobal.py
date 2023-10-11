from TP2.Objet import *
from TP2.Personnage import *
if __name__ == "__main__":

    o1 = Objet("serviette", 30)
    o2 = Objet()
    o3 = Objet("cacahuète", 10)

    p1 = Personnage("Arthur")
    p2 = Personnage("Trillian",[o1, o2, o3])

    for _ in range(10):
        p1.choisir_action(p2)
        p2.choisir_action(p1)

    print(p1)
    print(p2)
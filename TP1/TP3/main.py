from TP3.ObjetMortel import ObjetMortel
from TP3.Personnage import Personnage

if __name__ == "__main__":

    k = ObjetMortel('kill',0)
    alice = Personnage("Alice", [k])
    bob = Personnage("Bob")

    alice.donner(k, bob)
    alice.prendre(k, bob)

import unittest
import random

import names

from TP2.Charmeur import Charmeur
from TP2.Objet import Objet
from TP2.Personnage import Personnage

words = open('/etc/dictionaries-common/words').readlines()

class PersonnageTest():
    def vendre(self, obj: Objet, autre) -> str:
        return "PersonnageTest.vendre"

    def acheter(self, obj: Objet, autre) -> str:
        return "PersonnageTest.acheter"

    def donner(self, obj: Objet, autre) -> str:
        return "PersonnageTest.donner"

    def prendre(self, obj: Objet, autre) -> str:
        return "PersonnageTest.prendre"

    def choisir_action(self, autre) -> str:
        return "PersonnageTest.choisir_action"



class NewPersonnage(Personnage):

    def __init__(self):
        super().__init__(names.get_full_name())

    def choisir_action(self, autre) -> str:
        return 'NewPersonnage.choisir_action()'

class TestCharmeur(unittest.TestCase):
    def test_characteristiques(self):

        charisme_charmeur = 0
        charisme_personnage = 0
        empathie_charmeur = 0
        empathie_personnage = 0
        force_charmeur = 0
        force_personnage = 0
        obstination_charmeur = 0
        obstination_personnage = 0

        for i in range(1000):
            p = Personnage(names.get_full_name())
            charisme_personnage += p.charisme
            empathie_personnage += p.empathie
            force_personnage += p.force
            obstination_personnage += p.obstination

            c = Charmeur(names.get_full_name())
            charisme_charmeur += c.charisme
            empathie_charmeur += c.empathie
            force_charmeur += c.force
            obstination_charmeur += c.obstination

        self.assertAlmostEqual(1.3, charisme_charmeur/charisme_personnage, 1)  # add assertion here
        self.assertAlmostEqual(1.3, empathie_charmeur/empathie_personnage, 1)  # add assertion here
        self.assertAlmostEqual(0.7, force_charmeur/force_personnage, 1)  # add assertion here
        self.assertAlmostEqual(0.7, obstination_charmeur/obstination_personnage, 1)  # add assertion here

    def test_action(self):
        o = Objet(random.choice(words))
        c1 = Charmeur(names.get_full_name(), [o])
        c2 = Charmeur(names.get_full_name())

        c1.choisir_action(c2)

        self.assertEqual([o], c2.objets)
        self.assertEqual([], c1.objets)

        p = NewPersonnage()
        c1.amis[p] = 0.0

        self.assertEqual('NewPersonnage.choisir_action()', c1.choisir_action(p))

        Personnage.donner = PersonnageTest.donner
        Personnage.prendre = PersonnageTest.prendre
        Personnage.vendre = PersonnageTest.vendre
        Personnage.acheter = PersonnageTest.acheter
        Personnage.choisir_action = PersonnageTest.choisir_action

        action = c1.choisir_action(c2)
        self.assertTrue(action in {"PersonnageTest.choisir_action", "PersonnageTest.vendre", "PersonnageTest.acheter", "PersonnageTest.donner", "PersonnageTest.prendre"})

if __name__ == '__main__':
    unittest.main()
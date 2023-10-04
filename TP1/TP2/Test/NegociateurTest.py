import unittest
import random

import names

from TP2.Charmeur import Charmeur
from TP2.Negociateur import Negociateur
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


class TestNegociateur(unittest.TestCase):
    def test_characteristiques(self):
        empathie_nego = 0
        empathie_personnage = 0
        intelligence_nego = 0
        intelligence_personnage = 0
        force_nego = 0
        force_personnage = 0
        obstination_nego = 0
        obstination_personnage = 0

        for i in range(1000):
            p = Personnage(names.get_full_name())
            empathie_personnage += p.empathie
            intelligence_personnage += p.intelligence
            force_personnage += p.force
            obstination_personnage += p.obstination

            b = Negociateur(names.get_full_name())
            empathie_nego += b.empathie
            intelligence_nego += b.intelligence
            force_nego += b.force
            obstination_nego += b.obstination

        self.assertAlmostEqual(0.7, empathie_nego / empathie_personnage, 1, "L'attibut de `empathie` du `Negociateur` n'est pas 30% infÃ©rieur qu'un `Personnage` ordinaire")
        self.assertAlmostEqual(1.3, intelligence_nego / intelligence_personnage, 1, "L'attibut de `intelligence` du `Negociateur` n'est pas 30% supÃ©rieur qu'un `Personnage` ordinaire")
        self.assertAlmostEqual(0.7, force_nego / force_personnage, 1, "L'attibut de `force` du `Negociateur` n'est pas 30% infÃ©rieur qu'un `Personnage` ordinaire")
        self.assertAlmostEqual(1.3, obstination_nego / obstination_personnage, 1, "L'attibut de `obstination` du `Negociateur` n'est pas 30% supÃ©rieur qu'un `Personnage` ordinaire")

    def test_choisir_action(self):

        object_list_nego = [Objet(random.choice(words)) for _ in range(2)]
        n = Negociateur(names.get_full_name(), object_list_nego)

        Personnage.donner = PersonnageTest.donner
        Personnage.prendre = PersonnageTest.prendre
        Personnage.vendre = PersonnageTest.vendre
        Personnage.acheter = PersonnageTest.acheter
        Personnage.choisir_action = PersonnageTest.choisir_action

        Negociateur.vendre = PersonnageTest.vendre
        Negociateur.acheter = PersonnageTest.acheter

        # Personnage quelconque (connu ou inconnu, ami ou pas)
        for _ in range(10):
            object_list = [Objet(random.choice(words)) for _ in range(2)]
            p1 = Personnage(names.get_full_name(), object_list)
            self.assertTrue(n.choisir_action(p1) in ["PersonnageTest.acheter", "PersonnageTest.vendre"], "Lors de l'interaction avec un `Personnage` quelconque, le `Negociateur` ne se restreint pas seulement Ã  `acheter` ou `vendre`")

        # Charmeur quelconque
        for _ in range(10):
            object_list = [Objet(random.choice(words)) for _ in range(2)]
            c1 = Charmeur(names.get_full_name(), object_list)
            self.assertEqual(n.choisir_action(c1), "PersonnageTest.acheter", "Lors de l'interaction avec un `Charmeur` quelconque, le `Negociateur` ne se restreint Ã  `acheter` uniquement")


if __name__ == '__main__':
    unittest.main()
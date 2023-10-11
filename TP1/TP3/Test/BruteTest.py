import unittest
import random

import names

from TP2.Brute import Brute
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


class TestBrute(unittest.TestCase):
    def test_characteristiques(self):
        charisme_brute = 0
        charisme_personnage = 0
        intelligence_brute = 0
        intelligence_personnage = 0
        force_brute = 0
        force_personnage = 0
        obstination_brute = 0
        obstination_personnage = 0

        for i in range(1000):
            p = Personnage(names.get_full_name())
            charisme_personnage += p.charisme
            intelligence_personnage += p.intelligence
            force_personnage += p.force
            obstination_personnage += p.obstination

            b = Brute(names.get_full_name())
            charisme_brute += b.charisme
            intelligence_brute += b.intelligence
            force_brute += b.force
            obstination_brute += b.obstination

        self.assertAlmostEqual(0.7, charisme_brute / charisme_personnage, 1)
        self.assertAlmostEqual(0.7, intelligence_brute / intelligence_personnage, 1)
        self.assertAlmostEqual(1.3, force_brute / force_personnage, 1)
        self.assertAlmostEqual(1.3, obstination_brute / obstination_personnage, 1)

    def test_choisir_action(self):

        object_list1 = [Objet(random.choice(words)) for _ in range(2)]
        object_list2 = [Objet(random.choice(words)) for _ in range(2)]
        object_list3 = [Objet(random.choice(words)) for _ in range(2)]

        b = Brute(names.get_full_name(), object_list1)

        Personnage.donner = PersonnageTest.donner
        Personnage.prendre = PersonnageTest.prendre
        Personnage.vendre = PersonnageTest.vendre
        Personnage.acheter = PersonnageTest.acheter
        Personnage.choisir_action = PersonnageTest.choisir_action

        # Personnage inconnu
        p1 = Personnage(names.get_full_name(), object_list2)
        self.assertEqual("PersonnageTest.prendre",b.choisir_action(p1))

        # Personnage connu avec niveau amitiÃ© <= 0.0
        b.amis[p1] = 0.0
        self.assertEqual("PersonnageTest.prendre",b.choisir_action(p1))
        b.amis[p1] = -0.5
        self.assertEqual("PersonnageTest.prendre",b.choisir_action(p1))

        # Personnage connu avec niveau amitiÃ© > 0.0
        b.amis[p1] = 0.5
        for i in range(50):
            self.assertTrue(b.choisir_action(p1) in [False, "PersonnageTest.acheter", "PersonnageTest.vendre"])

        # Charmeur inconnu
        c1 = Charmeur(names.get_full_name(), object_list3)
        self.assertFalse(b.choisir_action(c1))

        # Charmeur connu avec amitiÃ© <= 0.0
        b.amis[c1] = 0.0
        self.assertFalse(b.choisir_action(c1))
        b.amis[c1] = -0.5
        self.assertFalse(b.choisir_action(c1))

        # Charmeur connu avec amitiÃ© > 0.0
        b.amis[c1] = 0.5
        c1.charisme = b.charisme + 1
        self.assertEqual("PersonnageTest.donner", b.choisir_action(c1))

        c1.charisme = b.charisme - 1
        for i in range(50):
            self.assertTrue(b.choisir_action(c1) in [False, "PersonnageTest.acheter", "PersonnageTest.vendre"])

if __name__ == '__main__':
    unittest.main()
import unittest
import random

import names

from TP2.Charmeur import Charmeur
from TP2.Calculateur import Calculateur
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


class TestCalculateur(unittest.TestCase):
    def test_characteristiques(self):
        empathie_calc = 0
        empathie_personnage = 0
        intelligence_calc = 0
        intelligence_personnage = 0
        force_calc = 0
        force_personnage = 0
        obstination_calc = 0
        obstination_personnage = 0

        for i in range(1000):
            p = Personnage(names.get_full_name())
            empathie_personnage += p.empathie
            intelligence_personnage += p.intelligence
            force_personnage += p.force
            obstination_personnage += p.obstination

            b = Calculateur(names.get_full_name())
            empathie_calc += b.empathie
            intelligence_calc += b.intelligence
            force_calc += b.force
            obstination_calc += b.obstination

        self.assertAlmostEqual(0.7, empathie_calc / empathie_personnage, 1,
                               "L'attibut de `empathie` du `Calculateur` n'est pas 30% infÃ©rieur qu'un `Personnage` ordinaire")
        self.assertAlmostEqual(1.3, intelligence_calc / intelligence_personnage, 1,
                               "L'attibut de `intelligence` du `Calculateur` n'est pas 30% supÃ©rieur qu'un `Personnage` ordinaire")
        self.assertAlmostEqual(0.7, force_calc / force_personnage, 1,
                               "L'attibut de `force` du `Calculateur` n'est pas 30% infÃ©rieur qu'un `Personnage` ordinaire")
        self.assertAlmostEqual(1.3, obstination_calc / obstination_personnage, 1,
                               "L'attibut de `obstination` du `Calculateur` n'est pas 30% supÃ©rieur qu'un `Personnage` ordinaire")

    def test_choisir_action(self):

        Personnage.donner = PersonnageTest.donner
        Personnage.prendre = PersonnageTest.prendre
        Personnage.vendre = PersonnageTest.vendre
        Personnage.acheter = PersonnageTest.acheter
        Personnage.choisir_action = PersonnageTest.choisir_action

        Calculateur.vendre = PersonnageTest.vendre
        Calculateur.acheter = PersonnageTest.acheter

        #
        # Si ses points de vie sont infÃ©rieurs Ã  10 il ne choisira jamais l'action prendre ;
        # si sa force est supÃ©rieure Ã  celle de son adversaire, il prendra un de ses objets ;
        # sinon, si son interlocuteur est un Charmeur il lui vendra un objet ;
        # sinon, si son interlocuteur lui est connu et son niveau d'amitiÃ© est infÃ©rieur Ã  zÃ©ro, il lui fera un don ;
        # sinon il ne fait rien dans 50% des cas ou prendra une action alÃ©atoire dans les 50% d'autres cas.
        #

        # Personnage quelconque (connu ou inconnu, ami ou pas)
        for _ in range(1000):
            c = Calculateur(names.get_full_name(), [Objet(random.choice(words)) for _ in range(2)])
            p1 = Personnage(names.get_full_name(), [Objet(random.choice(words)) for _ in range(2)])

            if random.randint(0, 1):
                c.amis[p1] = 2 * random.random() - 1
            action = c.choisir_action(p1)

            if c.pv < 10:
                self.assertNotEqual("PersonnageTest.prendre", action,
                                    "Lorsque les points de vie du 'Calculateur` sont infÃ©rieurs Ã  10, l'action ne peut pas Ãªtre 'prendre'.")

            if c.force > p1.force and not c.pv < 10:
                self.assertEqual("PersonnageTest.prendre", action,
                                 "Lorsque la force du 'Calculateur` est supÃ©rieure, l'action doit Ãªtre 'prendre'.")
            elif isinstance(p1, Charmeur):
                self.assertEqual("PersonnageTest.vendre", action,
                                 "Lorsque l'adversaire du 'Calculateur` est un 'Charmeur', l'action doit Ãªtre 'vendre'.")
            elif p1 in c.amis and c.amis[p1] <= 0:
                self.assertEqual("PersonnageTest.donner", action,
                                 "Lorsque l'adversaire du 'Calculateur` est connu avec une amitiÃ© <= 0, l'action doit Ãªtre 'donner'.")
            else:
                inaction = 0
                actions = {"PersonnageTest.donner": 0, "PersonnageTest.vendre": 0, "PersonnageTest.acheter": 0,
                           "PersonnageTest.prendre": 0}

                runs = 1000
                for _ in range(runs):
                    action = c.choisir_action(p1)
                    if not action:
                        inaction += 1
                    else:
                        self.assertTrue(action in actions.keys(),
                                        f"Par dÃ©faut l'action du Calculateur doit Ãªtre parmi ['donner', 'vendre', 'acheter'] et non {action}.")
                        actions[action] += 1

                self.assertAlmostEqual(0.5, inaction / runs, 1,
                                       "Par dÃ©faut, dans 50% des cas le `Calculateur` doit ne rien faire.")
                self.assertAlmostEqual(0.5 / 4.0, actions["PersonnageTest.donner"] / runs, 1,
                                       "Par dÃ©faut, dans 16.6% le `Calculateur` doit faire un don.")
                self.assertAlmostEqual(0.5 / 4.0, actions["PersonnageTest.vendre"] / runs, 1,
                                       "Par dÃ©faut, dans 16.6% le `Calculateur` doit vendre.")
                self.assertAlmostEqual(0.5 / 4.0, actions["PersonnageTest.acheter"] / runs, 1,
                                       "Par dÃ©faut, dans 16.6% le `Calculateur` doit acheter.")
                self.assertAlmostEqual(0.5 / 4.0, actions["PersonnageTest.prendre"] / runs, 1,
                                       "Par dÃ©faut, dans 16.6% le `Calculateur` doit acheter.")


if __name__ == '__main__':
    unittest.main()
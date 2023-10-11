import unittest
import random

import names

from TP2.Objet import Objet
from TP2.Personnage import Personnage

words = open('/etc/dictionaries-common/words').readlines()

class ObjectInteractionTest(unittest.TestCase):

    def test_ObjectAttribute(self):
        p = Personnage(names.get_full_name())

        self.assertEqual(p.objets, [], "Le constructeur par dÃ©faut de `Personnage` ne crÃ©e pas de liste d'objets vide")
        self.assertEqual(p.getObjets(), [], "`Personnage.getObjets()` ne retourne pas de liste d'objets vide")

        random_word = random.choice(words)
        o = Objet(random_word)
        self.assertEqual(o.nom, random_word, "Le constructeur de `Objet` n'enregistre pas correctement le nom")

        p.ajoutObjet(o)
        self.assertEqual(p.getObjets(), [o], "`Personnage.ajoutObjet()` ne fonctionne pas correctement")

        random_objects = [ Objet(random.choice(words)) for _ in range(10)]
        random_objects_copy = random_objects.copy()

        p = Personnage(names.get_full_name(), random_objects)
        self.assertEqual(p.getObjets(), random_objects, "Le constructeur de `Personnage` ne gÃ¨re pas correctement les objets")
        p.ajoutObjet(o)
        self.assertEqual(set(p.getObjets()), set(random_objects_copy+[o]), "`Personnage.ajoutObjet()` ne fonctionne pas correctement")
        self.assertNotEqual(p.getObjets(), random_objects, "`Personnage` ne gÃ¨re pas correctement la mutablitÃ© de la liste des objets")

        objets = p.getObjets()
        objets.append(Objet(random.choice(words)))
        self.assertNotEqual(p.getObjets(), objets, "`Personnage.getObjets` ne respecte pas les rÃ¨gles d'encapsulation")

        p = Personnage(random_word)
        self.assertEqual(p.objets, [], "Le constructeur de `Personnage` prend mal en compte la mutabilitÃ© des arguments par dÃ©faut")

if __name__ == '__main__':
    unittest.main()
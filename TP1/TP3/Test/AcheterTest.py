import unittest
import random

import names

from TP2.Objet import Objet
from TP2.Personnage import Personnage

words = open('/etc/dictionaries-common/words').readlines()


class AcheterTest(unittest.TestCase):

    def test_acheter(self):
        random_objects1 = [Objet(random.choice(words), random.randint(1, 10)) for _ in range(5)]
        random_objects1_copy = random_objects1.copy()
        random_objects2 = [Objet(random.choice(words), random.randint(1, 10)) for _ in range(5)]
        random_objects2_copy = random_objects2.copy()

        p1 = Personnage(names.get_full_name(), random_objects1)
        p2 = Personnage(names.get_full_name(), random_objects2)

        p1bis = Personnage(names.get_full_name(), random_objects1_copy)
        p2bis = Personnage(names.get_full_name(), random_objects2_copy)

        o = random.choice(p1.getObjets())

        p1.vendre(o, p2)
        p2bis.acheter(o, p1bis)

        self.assertEqual(p1.getObjets(), p1bis.getObjets())
        self.assertEqual(p2.getObjets(), p2bis.getObjets())

        self.assertTrue(p2bis in p1bis.amis)
        self.assertEqual(0, p1bis.amis[p2bis])
        self.assertTrue(p1bis in p2bis.amis)
        self.assertEqual(0, p2bis.amis[p1bis])

        self.assertEqual(p1.richesse, p1bis.richesse)
        self.assertEqual(p2.richesse, p2bis.richesse)

        p1_objects = p1.getObjets().copy()
        p2_objects = p2.getObjets().copy()

        self.assertFalse(p1.acheter(random.choice(p1_objects), p2))
        self.assertEqual(p1.getObjets(), p1_objects)
        self.assertEqual(p2.getObjets(), p2_objects)

if __name__ == '__main__':
    unittest.main()
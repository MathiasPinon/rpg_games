import unittest
import random

import names

from TP2.Objet import Objet
from TP2.Personnage import Personnage

words = open('/etc/dictionaries-common/words').readlines()


class VendreTest(unittest.TestCase):

    def test_vendre(self):
        random_objects1 = [Objet(random.choice(words), random.randint(1, 10)) for _ in range(5)]
        random_objects1_copy = random_objects1.copy()
        random_objects2 = [Objet(random.choice(words), random.randint(1, 10)) for _ in range(5)]
        random_objects2_copy = random_objects2.copy()

        p1 = Personnage(names.get_full_name(), random_objects1)
        p2 = Personnage(names.get_full_name(), random_objects2)

        o = random.choice(p1.getObjets())
        p2_objects = p2.getObjets().copy()

        richesse1 = p1.richesse
        richesse2 = p2.richesse

        self.assertTrue(p1.vendre(o, p2))
        self.assertEqual(richesse1 + o.valeur, p1.richesse)
        self.assertEqual(richesse2 - o.valeur, p2.richesse)
        self.assertTrue(o not in p1.getObjets())
        self.assertTrue(o in p2.getObjets())
        self.assertEqual(set(p2_objects + [o]), set(p2.getObjets()))
        self.assertEqual(set(p1.getObjets() + p2.getObjets()), set(random_objects1_copy + random_objects2_copy))
        self.assertCountEqual(p1.getObjets() + p2.getObjets(), random_objects1 + random_objects2)
        self.assertTrue(p2 in p1.amis)
        self.assertEqual(0, p1.amis[p2])
        self.assertTrue(p1 in p2.amis)
        self.assertEqual(0, p2.amis[p1])

        p1.amis[p2] = 0.13
        p2.amis[p1] = -0.87
        o = random.choice(p1.getObjets())
        self.assertTrue(p1.vendre(o, p2))
        self.assertEqual(p1.amis[p2], 0.13)
        self.assertEqual(p2.amis[p1], -0.87)

        p1_objects = p1.getObjets().copy()
        p2_objects = p2.getObjets().copy()

        self.assertFalse(p1.vendre(random.choice(p2_objects), p2))
        self.assertEqual(p1.getObjets(), p1_objects)
        self.assertEqual(p2.getObjets(), p2_objects)


if __name__ == '__main__':
    unittest.main()
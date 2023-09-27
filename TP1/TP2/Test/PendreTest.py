import unittest
import random

import names

from TP2.Objet import Objet
from TP2.Personnage import Personnage

words = open('/etc/dictionaries-common/words').readlines()


class PrendreTest(unittest.TestCase):

    def test_prendre(self):
        random_objects1 = [Objet(random.choice(words), random.randint(1, 10)) for _ in range(5)]
        random_objects1_copy = random_objects1.copy()
        random_objects2 = [Objet(random.choice(words), random.randint(1, 10)) for _ in range(5)]
        random_objects2_copy = random_objects2.copy()

        p1 = Personnage(names.get_full_name(), random_objects1)
        p1.force = 10
        pv1 = p1.pv

        p2 = Personnage(names.get_full_name(), random_objects2)
        p2.force = 5
        pv2 = p2.pv

        o1 = random.choice(p1.getObjets())
        o2 = random.choice(p2.getObjets())
        self.assertTrue(o2 in p2.getObjets())
        p1_objects = p1.getObjets().copy()
        p2_objects = p2.getObjets().copy()

        # p1 n'a pas assez d'obstination
        p2.force = 10
        p1.obstination = p2.obstination-1
        self.assertFalse(p1.prendre(o2, p2))
        self.assertEqual(p1.getObjets(), p1_objects)
        self.assertEqual(p2.getObjets(), p2_objects)
        self.assertEqual(pv1, p1.pv)
        self.assertEqual(pv2, p2.pv)

        # p1 a assez d'obstination
        p1.obstination += 2
        self.assertTrue(o2 in p2.getObjets())
        self.assertTrue(p1.prendre(o2, p2))
        self.assertEqual(0, pv1-p1.pv)
        self.assertEqual(0, pv2-p2.pv)
        self.assertTrue(o2 in p1.getObjets())
        self.assertTrue(o2 not in p2.getObjets())
        self.assertEqual(set(p1_objects + [o2]), set(p1.getObjets()))
        self.assertEqual(set(p1.getObjets() + p2.getObjets()), set(random_objects1_copy + random_objects2_copy))
        self.assertCountEqual(p1.getObjets() + p2.getObjets(), random_objects1 + random_objects2)

        # p1 a assez de force
        p1.obstination -= 2
        p1.force += 5
        o2 = random.choice(p2.getObjets())
        p1_objects = p1.getObjets().copy()
        p2_objects = p2.getObjets().copy()

        self.assertTrue(o2 in p2.getObjets())
        self.assertTrue(p1.prendre(o2, p2))
        self.assertEqual(5, pv1-p1.pv)
        self.assertEqual(5, pv2-p2.pv)
        self.assertTrue(o2 in p1.getObjets())
        self.assertTrue(o2 not in p2.getObjets())
        self.assertEqual(set(p1_objects + [o2]), set(p1.getObjets()))
        self.assertEqual(set(p1.getObjets() + p2.getObjets()), set(random_objects1_copy + random_objects2_copy))
        self.assertCountEqual(p1.getObjets() + p2.getObjets(), random_objects1 + random_objects2)

        self.assertTrue(p1 in p2.amis)
        self.assertEqual(-1, p2.amis[p1])
        self.assertTrue(p2 in p1.amis)
        self.assertEqual(0, p1.amis[p2])

        p1.amis[p2] = 0.13
        p2.amis[p1] = -0.87
        o = random.choice(p2.getObjets())
        self.assertTrue(p1.prendre(o, p2))
        self.assertEqual(0.13, p1.amis[p2])
        self.assertEqual(-1, p2.amis[p1])

if __name__ == '__main__':
    unittest.main()
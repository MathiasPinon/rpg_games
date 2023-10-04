import random
import unittest

import names

from TP2.Objet import Objet
from TP2.Personnage import Personnage

words = open('/etc/dictionaries-common/words').readlines()


class TestAccesseurs(unittest.TestCase):

    def test_pv(self):
        for _ in range(10):
            p1 = Personnage(names.get_full_name())
            self.assertEqual(p1.pv,p1.getPV(), "La mÃ©thode `Personnage.getPV()` ne renvoie pas la bonne valeur")

    def test_richesse(self):
        for _ in range(10):
            object_list = [Objet(random.choice(words), random.randint(1,30)) for _ in range(10)]
            object_list_value = sum([o.valeur for o in object_list])

            p1 = Personnage(names.get_full_name(), object_list)
            self.assertEqual(p1.richesse + object_list_value,p1.getRichesse(), "La mÃ©thode `Personnage.getRichesse()` ne renvoie pas la bonne valeur")

    def test_amis(self):
        person_list = [Personnage(names.get_full_name()) for _ in range(10)]

        for p in person_list:
            s = set()
            for _ in range(random.randrange(0,5)):
                s.add(random.choice(person_list))
                for a in s:
                    p.amis[a] = random.random()*2-1
            self.assertDictEqual(p.amis, p.getAmis(), "`Personnage.getAmis()` ne renvoie pas la bonne valeur")  # add assertion here


if __name__ == '__main__':
    unittest.main()
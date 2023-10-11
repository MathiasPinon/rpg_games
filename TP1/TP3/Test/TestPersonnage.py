import random
import unittest

from TP3.Negociateur import Negociateur
from TP3.Objet import Objet
from TP3.RandomPersonnage import create_RandomPersonnage


class ObjetNul(Objet):
    """
    Objet qui ne sert Ã  rien, et qui ne s'acquiÃ¨re ou ne se cÃ¨de pas
    """

    def __init__(self, n=None, v=10, **kwargs):
        super().__init__(n, v, **kwargs)

    def effetAcquisition(self, p):
        return lambda *args, **kwargs: None

    def effetCession(self, p):
        return lambda *args, **kwargs: None


class AcquisitionCessionTest(unittest.TestCase):

    def test_cessionNul(self):
        """
        Teste si la fonction `Objet.effetCession()` est bien utilisÃ©e avec un objet de test ne pouvant pas Ãªtre
        cÃ©dÃ© ni acquis.
        :return: None
        """
        o = ObjetNul()
        for _ in range(100):
            p1 = create_RandomPersonnage()
            richesse_p1 = p1.richesse

            p2 = create_RandomPersonnage()
            richesse_p2 = p2.richesse

            if isinstance(p1.getObjets(), list):
                p1.objets.append(o)
            elif isinstance(p1.getObjets(), set):
                p1.objets.add(o)
            else:
                raise TypeError(
                    f"{type(p1)}.objets est ni de type 'list', ni de type 'set' mais de type {type(p1.getObjets())}")

            o.effetCession(p1)()
            self.assertTrue(o in p1.getObjets())

            self.assertTrue(p1.donner(o, p2),
                            f"Un personnage de type {type(p1)} possÃ¨de un objet et pourtant l'opÃ©ration de `donner` Ã©choue")
            self.assertTrue(o in p1.getObjets(),
                            f"L'opÃ©ration `donner` de {type(p1)} utilise mal `Objet.effetCession()` pour enlever l'objet de `self.objets`. ")
            self.assertFalse(o in p2.getObjets(),
                             f"L'opÃ©ration `donner` de {type(p1)} utilise mal `Objet.effetAcquisition()` pour ajouter l'objet dans `autre.objets`. ")
            self.assertEqual(richesse_p1, p1.richesse,
                             f"L'opÃ©ration `donner` de {type(p1)} utilise mal `Objet.effetCession()` pour ajuster `self._richesse`. ")
            self.assertEqual(richesse_p2, p2.richesse,
                             f"L'opÃ©ration `donner` de {type(p1)} utilise mal `Objet.effetAcquisition()` pour ajuster `autre._richesse`. ")

            self.assertTrue(p1.vendre(o, p2),
                            f"Un personnage de type {type(p1)} possÃ¨de un objet et pourtant l'opÃ©ration de `vendre` Ã©choue")
            self.assertTrue(o in p1.getObjets(),
                            f"L'opÃ©ration `vendre` de {type(p1)} utilise mal `Objet.effetCession()` pour enlever l'objet de `self.objets`. ")
            self.assertFalse(o in p2.getObjets(),
                             f"L'opÃ©ration `vendre` de {type(p1)} utilise mal `Objet.effetAcquisition()` pour ajouter l'objet dans `autre.objets`. ")
            self.assertEqual(richesse_p1, p1.richesse,
                             f"L'opÃ©ration `vendre` de {type(p1)} utilise mal `Objet.effetCession()` pour ajuster `self._richesse`. ")
            self.assertEqual(richesse_p2, p2.richesse,
                             f"L'opÃ©ration `vendre` de {type(p1)} utilise mal `Objet.effetAcquisition()` pour ajuster `autre._richesse`.")

    def test_cessionNormal(self):
        """
        Teste si la fonction `Objet.effetCession()` est bien utilisÃ©e avec un objet normal
        :return: None
        """
        for _ in range(100):
            p1 = create_RandomPersonnage()
            richesse_p1 = p1._richesse

            p2 = create_RandomPersonnage()
            richesse_p2 = p2._richesse

            liste_objets_p1 = list(p1.getObjets())
            self.assertFalse(liste_objets_p1 is None or liste_objets_p1 == [])

            o = random.choice(liste_objets_p1)
            liste_objets_p1.remove(o)

            self.assertTrue(p1.donner(o, p2),
                            f"Un personnage de type {type(p1)} possÃ¨de un objet et pourtant l'opÃ©ration de `donner` Ã©choue")
            self.assertFalse(o in p1.getObjets(),
                            f"L'opÃ©ration `donner` de {type(p1)} utilise mal `Objet.effetCession()` pour enlever l'objet de `self.objets`. ")
            self.assertTrue(o in p2.getObjets(),
                             f"L'opÃ©ration `donner` de {type(p1)} utilise mal `Objet.effetAcquisition()` pour ajouter l'objet dans `autre.objets`. ")
            self.assertEqual(richesse_p1, p1._richesse,
                             f"L'opÃ©ration `donner` de {type(p1)} utilise mal `Objet.effetCession()` pour ajuster `self._richesse`. ")
            self.assertEqual(richesse_p2, p2._richesse,
                             f"L'opÃ©ration `donner` de {type(p1)} utilise mal `Objet.effetAcquisition()` pour ajuster `autre._richesse`. ")

            o = random.choice(liste_objets_p1)
            liste_objets_p1.remove(o)

            marge = 0.0
            if isinstance(p1, Negociateur) and hasattr(p1, 'marge'):
                marge = random.random()
                p1.marge = marge

            self.assertTrue(p1.vendre(o, p2),
                            f"Un personnage de type {type(p1)} possÃ¨de un objet et pourtant l'opÃ©ration de `vendre` Ã©choue")
            self.assertFalse(o in p1.getObjets(),
                            f"L'opÃ©ration `vendre` de {type(p1)} utilise mal `Objet.effetCession()` pour enlever l'objet de `self.objets`. ")
            self.assertTrue(o in p2.getObjets(),
                             f"L'opÃ©ration `vendre` de {type(p1)} utilise mal `Objet.effetAcquisition()` pour ajouter l'objet dans `autre.objets`. ")
            self.assertEqual(richesse_p1+(o.valeur*(1+marge)), p1._richesse,
                             f"L'opÃ©ration `vendre` de {type(p1)} utilise mal `Objet.effetCession()` pour ajuster `self._richesse`. ")
            self.assertEqual(richesse_p2-(o.valeur*(1+marge)), p2._richesse,
                             f"L'opÃ©ration `vendre` de {type(p1)} utilise mal `Objet.effetAcquisition()` pour ajuster `autre._richesse`.")


    def test_acquisitionNul(self):
        """
        Teste si la fonction `Objet.effetAcquisition()` est bien implÃ©mentÃ©e et bien utilisÃ©e avec un objet de test ne
        pouvant pas Ãªtre cÃ©dÃ© ni acquis.
        :return: None
        """
        o = ObjetNul()
        for _ in range(100):
            p1 = create_RandomPersonnage()
            richesse_p1 = p1.richesse

            p2 = create_RandomPersonnage()
            richesse_p2 = p2.richesse

            p1._force = p2.force + 1

            if isinstance(p2.getObjets(), list):
                p2.objets.append(o)
            elif isinstance(p2.getObjets(), set):
                p2.objets.add(o)
            else:
                raise TypeError(
                    f"{type(p1)}.objets est ni de type 'list', ni de type 'set' mais de type {type(p1.getObjets())}")

            o.effetAcquisition(p2)()
            self.assertTrue(o in p2.getObjets())

            self.assertTrue(p1.prendre(o, p2),
                            f"Un personnage de type {type(p2)} possÃ¨de un objet et pourtant l'opÃ©ration de `prendre` Ã©choue")
            self.assertFalse(o in p1.getObjets(),
                             f"L'opÃ©ration `prendre` de {type(p1)} utilise mal `Objet.effetCession()` pour enlever l'objet de `self.objets`. ")
            self.assertTrue(o in p2.getObjets(),
                            f"L'opÃ©ration `prendre` de {type(p1)} utilise mal `Objet.effetAcquisition()` pour ajouter l'objet dans `autre.objets`. ")
            self.assertEqual(richesse_p1, p1.richesse,
                             f"L'opÃ©ration `prendre` de {type(p1)} utilise mal `Objet.effetCession()` pour ajuster `self._richesse`. ")
            self.assertEqual(richesse_p2, p2.richesse,
                             f"L'opÃ©ration `prendre` de {type(p1)} utilise mal `Objet.effetAcquisition()` pour ajuster `autre._richesse`. ")

            self.assertTrue(p1.acheter(o, p2),
                            f"Un personnage de type {type(p2)} possÃ¨de un objet et pourtant l'opÃ©ration de `acheter` Ã©choue")
            self.assertFalse(o in p1.getObjets(),
                             f"L'opÃ©ration `acheter` de {type(p1)} utilise mal `Objet.effetCession()` pour enlever l'objet de `self.objets`. ")
            self.assertTrue(o in p2.getObjets(),
                            f"L'opÃ©ration `acheter` de {type(p1)} utilise mal `Objet.effetAcquisition()` pour ajouter l'objet dans `autre.objets`. ")
            self.assertEqual(richesse_p1, p1.richesse,
                             f"L'opÃ©ration `acheter` de {type(p1)} utilise mal `Objet.effetCession()` pour ajuster `self._richesse`. ")
            self.assertEqual(richesse_p2, p2.richesse,
                             f"L'opÃ©ration `acheter` de {type(p1)} utilise mal `Objet.effetAcquisition()` pour ajuster `autre._richesse`. ")

    def test_acquisitionNormal(self):
        """
        Teste si la fonction `Objet.effetAcquisition()` est bien implÃ©mentÃ©e et bien utilisÃ©e avec un objet normal
        :return: None
        """
        for _ in range(100):
            p1 = create_RandomPersonnage()
            richesse_p1 = p1._richesse

            p2 = create_RandomPersonnage()
            richesse_p2 = p2._richesse

            p1._force = p2.force + 1

            liste_objets_p2 = list(p2.getObjets())
            self.assertFalse(liste_objets_p2 is None or liste_objets_p2 == [])

            o = random.choice(liste_objets_p2)
            liste_objets_p2.remove(o)

            self.assertTrue(p1.prendre(o, p2),
                            f"Un personnage de type {type(p2)} possÃ¨de un objet et pourtant l'opÃ©ration de `prendre` Ã©choue")
            self.assertTrue(o in p1.getObjets(),
                             f"L'opÃ©ration `prendre` de {type(p1)} utilise mal `Objet.effetCession()` pour enlever l'objet de `self.objets`. ")
            self.assertFalse(o in p2.getObjets(),
                            f"L'opÃ©ration `prendre` de {type(p1)} utilise mal `Objet.effetAcquisition()` pour ajouter l'objet dans `autre.objets`. ")
            self.assertEqual(richesse_p1, p1._richesse,
                             f"L'opÃ©ration `prendre` de {type(p1)} utilise mal `Objet.effetCession()` pour ajuster `self._richesse`. ")
            self.assertEqual(richesse_p2, p2._richesse,
                             f"L'opÃ©ration `prendre` de {type(p1)} utilise mal `Objet.effetAcquisition()` pour ajuster `autre._richesse`. ")

            o = random.choice(liste_objets_p2)
            liste_objets_p2.remove(o)
            richesse_p1 = p1._richesse
            richesse_p2 = p2._richesse

            marge = 0.0
            if isinstance(p1, Negociateur) and hasattr(p1, 'marge'):
                marge = random.random()
                p1.marge = marge

            self.assertTrue(p1.acheter(o, p2),
                            f"Un personnage de type {type(p2)} possÃ¨de un objet et pourtant l'opÃ©ration de `acheter` Ã©choue")
            self.assertTrue(o in p1.getObjets(),
                             f"L'opÃ©ration `acheter` de {type(p1)} utilise mal `Objet.effetCession()` pour enlever l'objet de `self.objets`. ")
            self.assertFalse(o in p2.getObjets(),
                            f"L'opÃ©ration `acheter` de {type(p1)} utilise mal `Objet.effetAcquisition()` pour ajouter l'objet dans `autre.objets`. ")
            self.assertEqual(richesse_p1-(o.valeur*(1-marge)), p1._richesse,
                             f"L'opÃ©ration `acheter` de {type(p1)} utilise mal `Objet.effetCession()` pour ajuster `self._richesse`. ")
            self.assertEqual(richesse_p2+(o.valeur*(1-marge)), p2._richesse,
                             f"L'opÃ©ration `acheter` de {type(p1)} utilise mal `Objet.effetAcquisition()` pour ajuster `autre._richesse`. ")


if __name__ == '__main__':
    unittest.main()
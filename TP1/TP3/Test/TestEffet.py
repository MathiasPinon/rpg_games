import random
import unittest

from TP2.Objet import Objet
from RandomPersonnage import create_RandomPersonnage


class AcquisitionCessionTest(unittest.TestCase):

    def test_cessionNormal(self):
        """
        Teste si la fonction `Objet.effetCession()` est bien utilisÃ©e avec un objet normal
        :return: None
        """
        for _ in range(100):
            p1 = create_RandomPersonnage()
            richesse_p1 = p1.richesse

            liste_objets_p1 = list(p1.getObjets())
            self.assertFalse(liste_objets_p1 is None or liste_objets_p1 == [])

            o = random.choice(liste_objets_p1)
            liste_objets_p1.remove(o)

            o.effetCession(p1)()
            self.assertFalse(o in p1.getObjets(),
                             f"`Objet.effetCession({type(p1)}()` n'enlÃ¨ve pas l'objet de `Personnage.objets`.")
            self.assertSetEqual(set(liste_objets_p1), set(p1.getObjets()),
                                f"`Objet.effetCession({type(p1)}()` a des effets de bord indÃ©sirables sur `Personnage.objets`.")
            self.assertEqual(richesse_p1 + o.valeur, p1.richesse,
                             f"`Objet.effetCession({type(p1)}()` n'ajuste pas correctement `Personnage._richesse`.")

            richesse_p1 = p1.richesse
            o = random.choice(liste_objets_p1)
            liste_objets_p1.remove(o)

            prix_objet = 3.33333
            o.effetCession(p1)(prix=prix_objet)
            self.assertFalse(o in p1.getObjets(),
                             f"`Objet.effetCession({type(p1)}(prix=value)` n'enlÃ¨ve pas l'objet de `Personnage.objets`.")
            self.assertSetEqual(set(liste_objets_p1), set(p1.getObjets()),
                                f"`Objet.effetCession({type(p1)}(prix=value)` a des effets de bord indÃ©sirables sur `Personnage.objets`.")
            self.assertEqual(richesse_p1 + prix_objet, p1.richesse,
                             f"`Objet.effetCession({type(p1)}(prix=value)` n'ajuste pas correctement `Personnage._richesse`.")

    def test_acquisitionNormal(self):
        """
        Teste si la fonction `Objet.effetAcquisition()` est bien implÃ©mentÃ©e et bien utilisÃ©e avec un objet normal
        :return: None
        """
        for _ in range(100):
            p1 = create_RandomPersonnage()
            richesse_p1 = p1.richesse

            liste_objets_p1 = list(p1.getObjets())
            self.assertFalse(liste_objets_p1 is None or liste_objets_p1 == [])

            o = Objet('Test 1')
            o.effetAcquisition(p1)()
            self.assertTrue(o in p1.getObjets(),
                            f"`Objet.effetAcquisition({type(p1)}()` n'ajoute pas l'objet Ã  `Personnage.objets`.")

            liste_objets_p1.append(o)
            self.assertSetEqual(set(liste_objets_p1), set(p1.getObjets()),
                                f"`Objet.effetAcquisition({type(p1)}()` a des effets de bord indÃ©sirables sur `Personnage.objets`.")
            self.assertEqual(richesse_p1 - o.valeur, p1.richesse,
                             f"`Objet.effetAcquisition({type(p1)}()` n'ajuste pas correctement `Personnage._richesse`.")

            richesse_p1 = p1.richesse
            o = Objet('Test 1')
            prix_objet = 3.33333
            o.effetAcquisition(p1)(prix=prix_objet)
            self.assertTrue(o in p1.getObjets(),
                            f"`Objet.effetAcquisition({type(p1)}(prix=value)` n'ajoute pas l'objet Ã  `Personnage.objets`.")
            liste_objets_p1.append(o)
            self.assertSetEqual(set(liste_objets_p1), set(p1.getObjets()),
                                f"`Objet.effetAcquisition({type(p1)}(prix=value)` a des effets de bord indÃ©sirables sur `Personnage.objets`.")
            self.assertEqual(richesse_p1 - prix_objet, p1.richesse,
                             f"`Objet.effetAcquisition({type(p1)}(prix=value)` n'ajuste pas correctement `Personnage._richesse`.")


if __name__ == '__main__':
    unittest.main()
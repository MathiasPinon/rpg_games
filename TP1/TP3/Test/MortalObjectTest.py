import unittest

from TP3.ObjetMortel import ObjetMortel
from TP3.RandomPersonnage import create_RandomPersonnage


class MortalObjectTest(unittest.TestCase):
    def test_cession(self):
        """
        Teste si la fonction `Objet.effetCession()` est bien implantée pour `RandomObjet
        :return: None
        """
        for _ in range(100):
            p1 = create_RandomPersonnage()
            richesse_p1 = p1.richesse

            force_p1 = p1.force
            intelligence_p1 = p1.intelligence
            empathie_p1 = p1.empathie
            obstination_p1 = p1.obstination
            charisme_p1 = p1.charisme

            liste_objets_p1 = list(p1.getObjets())
            self.assertFalse(liste_objets_p1 is None or liste_objets_p1 == [])

            o = ObjetMortel('Test Objet 1')
            if hasattr(p1, '_objets'):
                objets = p1._objets
            elif hasattr(p1, 'objets'):
                objets = p1.objets
            else:
                raise AttributeError(f"{type(p1)} n'a pas d'attribut `objets` ou `_objets`.")

            if isinstance(objets,list):
                objets.append(o)
            else:
                objets.add(o)

            o.effetCession(p1)()
            self.assertFalse(o in p1.getObjets(),
                             f"`{type(o)}.effetCession({type(p1)})()` n'enlève pas l'objet de `Personnage.objets`.")
            self.assertSetEqual(set(liste_objets_p1), set(p1.getObjets()),
                                f"`{type(o)}.effetCession({type(p1)})()` a des effets de bord indésirables sur `Personnage.objets`.")
            self.assertEqual(richesse_p1 + o.valeur, p1.richesse,
                             f"`{type(o)}.effetCession({type(p1)})()` n'ajuste pas correctement `Personnage._richesse`.")

            self.assertEqual(force_p1, p1.force,
                             f"`Objet.effetCession({type(p1)})()` modifie `Personnage._force`.")
            self.assertEqual(intelligence_p1, p1.intelligence,
                             f"`Objet.effetCession({type(p1)})()` modifie `Personnage._intelligence`.")
            self.assertEqual(empathie_p1, p1.empathie,
                             f"`Objet.effetCession({type(p1)})()` modifie `Personnage._empathie`.")
            self.assertEqual(obstination_p1, p1.obstination,
                             f"`Objet.effetCession({type(p1)})()` modifie `Personnage._obstination`.")
            self.assertEqual(charisme_p1, p1.charisme,
                             f"`Objet.effetCession({type(p1)})()` modifie `Personnage._charisme`.")

            richesse_p1 = p1.richesse
            o = ObjetMortel('Test Objet 2')

            if isinstance(objets,list):
                objets.append(o)
            else:
                objets.add(o)

            prix_objet = 3.33333
            o.effetCession(p1)(prix=prix_objet)
            self.assertFalse(o in p1.getObjets(),
                             f"`{type(o)}.effetCession({type(p1)})(prix=value)` n'enlève pas l'objet de `Personnage.objets`.")
            self.assertSetEqual(set(liste_objets_p1), set(p1.getObjets()),
                                f"`{type(o)}.effetCession({type(p1)})(prix=value)` a des effets de bord indésirables sur `Personnage.objets`.")
            self.assertEqual(richesse_p1 + prix_objet, p1.richesse,
                             f"`{type(o)}.effetCession({type(p1)})(prix=value)` n'ajuste pas correctement `Personnage._richesse`.")

    def test_acquisition(self):
        """
        Teste si la fonction `Objet.effetAcquisition()` est bien implantée pour `RandomObjet`
        :return: None
        """
        for _ in range(100):
            p1 = create_RandomPersonnage()
            richesse_p1 = p1.richesse

            force_p1 = p1.force
            intelligence_p1 = p1.intelligence
            empathie_p1 = p1.empathie
            obstination_p1 = p1.obstination
            charisme_p1 = p1.charisme

            liste_objets_p1 = list(p1.getObjets())
            self.assertFalse(liste_objets_p1 is None or liste_objets_p1 == [])

            o = ObjetMortel('Acquisition Test 1')
            o.effetAcquisition(p1)()
            self.assertTrue(o in p1.getObjets(),
                            f"`Objet.effetAcquisition({type(p1)})()` n'ajoute pas l'objet à `Personnage.objets`.")

            liste_objets_p1.append(o)
            self.assertSetEqual(set(liste_objets_p1), set(p1.getObjets()),
                                f"`Objet.effetAcquisition({type(p1)})()` a des effets de bord indésirables sur `Personnage.objets`.")
            self.assertEqual(richesse_p1 - o.valeur, p1.richesse,
                             f"`Objet.effetAcquisition({type(p1)})()` n'ajuste pas correctement `Personnage._richesse`.")

            self.assertEqual(0, p1.force, f"`Objet.effetAcquisition({type(p1)})()` ne met pas `Personnage._force` à zéro.")
            self.assertEqual(0, p1.intelligence, f"`Objet.effetAcquisition({type(p1)})()` ne met pas `Personnage._intelligence` à zéro.")
            self.assertEqual(0, p1.empathie, f"`Objet.effetAcquisition({type(p1)})()` ne met pas `Personnage._empathie` à zéro.")
            self.assertEqual(0, p1.obstination, f"`Objet.effetAcquisition({type(p1)})()` ne met pas `Personnage._obstination` à zéro.")
            self.assertEqual(0, p1.charisme, f"`Objet.effetAcquisition({type(p1)})()` ne met pas `Personnage._charisme` à zéro.")
            self.assertEqual(0, p1.pv, f"`Objet.effetAcquisition({type(p1)})()` ne met pas `Personnage._pv` à zéro.")

            richesse_p1 = p1.richesse
            o = ObjetMortel('Acquisition Test 2')
            prix_objet = 3.33333
            o.effetAcquisition(p1)(prix=prix_objet)
            self.assertTrue(o in p1.getObjets(),
                            f"`Objet.effetAcquisition({type(p1)}(prix=value)` n'ajoute pas l'objet à `Personnage.objets`.")
            liste_objets_p1.append(o)
            self.assertSetEqual(set(liste_objets_p1), set(p1.getObjets()),
                                f"`Objet.effetAcquisition({type(p1)}(prix=value)` a des effets de bord indésirables sur `Personnage.objets`.")
            self.assertEqual(richesse_p1 - prix_objet, p1.richesse,
                             f"`Objet.effetAcquisition({type(p1)}(prix=value)` n'ajuste pas correctement `Personnage._richesse`.")


if __name__ == '__main__':
    unittest.main()

import string
import unittest
import random

from Class.Parser import Parser

alpha = string.ascii_letters + '_'
alphanum = alpha + string.digits


def generate_alphanum_token(length: int) -> str:
    '''
    Generates a valid alphanumeric token of given length.
    The token consists of `length` alphanumeric characters (including `_`) but does not start with a digit.

    :param length: length of the token to generate
    :return: a valid alphanumeric token of length `length`
    '''

    if length <= 0:
        return ''
    else:
        return random.choice(alpha) + ''.join(random.choice(alphanum) for i in range(length))


class ParserTest(unittest.TestCase):

    def test_Exemple1_Sujet(self):
        p = Parser()

        flux1 = 'a + b'
        flux2 = ' a + b'
        flux3 = 'a+b'
        flux4 = 'abcd'
        flux5 = '12ab'
        flux6 = 'ab12'
        flux7 = '@ab'

        self.assertEqual(p.get_token(flux1), ('a', ' + b'))
        self.assertEqual(p.get_token(flux2), ('a', ' + b'))
        self.assertEqual(p.get_token(flux3), ('a', '+b'))
        self.assertEqual(p.get_token(flux4), ('abcd', ''))
        self.assertEqual(p.get_token(flux5), ('12', 'ab'))
        self.assertEqual(p.get_token(flux6), ('ab12', ''))
        self.assertEqual(p.get_token(flux7), ('', '@ab'))

    def test_get_token_Whitespace(self):

        p = Parser()

        # Testing empty string
        self.assertEqual(p.get_token(''), ('', ''), "Le flux vide n'est pas correctement gÃ©rÃ©")

        # Testing whitespace only
        for i in range(10):
            flux = ' ' * random.randrange(1, 10)
            self.assertEqual(('', ''), p.get_token(flux), "Le flux composÃ© uniquement de blancs n'est pas correctement gÃ©rÃ©")

        # Testing whitespace preceding valid token
        for i in range(1000):
            token = generate_alphanum_token(random.randrange(1, 10))
            flux = '' + ' ' * random.randrange(10) + token

            self.assertEqual((token, ''), p.get_token(flux), "Le parseur ne gÃ¨re pas correctement les blancs en dÃ©but d'expression")

        # Testing whitespace following valid token
        for i in range(1000):
            token = generate_alphanum_token(random.randrange(1, 10))
            whitespace = '' + ' ' * random.randrange(10)
            flux = token + whitespace

            self.assertEqual((token, whitespace), p.get_token(flux), "Le parseur ne gÃ¨re pas correctement les blancs en fin d'expression")

    def test_get_token_SimpleToken(self):

        p = Parser()

        for i in range(1000):
            token = generate_alphanum_token(random.randrange(1, 10))
            self.assertEqual((token, ''), p.get_token(token), "Le parseur ne reconnaÃ®t pas correctement les chaÃ®nes alphanumÃ©riques")

    def test_get_token_NumberToken(self):

        p = Parser()

        for i in range(1000):
            token = generate_alphanum_token(random.randrange(1, 10))
            self.assertEqual((token, ''), p.get_token(token), "Le parseur ne reconnaÃ®t pas correctement les entiers")

    def test_get_token_DefaultOperator(self):

        default_operators = ['(', ')', '+', '-', '*', '/']
        p_def = Parser()
        alternative_operators = ['@', '#', '~', '[', ']', '&']
        p_alt = Parser(alternative_operators)

        for i in default_operators:
            token = i + ' '
            self.assertEqual((i, ' '), p_def.get_token(token), "Le parseur ne gÃ¨re pas correctement les caractÃ¨res spÃ©ciaux")
            self.assertEqual(('', token), p_alt.get_token(token), 'Le parseur ne gÃ¨re pas correctement des alphabets passÃ©s au constructeur')

            token = i+'_'
            self.assertEqual((i, '_'), p_def.get_token(token), "Le parseur ne gÃ¨re pas correctement la sÃ©paration entre caractÃ¨res spÃ©ciaux")
            self.assertEqual(('', token), p_alt.get_token(token), 'Le parseur ne gÃ¨re pas correctement des alphabets passÃ©s au constructeur')

        for i in alternative_operators:
            token = i + ' '
            self.assertEqual(('', token), p_def.get_token(token), "Le parseur ne gÃ¨re pas correctement les caractÃ¨res spÃ©ciaux hors alphabet")
            self.assertEqual((i, ' '), p_alt.get_token(token), 'Le parseur ne gÃ¨re pas correctement des alphabets passÃ©s au constructeur')

            token = i+'_'
            self.assertEqual(('', token), p_def.get_token(token), "Le parseur ne gÃ¨re pas correctement les caractÃ¨res spÃ©ciaux hors alphabet")
            self.assertEqual((i, '_'), p_alt.get_token(token), 'Le parseur ne gÃ¨re pas correctement des alphabets passÃ©s au constructeur')


    def test_IsInAlphabet(self):

        default_operators = ['(', ')', '+', '-', '*', '/']
        p_def = Parser()
        alternative_operators = ['@', '#', '~', '[', ']', '&']
        p_alt = Parser(alternative_operators)

        for i in default_operators:
            self.assertTrue(p_def.is_in_alphabet(i), "Le parseur ne gÃ¨re pas correctement les caractÃ¨res spÃ©ciaux de l'alphabet")
            self.assertFalse(p_alt.is_in_alphabet(i), 'Le parseur ne gÃ¨re pas correctement des alphabets passÃ©s au constructeur')

        for i in alternative_operators:
            self.assertFalse(p_def.is_in_alphabet(i), "Le parseur ne gÃ¨re pas correctement les caractÃ¨res spÃ©ciaux hors alphabet")
            self.assertTrue(p_alt.is_in_alphabet(i), 'Le parseur ne gÃ¨re pas correctement des alphabets passÃ©s au constructeur')

    def test_IsOperator(self):

        operators = ['+', '-', '*', '/']
        non_operators = ['_', '(', ')', ' ']
        non_alphabet = ['@', '#', '~', '[', ']', '&']
        p = Parser()

        for i in operators:
            self.assertTrue(p.is_operator(i))

        for i in operators:
            for j in operators:
                self.assertFalse(p.is_operator(i+j))

        for i in non_operators:
            self.assertFalse(p.is_operator(i))

        for i in non_alphabet:
            self.assertFalse(p.is_operator(i))


if __name__ == '__main__':
    unittest.main()
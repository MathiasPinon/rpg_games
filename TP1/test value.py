import random
import string
import unittest

from Class.Expression import Expression, Value, Variable

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


def generate_num_token(length: int) -> str:
    '''
    Generates a valid numeric token of given length.
    The token consists of `length` digits.

    :param length: length of the token to generate
    :return: a valid numeric token of length `length`
    '''

    if length <= 0:
        return '0'
    else:
        return random.choice(string.digits) + ''.join(random.choice(string.digits) for i in range(length))


class ExpressionTest(unittest.TestCase):
    def test_ExpressionEval(self):
        e = Expression()
        self.assertRaises(NotImplementedError, Expression.eval, e)

    def test_Value(self):
        for i in range(1000):
            token = generate_num_token(random.randrange(10))
            v = Value(token)
            while len(token) > 1 and token[0] == '0':
                token = token[1:]

            self.assertEqual(token, v.__str__(), f'Value.__str__() ne renvoie pas la bonne valeur {token}')
            self.assertEqual(int(token), v.eval(), 'Value.eval() ne renvoie pas la bonne valeur')

    def test_Variable(self):
        for i in range(1000):
            token = generate_alphanum_token(random.randrange(10))
            v = Variable(token)
            self.assertEqual(token, v.__str__(), f'Variable.__str__() ne renvoie pas la bonne valeur {token}')
            self.assertIsNone(v.eval(), 'Variable.eval() ne renvoie pas la bonne valeur par dÃ©faut')
            value = random.randrange(1000)
            v.set_value(value)
            self.assertEqual(value, v.eval(), 'Variable.eval() ne renvoie pas la bonne valeur')
            self.assertEqual(token, v.__str__(), f'Variable.__str__() est modifiÃ© aprÃ¨s Variable.set_value()')



if __name__ == '__main__':
    unittest.main()
import random
import string
import unittest

from Class.Expression import Expression, Value, Variable, PrefixExpression
from Class.Parser import Parser

alpha = string.ascii_letters + '_'
alphanum = alpha + string.digits


def generate_alphanum_token(length: int) -> str:
    """
    Generates a valid alphanumeric token of given length.
    The token consists of `length` alphanumeric characters (including `_`) but does not start with a digit.

    :param length: length of the token to generate
    :return: a valid alphanumeric token of length `length`
    """

    if length <= 0:
        return ''
    else:
        return random.choice(alpha) + ''.join(random.choice(alphanum) for i in range(length))


def generate_num_token(length: int) -> str:
    """
    Generates a valid numeric token of given length.
    The token consists of `length` digits.

    :param length: length of the token to generate
    :return: a valid numeric token of length `length`
    """

    if length <= 0:
        return '0'
    else:
        return random.choice(string.digits) + ''.join(random.choice(string.digits) for i in range(length))


def generate_random_Value():
    token = generate_num_token(random.randrange(10))
    return Value(token)


def generate_random_Variable():
    token = generate_alphanum_token(random.randrange(10))
    v = Variable(token)
    value = random.randrange(1000)
    v.set_value(value)
    return v


class PrefixExpressionTest(unittest.TestCase):
    '''
    def test_PrefixExpressionConstruct(self):

        global exception
        v = generate_random_Value()

        for i in ['-', '+']:
            pe = PrefixExpression(i, v)

        p = Parser()
        for i in p.alph:
            if i not in ['-', '+']:
                try:
                    exception = True
                    pe = PrefixExpression(i, v)
                    exception = False
                except RuntimeError:
                    pass
                finally:
                    self.assertTrue(exception,
                                    "Il ne devrait pas Ãªtre possible de crÃ©er des PrefixExpression avec n'importe quel opÃ©rateur")
        '''
    def test_PrefixExpressionEval(self):
        for i in range(1000):
            v = generate_random_Value()
            pe = PrefixExpression('-', v)
            self.assertEqual(-v.eval(), pe.eval())

            v = generate_random_Variable()
            pe = PrefixExpression('-', v)
            self.assertEqual(-v.eval(), pe.eval())

        v = Variable(generate_alphanum_token(10))
        pe = PrefixExpression('-', v)
        self.assertRaises(TypeError, pe.eval)

    def test_PrefixExpressionStr(self):
        for i in range(1000):
            v = generate_random_Value()
            pe = PrefixExpression('-', v)
            self.assertEqual('- ' + v.__str__(), pe.__str__())

            v = generate_random_Variable()
            pe = PrefixExpression('-', v)
            self.assertEqual('- ' + v.__str__(), pe.__str__())

        v = Variable(generate_alphanum_token(10))
        pe = PrefixExpression('-', v)
        self.assertEqual('- ' + v.__str__(), pe.__str__())


if __name__ == '__main__':
    unittest.main()

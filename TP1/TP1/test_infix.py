import random
import string
import unittest

from Class.Expression import Expression, Value, Variable, PrefixExpression, InfixExpression
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


def generate_random_Value():
    token = generate_num_token(random.randrange(10))
    return Value(token)


def generate_random_Variable():
    token = generate_alphanum_token(random.randrange(10))
    v = Variable(token)
    value = random.randrange(1000)
    v.set_value(value)
    return v

def generate_random_Expression():
    expression_types = [Value, Variable, PrefixExpression]
    random_expression = None

    random_type = random.choice(expression_types)
    if random_type == Value:
        random_expression = generate_random_Value()
    elif random_type == Variable:
        random_expression = generate_random_Variable()
    elif random_type == PrefixExpression:
        random_expression = generate_random_Expression()
        random_expression = PrefixExpression('-', random_expression)
    else:
        raise RuntimeError("Cette erreur est impossible")

    return random_expression

class InfixExpressionTest(unittest.TestCase):


    def test_InfixExpressionConstruct(self):

        for i in range(1000):
            e1 = generate_random_Expression()
            e2 = generate_random_Expression()
            op = random.choice(['+', '-', '*', '/'])
            ie = InfixExpression(op, e1, e2)


    def test_InfixExpressionEval(self):
        for i in range(1000):
            e1 = generate_random_Expression()
            e2 = generate_random_Expression()
            op = random.choice(['+', '-', '*', '/'])

            ie = InfixExpression(op, e1, e2)

            if op == '+':
                self.assertEqual(e1.eval() + e2.eval(), ie.eval())
            elif op == '-':
                self.assertEqual(e1.eval() - e2.eval(), ie.eval())
            elif op == '*':
                self.assertEqual(e1.eval() * e2.eval(), ie.eval())
            elif op == '/':
                if e2.eval() != 0:
                    self.assertEqual(e1.eval() // e2.eval(), ie.eval())
                else:
                    self.assertRaises(ZeroDivisionError, ie.eval)

        e1 = generate_random_Value()
        e2 = Value('0')
        ie = InfixExpression('/', e1, e2)

        self.assertRaises(ZeroDivisionError, ie.eval)

        e2 = Variable(generate_alphanum_token(10))
        for i in ['+', '-', '/', '*']:
            ie = InfixExpression(i, e1, e2)
            self.assertRaises(TypeError, ie.eval)

    def test_InfixExpressionStr(self):
        for i in range(1000):
            for i in range(1000):
                e1 = generate_random_Expression()
                e2 = generate_random_Expression()
                op = random.choice(['+', '-', '*', '/'])

                ie = InfixExpression(op, e1, e2)
                self.assertEqual(f'{e1.__str__()} {op} {e2.__str__()}',ie.__str__())


if __name__ == '__main__':
    unittest.main()
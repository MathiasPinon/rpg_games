import unittest

from Class.Expression import Expression, Value, PrefixExpression, InfixExpression, Variable
from Class.Parser import Parser
from main import read_expression


class ReadExpressionTest(unittest.TestCase):

    def read_expression_example(flot: str) -> (Expression, str):
        """
        :param flot:
        :return:
        """
        p = Parser()

        (token, flot) = p.get_token(flot)
        previousExpression = None
        currentExpression = None

        while token:
            if token.isnumeric():
                currentExpression = Value(int(token))
            elif p.is_operator(token[0]):
                operator = token
                (nextExpression, flot) = ReadExpressionTest.read_expression_example(flot)

                if not previousExpression:
                    currentExpression = PrefixExpression(operator, nextExpression)
                else:
                    currentExpression = InfixExpression(operator, previousExpression, nextExpression)

            elif token[0].isalpha():
                currentExpression = Variable(token)

            previousExpression = currentExpression
            (token, flot) = p.get_token(flot)

        return currentExpression, flot

    def test_ReadExpression_1(self):
        expression_list = [ "2 + 3", "2 + 3 - 5", "2 + 3 * 4", "3 * 4 + 2", "(3 * 4) + 2", "3 + a"]
        for e in expression_list:
            ref_read_result = ReadExpressionTest.read_expression_example(e)
            (ref_expression, ref_rest) = (ref_read_result[0], ref_read_result[-1])

            test_read_result = ReadExpressionTest.read_expression_example(e)
            (test_expression, test_rest) = (test_read_result[0], test_read_result[-1])

            self.assertEqual(ref_expression.__str__(), test_expression.__str__())  # add assertion here
            self.assertEqual(ref_rest, test_rest)


if __name__ == '__main__':
    unittest.main()
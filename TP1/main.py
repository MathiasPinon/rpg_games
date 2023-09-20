import Class.Expression
from Class.Parser import Parser
from Class.Expression import *
'''
p = Parser()

flux1 = 'a + b'
flux2 = ' a + b'
flux3 = 'a+b'
flux4 = 'abcd'
flux5 = '410fer'
flux6 = 'ab12'
flux7 = '@ab'

print(p.get_token(flux1))  # doit afficher ('a', ' + b')
print(p.get_token(flux2))  # doit afficher ('a', ' + b')
print(p.get_token(flux3))  # doit afficher ('a', '+b')
print(p.get_token(flux4))  # doit afficher ('abcd', '')
print(p.get_token(flux5))  # doit afficher ('12', 'ab')
print(p.get_token(flux6))  # doit afficher ('ab12', '')
print(p.get_token(flux7))  # doit afficher ('', '@ab')

#flux8 = "410fer + 47 + ces78 + / + @uti + 14fer "
#print(p.get_token_long(flux8))
'''

def read_expression(flot: str) -> (Expression, str):
    """
    :param flot:
    :return:
    """
    #Création d'une classe
    p = Parser()

    #définition du token
    (token, flot) = p.get_token(flot)
    previousExpression = None
    currentExpression = None

    #Tant que il y a un token
    while token:
        # Si token est un nombre ou str
        if token.isnumeric():
            currentExpression = Value(int(token))
        # Sinon on regarde si le premier caractère est un opérateur

        elif p.is_operator(token[0]):
            operator = token
            (nextExpression, flot) = read_expression(flot)
            # s'il n'a pas d'Expression précendent on fait l'oppération
            if not previousExpression:
                currentExpression = PrefixExpression(operator, nextExpression)

            # s'il a d'Expression précendent on fait l'oppération on écrit la chaine de caractère
            else:
                currentExpression = InfixExpression(operator, previousExpression, nextExpression)

        # si la première lettre du token est dans l'alphabet
        elif token[0].isalpha():
            currentExpression = Variable(token)

        previousExpression = currentExpression
        (token, flot) = p.get_token(flot)

    return currentExpression, flot
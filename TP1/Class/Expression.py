class Expression:
    def eval(self) -> int:
        '''
        Evalue l'expression et calcule sa valeur
        :return: la valeur de l'expression
        '''
        raise NotImplementedError


class Value(Expression):
    value: int

    def __init__(self, token: str):
        self.value = int(token)

    def __str__(self):
        return str(self.value)

    def eval(self) -> int:
        return self.value


class Variable(Expression):
    name: str
    value: int

    def __init__(self, variable: str):
        self.name = variable
        self.value = None

    def __str__(self) -> str:
        return self.name

    def eval(self) -> int:
        return self.value

    def set_value(self, value: int):
        self.value = value

class PrefixExpression(Expression):
    op: str
    expr: Expression

    def __init__(self, op: str, expr: Expression):
        self.op = op
        self.expr = expr

    def __str__(self) -> str:
        chaine_car = self.op + ' ' + self.expr.__str__()
        return chaine_car

    def eval(self):
        expr = self.expr.eval()
        nbr_moins = self.op.count("-")
        for i in range(nbr_moins):
            expr *= -1
        return expr

class InfixExpression(Expression):
    op: str
    expr1: Expression
    expr2: Expression

    def __init__(self, op: str, expr1: Expression, expr2: Expression):
        self.op = op
        self.expr1 = expr1
        self.expr2 = expr2

    def __str__(self) -> str:
        chaine_car = self.expr1.__str__() + ' ' + self.op + ' ' + self.expr2.__str__()
        return chaine_car

    def eval(self):
        expr1 = self.expr1.eval()
        expr2 = self.expr2.eval()
        nbr_moins = self.op.count("-")
        if self.op == "-":
            return expr1 - expr2
        if self.op == "+" :
            return expr1 + expr2
        if self.op == "*" :
            return expr1 * expr2
        if self.op == "/" :
            return expr1 // expr2

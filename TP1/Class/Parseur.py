class Parseur :
    alph : list

    def __init__(self,liste:list):
        if liste is None :
            self.alph = [ '+', '-', '*', '/', '_', '(', ')', ' ']
        else :
            self.alph = liste

    
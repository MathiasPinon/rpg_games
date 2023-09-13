class Parseur :
    alph : list

    def __init__(self,liste:list):
        if type(liste) != list :
            self.alph = [ '+', '-', '*', '/', '_', '(', ')', ' ']
        else :
            self.alph = liste

    def is_in_alphabet(self, c:str)->bool:
        if c in self.alph :
            return True
        else :
            return False


class Parser:
    alph: list

    def __init__(self, liste: list = ['+', '-', '*', '/', '_', '(', ')', ' ']):
        if type(liste) != list:
            self.alph = ['+', '-', '*', '/', '_', '(', ')', ' ']
        else:
            self.alph = liste

    def is_in_alphabet(self, c: str) -> bool:
        if c in self.alph:
            return True
        else:
            return False

    def get_token(self, flux: str) -> tuple:
        chaine1 = ''
        chaine2 = ''
        number = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
        i = 0
        while flux[i] == ' ':
            i += 1

        if flux[i] in self.alph:
            chaine1 = flux

        elif flux[i].isalnum():
            if flux[i] in number:
                while i < len(flux) and flux[i] in number:
                    chaine1 += flux[i]
                    i += 1
                for t in range(i, len(flux)):
                    chaine2 += flux[t]
            else:
                while i < len(flux) and flux[i].isalnum() :
                    chaine1 += flux[i]
                    i += 1
                for t in range(i, len(flux)):
                    chaine2 += flux[t]
        else:
            chaine2 = flux

        return (chaine1, chaine2)

    def get_token_long(self, flux: str) -> list:
        liste = []
        fluxListe = []
        t = 0
        mot = ''
        for i in range(len(flux)):
            if flux[i] != ' ':
                mot += flux[i]
            else:
                liste.append(mot)
                mot = ''
        for t in range(len(liste)):
             fluxListe.append(self.get_token(liste[t])[0] )
        return fluxListe

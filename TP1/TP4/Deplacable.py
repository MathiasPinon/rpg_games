from TP4.Actionnable import Actionnable
from TP4.Localisable import Localisable


class Deplacable(Localisable, Actionnable):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.destination = (self.x,self.y)
        self._actions['deplacer'] = self.move

    def getDestination(self) -> tuple :
        return self.destination

    def setDestination(self, destination: tuple):
        self.destination = destination

    def move(self):
        x = self.lieu[0]
        y = self.lieu[1]
        if self.destination[0] > self.lieu[0] :
            x += 1
        elif self.destination[0] < self.lieu[0] :
            x -= 1
        if self.destination[1] > self.lieu[1]:
            y += 1
        elif self.destination[1] < self.lieu[1]:
            y -= 1
        self.lieu = (x,y)

if __name__ == '__main__':

    d = Deplacable()
    d.destination = (6, 12)

    while d.destination != d.lieu:
        d.move()
        print(d.lieu)

    d.destination = (0,0)
    while d.destination != d.lieu:
        d.actions['deplacer']()
        print('je me déplace')
        print(d.lieu)
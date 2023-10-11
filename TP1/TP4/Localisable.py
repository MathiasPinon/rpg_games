class Localisable(object):
    def __init__(self, x=0, y=0, **kwargs):
        super().__init__(**kwargs)
        self.__pos_x = x
        self.__pos_y = y

    @property
    def x(self):
        return self.__pos_x

    @property
    def y(self):
        return self.__pos_y

    @property
    def lieu(self):
        return self.__pos_x, self.__pos_y

    @lieu.setter
    def lieu(self, loc: tuple):
        self.__pos_x, self.__pos_y = loc
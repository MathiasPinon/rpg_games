class Actionnable(object):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._actions = {}

    @property
    def actions(self):
        return self._actions

if __name__ == '__main__':
    a = Actionnable()

    def f():
        print('Action effectuée')

    a.actions['demo'] = f

    print(a.actions)
    a.actions['demo']()
from Example import Example


class Dxample(Example):

    def __init__(self, value: int, name: str):
        super().__init__(value)
        self.__name = name

    def __del__(self):
        pass

    @property
    def name(self):
        return self.__name
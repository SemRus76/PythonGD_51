from Figure import Figure

class Square(Figure):

    def __init__(self, X: int, Y: int, width: int, height: int):
        super().__init__(X, Y, width, height)

    def __del__(self):
        pass

    def square(self):
        return self.height * self.width





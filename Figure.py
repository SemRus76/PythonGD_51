
class Figure:

    __coord_X = 0
    __coord_Y = 0
    __width_F = 0
    __height_F = 0

    def __init__(self, X: int, Y: int, width: int, height: int):
        self.__coord_X = X
        self.__coord_Y = Y
        self.__width_F = width
        self.__height_F = height

    def __del__(self):
        pass

    @property
    def x(self):
        return self.__coord_X

    @x.setter
    def x(self, value: int):
        if 100 > value and value > -100:
            self.__coord_X = value

    @property
    def y(self):
        return self.__coord_Y

    @y.setter
    def y(self, value):
        if 100 > value and value > -100:
            self.__coord_Y = value

    @property
    def width(self):
        return self.__width_F

    @width.setter
    def width(self, value):
        if value >= 0:
            self.__width_F = value
        else:
            self.__width_F = abs(value)

    @property
    def height(self):
        return self.__height_F

    @height.setter
    def height(self, value):
        if value >= 0:
            self.__height_F = value
        else:
            self.__height_F = abs(value)

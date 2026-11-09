
class Example:

    def __init__(self, value):
        self.__number = value if value != 0 else 0

    def __del__(self):
        pass

    def output(self):
        return str(self.__number)

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, value):
        if not (value < 0):
            self.__number = value


# Наследование
#
# Третий принцип ООП - Наследование - позволяет создавать классы на
#   базе уже имеющихся
from temp import Temp

class Template(Temp):

    __name = str()

    def __init__(self, name: str):
        super().__init__(10, 2)
        self.__name = name

    def __del__(self):
        pass

    def __str__(self):
        return self.__name + f" {super().__str__()}"








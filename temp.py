
# Класс
#
# Описание любого класса начинается с ключевого слова
#   class <имя класса>:
#       pass
#
#   __init__(self): - описывает то, как нужно создавать объект класса
#   __del__(self): - описывает то, как нужно уничтожать объект класса
#
#   __add__(self, other): - описание оператора сложения для объектов класса
#   __sub__(self, other): - описание оператора вычитания для объектов класса
#   __mul__(self, other): - описание оператора умножения
#   __matmul__(self, other): - описаие оператора мат. множения
#   __truediv__(self, other): - описание целочисленное деление
#   __floordiv__(self, other): - описание деление с остатком
#   __mod__(self, other): - остаток от деления
#   __divmod__(self, other): - остаток от целого деления
#   __pow__(self, other[, modulo]): - возведение в степень
#   __and__(self, other): - Логическое И
#   __or__(self, other): - Логическое ИЛИ
#
#   __lt__(self, other): - less then - строгое меньше <
#   __le__(self, other): - less equal - меньше или равно <=
#   __gt__(self, other): - great then - строгое больше >
#   __ge__(self, other): - great equal - больше или равно >=
#   __eq__(self, other): - equal - равно ==
#   __ne__(self, other): - not equal - не равно !=
#
#   __str__(self): - приведение объекта класса к строке
#
class Temp:
    __value_1 = -1  # Поле класса
    __value_2 = -1  # Поле класса
    __value_3 = -1

    def __init__(self, value_1: int = 0, value_2: int = 0):
        self.__value_1 = value_1
        self.__value_2 = value_2
        self.__value_3 = 0

    def __del__(self):
        pass

    def __add__(self, other):
        if (isinstance(other, Temp)):
            self.__value_1 += other.__value_1
            self.__value_2 += other.__value_2
            self.__value_3 += other.__value_3

    def __str__(self):
        return f"val_1 = {self.__value_1} - val_2 = {self.__value_2} = {self.__get_value()}"

    def get_str(self) -> str:  # Метод класса
        return f"val_1 = {self.__value_1} - val_2 = {self.__value_2} = {self.__get_value()}"

    def __get_value(self):
        self.__value_3 = self.__value_1 - self.__value_2
        return self.__value_3

    def get_value_1(self) -> int:
        return self.__value_1

    def set_value_1(self, value: int) -> None:
        if value < 0:
            return
        self.__value_1 = value
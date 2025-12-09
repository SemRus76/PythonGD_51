
# Класс
#
# Описание любого класса начинается с ключевого слова class <имя класса>:
#
#
#
#
#


class Temp:

    __value_1 = -1  # Поле класса
    __value_2 = -1  # Поле класса

    def get_str(self) -> str:  # Метод класса
        return f"val_1 = {self.__value_1} - val_2 = {self.__value_2} = {self.__get_value()}"

    def __get_value(self):
        return self.__value_1 - self.__value_2

    def get_value_1(self) -> int:
        return self.__value_1

    def set_value_1(self, value: int) -> None:
        if value < 0:
            return
        self.__value_1 = value

    def __
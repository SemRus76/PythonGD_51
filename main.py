from temp import Temp
from file import Template

obj_1 = Temp(0, 2)

obj_2 = Temp(0, 4)

obj_1.set_value_1(1500)
obj_2.set_value_1(1890)

print(f"Object 1 = {obj_1.get_str()}")
print(f"Object 2 = {obj_2.get_str()}")

obj_1 + obj_2

print(obj_1)

print("-========================-")

template_obj_1 = Template("NAMA")
print(template_obj_1)
template_obj_1.set_value_1(100)

template_obj_1 + obj_1
print(template_obj_1)

# Задание
#
# Создать базовый класс Figure, который хранит в себе
#   точку центра фигуры и ширину и высоту фигуры
# От этого класса необходимо создать 3 наследника
#       - Square, Triangle, Circle
#  В наследниках необходимо реализовать функцию Площади (Square)
#
#   Во всех классах должен присутствовать конструктор и метод str
#




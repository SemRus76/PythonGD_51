from functools import reduce

from Example import Example
from Dxample import Dxample

obj = Example(5)

print(obj.output())
obj.number = 10
print(obj.number)

dbj = Dxample(7,"Hello")
print(dbj.number)
print(dbj.name)

def endpoint():
    try:
        raise Exception("Error")
    except Exception as err:
        print("502 ошибка - ", err)

endpoint()

lst = [0, 1, -1, 2, -2, 3, -3]

for element in filter(lambda value: True if value >= 0 else False, lst):
    print(element, end=' ')
print()

for element in map(lambda value: -value, lst):
    print(element, end=' ')
print()

summer = reduce(lambda x, y: x+y, [1,2,3,4,5,6,7,8,9])
print(summer)

print(lst)




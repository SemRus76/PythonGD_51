
# Полиморфизм
#
#   Полиморфизм - это способность объектов менять свой тип и
#       представляться другими объектами
#
#   Полиморфизм неразрывно связан с наследованием, потому как
#       Сама спосбность представляться другим объектом заложена в
#       механизм наследования


from First import First
from Lastli import Lastli

def functionA(obj : First):
    print(obj)
    print(type(obj))

def functionB(obj : First):
    print(obj.nummer)
    print(type(obj))

fObj = First(10)
functionA(fObj)
functionB(fObj)
print("-===================-")
lObj = Lastli(99, "Иван")
functionA(lObj)
functionB(lObj)
print("-===================-")

from threading import Thread
import time

def print_chrismass(sign : str):
    for i in range(1, 99, 2):
        print(sign * i)
        time.sleep(0.5)

Thr1 = Thread(target=print_chrismass, args=("*"))
Thr2 = Thread(target=print_chrismass, args=("#"))

Thr1.start()
Thr2.start()

Thr1.join()
Thr2.join()






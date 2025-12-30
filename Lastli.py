from First import First

class Lastli(First):
    __name = str()

    def __init__(self, num : int, name : str):
        super().__init__(num)
        self.__name = name

    def __str__(self):
        return f"{self.__name} имеет {self.nummer} рублей"

    @property
    def name(self):
        return self.__name

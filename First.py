class First:

    __nummer = 0

    def __init__(self, num : int = 0):
        self.__nummer = num

    def __str__(self):
        return f"Nummer = {self.__nummer}"

    @property
    def nummer(self):
        return self.__nummer

class Calculator:
    def __init__(self, num1, num2):
        self.__result = 0
        self.num1 = num1
        self.num2 = num2

    def add(self):
        self.__result = self.num1 + self.num2

    def sub(self):
        self.__result = self.num1 - self.num2

    def mul(self):
        self.__result = self.num1 * self.num2

    def div(self):
        self.__result = self.num1 / self.num2

    def get_result(self):
        return self.__result

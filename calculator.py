class Calculator:
    def __init__(self):
        self.calculation = 0
        self.operation = "+"
    
    def plus(self, num):
        self.operation = "+"
        self.calculation += num

    def minus(self, num):
        self.operation = "-"
        self.calculation -= num

    def multiply(self, num1, num2):
        self.operation = "*"
        self.calculation *= num

    def divide(self, num):
        self.operation = "/"
        self.calculation /= num
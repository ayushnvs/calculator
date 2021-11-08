class Calculator:
    def __init__(self):
        self.calculation = 0
        self.operation = None
    
    def plus(self, num):
        self.calculation += num

    def minus(self, num):
        self.calculation -= num

    def multiply(self, num):
        self.calculation *= num

    def divide(self, num):
        self.calculation /= num
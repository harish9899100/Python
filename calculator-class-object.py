class claculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def add(self):
        return self.a + self.b
    def diff(self):
        return self.a - self.b
    def mult(self):
        return self.a * self.b
    def div(self):
        if self.b == 0:
            return("Zero division error")
        return self.a / self.b
a = int(input("Enter first number :"))
b = int(input("Enter second number :"))

calc = claculator(a, b)
print("Add :", calc.add())
print("Diffrence :", calc.diff())
print("Multyply :", calc.mult())
print("Divide :", calc.div())
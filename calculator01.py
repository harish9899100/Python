
def add(a, b):
    return a + b
def diff(a, b):
    return a - b
def mult(a, b):
    return(a * b)
def div(a, b):
    return a / b
print("Task :\n\n1.Add\n2.Diffrance\n3.Multyply\n4.Divide\n")
task = int(input("Select a task : "))

a = int(input("Enter your first number :"))
b = int(input("Enter your second number :"))

if task == 1:
    print(f"{a} + {b} = ", add(a, b))
    #print(a, "+", b,"=", add(a, b))
elif task == 2:
    print(f"{a} - {b} = ", diff(a, b))
elif task == 3:
    print(f"{a} * {b} = ", mult(a, b))
elif task == 4:
    print(f"{a} / {b} =", div(a, b))
else:
    print("Enter valid input ")
    
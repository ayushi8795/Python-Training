print("Calculations on 2 numbers")
def Calculate(func):
    def inner(a,b):
        return func(a,b)
    return inner

@Calculate
def add(a,b):
    return a+b

@Calculate
def sub(a,b):
    if a>=b:
        return a-b
    else:
        return b-a

@Calculate
def mul(a,b):
    return a*b

@Calculate
def div(a,b):
    if b ==0:
        print("Cannot divide b is 0")
    else:
        return a/b

value1 = add(4,3)
print("additon: ",value1)
value2 = sub(4,3)
print("subtraction: ",value2)
value3 = mul(4,3)
print("Multiplication: ",value3)
value4 = div(4,3)
print("Division: ",value4)
value5 = sub(3,4)
print("Subtraction a<b: ",value5)
value6 = div(3,0)

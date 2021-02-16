print("1.Addition")
print("2.Subtraction")
print("3.Division")
print("4.Multiplication")
print("5.Average")
a = int(input("Enter the numerical value of operation: "))
num1 = int(input("Enter value of num1: "))
num2 = int(input("Enter value of num2: "))
if a == 1:
    b=num1+num2
elif a == 2:
    b = num1-num2
elif a == 3:
    b = num1/num2
elif a == 4:
    b = num1*num2
elif a == 5:
    num3 = int(input("Enter value of num3: "))
    num4 = int(input("Enter value of num4: "))
    b = ((num1+num2+num3+num4)/4)
else:
    print("ABC")
if b>=0:
    print("Result: ",b)
else:
    print("Negative")

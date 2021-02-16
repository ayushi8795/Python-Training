l1 =[]
add = 0
mul =1
n = int(input("Enter the number of element in list: "))
for i in range(0,n):
    a = int(input())
    l1.append(a)
for i in range(len(l1)):
    add = add+l1[i]
print("Addition: ",add)
for i in range(len(l1)):
    mul = mul*l1[i]
print("Multiplication: ",mul)

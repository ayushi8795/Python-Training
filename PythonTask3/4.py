l1 =[]
n = int(input("Enter the number of element in list: "))
for i in range(0,n):
    a = int(input())
    l1.append(a)
print("smallest: ",min(l1))
print("Largest: ",max(l1))

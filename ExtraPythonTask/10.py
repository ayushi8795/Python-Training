tup = (1,2,3,4,5,6,7,8,9,12,1,3,14,15,16)
lst2=[]
lst = list(tup)
for i in lst:
    if i%2 == 0:
        lst2.append(i)
tup2 = tuple(lst2)
print("Original tuple: ",tup)
print("modified tuple: ",tup2)
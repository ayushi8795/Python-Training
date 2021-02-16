str1 = input("Enter string: ")
l ={}
for i in str1:
    if i.isalpha()==True:
        if i in l:
            l[i] = l[i]+1
        else:
            l[i] = 1
    else:
        pass
print(l)
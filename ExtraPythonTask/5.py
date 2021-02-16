str1 = input("enter the string: ")
str2 = str1[::-1]
print("Reverse of given string is: ",str2)
l = ['a','e','i','o','u','A','E','I','O','U']
for i in str2:
    if i in l:
        print(i,str2.index(i))

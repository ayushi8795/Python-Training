str1 = "hello my name is abcde"
str2 = str1.split(" ")
for i in range(0,len(str2)):
    if len(str2[i])%2 == 0:
        print(str2[i])

def fun():
    str1 = input("Enter string 1: ")
    str2 = input("Enter string 2: ")
    s1 = len(str1)
    s2 = len(str2)
    if s1>s2:
        print(str1)
    elif s2>s1:
        print(str2)
    elif s1==s2:
        print(str1)
        print(str2)
fun()

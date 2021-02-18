def function():
    l = []
    l2 =[]
    l =input("Enter space separated input: ").split()
    for a in l:
        l1=[]
        for p in a:
            x = p.capitalize()
            l1.append(x)
            y = "".join(l1)
        l2.append(y)
    return (" ".join(l2))
print(function())
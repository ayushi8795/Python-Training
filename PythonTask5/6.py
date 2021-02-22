file = open("doct.txt",'r')
for x in file.readlines():
    x = x.strip()
    if len(x)%2 == 0:
        print(x)
        continue
    else:
        pass
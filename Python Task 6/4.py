def genfun():
    str = "consultadd training"
    length = len(str)
    for i in range(length-1,-1,-1):
        yield str[i]

for char in genfun():
    print(char)

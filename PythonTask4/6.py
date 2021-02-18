def fun(x, y):
    x = int(x)
    y = int(y)
    return lambda x,y: x+y

print(fun(x=3,y=4) )
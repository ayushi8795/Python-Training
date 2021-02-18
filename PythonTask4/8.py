def fun(n):
    return n*n
number = range(1,21)
result = map(fun,number)
print(tuple(result))
    
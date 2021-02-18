l = range(1,2000)
x=[]
result = filter(lambda x : x if (x%7 == 0  and x%3 != 0) else False,l)
print(list(result))

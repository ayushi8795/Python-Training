from functools import reduce
lis = [1,2,3,4,5,6,7]
result = reduce(lambda total, d: 10 * total + d, lis)
print(result)
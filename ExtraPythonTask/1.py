x=[100,200,300,400,500,[1,2,3,4,5,[10,20,30,40,50],6,7,8,9],600,700,800]
l=[]
for i in range(0,4):
    l.append(x[5][i])
print(l)
print(x[-3:-1])
print(x[::2])
print(x[::-1])
print([x[5][5][0]])
print([])
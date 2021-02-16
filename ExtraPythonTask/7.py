x=[1,2,3,4,5,6,7,8,9,-1]
target = 8 
for i in x:
    if target-i in x and i<target-i:
        print(i,target-i)
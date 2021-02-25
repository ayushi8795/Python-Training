class zero:
    def __init__(self,lst):
        self.lst =lst
    def ze(self):
        lst2 = []
        n = len(self.lst)
        for i in range(0,n-2):
            for j in range(i+1,n-1):
                for k in range(j+1,n):
                    if self.lst[i]+self.lst[j]+self.lst[k] == 0:
                        lst1 = []
                        lst1.append(self.lst[i])
                        lst1.append(self.lst[j])
                        lst1.append(self.lst[k])
                        lst2.append(lst1)
        print(lst2)

s = zero([-25,-10,-7,-3,2,4,8,10])
s.ze()

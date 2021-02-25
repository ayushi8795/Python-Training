class Time:
    def __init__(self,hrs,min):
        self.hrs = hrs
        self.min = min
    def addTime(t1,t2):
        t3 = Time(0,0)
        t3.hrs = t1.hrs +t2.hrs
        t3.min = t1.min +t2.min
        while t3.min >= 60:
            t3.hrs = t3.hrs+1
            t3.min = t3.min-60
        return t3

    def displayTime(self):
        print("The total time is:{0} hrs and {1} minute".format(self.hrs,self.min))
    def displayMinute(self):
        print((self.hrs*60)+self.min,"minutes")

a = Time(2,90)
b = Time(3,80)
c = Time.addTime(a,b)
c.displayTime()
c.displayMinute()

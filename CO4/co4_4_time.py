class Time:
    def __init__(self,h,m,s):
        self.h = h
        self.m = m
        self.s = s

       
    def __add__(self,other):
        self.second = self.s+other.s
        self.minute = self.m+other.m+ int(self.second/60)
        self.hour = self.h+other.h+int(self.minute/60)
        self.minute = self.minute%60
        self.second = self.second%60
        return "%d:%02d:%02d" % (self.hour,self.minute,self.second)
s1 = Time(int(input("Enter hr1")),int(input("Enter min1")),int(input("Enter sec1")))
s2 = Time(int(input("Enter hr2")),int(input("Enter min2")),int(input("Enter sec2")))
print(s1+s2)

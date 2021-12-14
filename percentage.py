class Students:
    def __init__(self,name,roll,m1,m2,m3):
        self.name=name
        self.roll=roll
        self.m1=m1
        self.m2=m2
        self.m3=m3
        
print("Enter the Number of Students:")
N=int(input())
list=[]

for i in range(0,N):
    a=input("Enter the name:")
    b=int(input("Enter the roll:"))
    c=int(input("Enter m1:"))
    d=int(input("Enter m2:"))
    e=int(input("Enter m3:"))
    list.append(Students(a,b,c,d,e))
for obj in list:
    print(obj.name,(obj.m1 + obj.m2 + obj.m3)/3,"%")

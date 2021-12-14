class Students:
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll

print("Enter N:")
N=int(input())
list =[]
a=[]
b=[]
for i in range(0,N):
    n=input("Enter the name:")
    q=input("Enter roll no:")
    a.append(n)
    b.append(q)
    list.append(Students(a[i],b[i]))
    
for obj in list:
    print(obj.name,obj.roll,sep=" ")

class Students:
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll

print("Enter N:")
N=int(input())
list =[]
for i in range(0,N):
    n=input("Enter the name:")
    q=input("Enter roll no:")
    list.append(Students(n,q))
    
for obj in list:
    print(obj.name,obj.roll,sep=" ")

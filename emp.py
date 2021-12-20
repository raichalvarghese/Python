class Employee:
    def __init__(self,name,idd,salary,depart):
        self.name=name
        self.idd=idd
        self.salary=salary
        self.depart=depart
        
print("Enter the Number of Employee:")
N=int(input())
list=[]
for i in range(0,N):
    a=input("Enter the name:")
    b=int(input("Enter the id:"))
    c=int(input("Enter salary:"))
    d=input("Enter depart:")
    list.append(Employee(a,b,c,d))

for obj in list:
    if obj.salary==15000:
        print("Details of employee with salary 15k:")
        print(obj.name,obj.idd,obj.salary,obj.depart,sep=" ")
       

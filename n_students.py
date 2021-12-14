class Student:
    "information"
    studentcount=0
    def __init__(self,roll,name,course):
        self.roll=roll
        self.name=name
        self.course=course
        Student.studentcount=Student.studentcount+1
    def displaycount():
        print("No. of students",Student.studentcount)
    def display(self):
        print("Roll No",self.roll)
        print("name",self.name)
        print("course",self.course)
    

print("Enter N:")
N=int(input())
l=[]
m=[]
o=[]
for i in range(0,N):
    y=int(input("Enter the year:"))
    n=input("Enter the name:")
    q=input("Enter the qualification:")
    l.append(y)
    m.append(n)
    o.append(q)


for i in range(0,N):
    s=Student(l[i],m[i],o[i])
    s.display()
    

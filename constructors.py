#constuctors

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
    def __del__(self):
        class_name=self.__class__.__name__
        print(class_name,"destroyed")

s1=Student(2008,"Reshma","MCA")
s2=Student(2012,"Riya","MTech")
print(getattr(s1,'name'))
s1.display()
s2.display()
Student.displaycount()
del s1


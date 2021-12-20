# Object Oriented Programming

class Student:
    "information"
    studentcount=0
    def getdata(self,roll,name,course):
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
s1=Student()
s2=Student()
s1.getdata(2008,"Reshma","MCA")
s2.getdata(2012,"Riya","MTech")
Student.display(s1)
Student.displaycount()

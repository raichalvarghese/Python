class Rectangle:
    def __init__(self):
        self.length=int(input("Enter the length"))
        self.breadth=int(input("Enter the breadth"))
    def area(self):
        a=self.length*self.breadth
        return a
    def perimeter(self):
        p=2*(self.length+self.breadth)
        return p
r1=Rectangle()
r2=Rectangle()
if Rectangle.area(r1)>Rectangle.area(r2):
    print("r1 is bigger")
else:
    print("r2 is bigger")

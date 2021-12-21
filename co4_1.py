class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        a=self.length*self.breadth
        return a
    def perimeter(self):
        p=2*(self.length+self.breadth)
        return p
r1=Rectangle(2,3)
r2=Rectangle(4,5)
if Rectangle.area(r1)>Rectangle.area(r2):
    print("r1 is bigger")
else:
    print("r2 is bigger")

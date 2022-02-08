class Rectangle:
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def area(self):
        self.area = self.l*self.b

    def __lt__(self,other):
        if self.area<other.area:
            return True
        else:
            return False

l1= int(input("Enter length of the rectangle1: "))
b1 = int(input("Enter breadth of the rectangle1: "))
l2 = int(input("Enter length of the rectangle2: "))
b2 = int(input("Enter breadth of the rectangle2: "))

r1 = Rectangle(l1,1)
r2 = Rectangle(l2,2)
r1.area()
r2.area()

if r1 < r2:
        print("Rectangle 2 is large")
else:
        print("Rectangle 1 is large")


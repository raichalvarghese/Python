class Book:
    def __init__(self,pages):
        self.pages = pages
    # Overloading +operator with magic method
    def __add__(self,other):
        return self.pages + other.pages
b1 = Book(400)
b2 = Book(300)
print("Total number of pages: ",b1+b2)

def cub():
    l=int(input("Enter the length of the cuboid:"))
    b=int(input("Enter the breadth of the cuboid:"))
    h=int(input("Enter the height of the cuboid:"))
    area=2*(l*b+b*h+h*l)
    perimeter=2*h*(l+b)
    print("Area is",area)
    print("Perimeter is",perimeter)

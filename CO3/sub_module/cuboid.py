def cub():
    l=int(input("Enter the length of the cuboid:"))
    b=int(input("Enter the breadth of the cuboid:"))
    h=int(input("Enter the height of the cuboid:"))
    s_area=2*(l*b+b*h+h*l)
    volume=l*b*h
    print("surface Area is",s_area)
    print("volume is",volume)

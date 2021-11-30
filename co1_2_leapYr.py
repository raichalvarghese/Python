y1=int(input("Enter the current year"))
y2=int(input("Enter the a future year"))
for i in range(y1,y2):
    if i%4==0:
        if i%100==0:
            if i%400==0:
                print(i)
        else:
            print(i)

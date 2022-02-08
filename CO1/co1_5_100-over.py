#Prompt the user for a list of integers.
#For all values greater than 100, store ‘over’ instead.

s=[int(x) for x in input().split()]
for x in s:
    if x>100:
        print(str(x).replace(str(x),'over'),end=" ")
    else:
        print(x,end=" ")

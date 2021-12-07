#Check whether a given number is Aliquot Number or not.

num = int(input("Enter a Number:"))
def aliquot(x):
    l=[]
    for i in range(1,x):
        if x%i==0:
            l.append(i)
        k=sum(l)
    if k==x:
        return True
    else:
        return False
    
if aliquot(num)==True:
    print("Aliquot")
else:
    print("Not aliquot")


def aliquot(x):
    l=[]
    for i in range(1,x):
        if x%i==0:
            l.append(i)
    k=sum(l)
    return k
    
# Check whether a pair of numbers is amicable or not

num1=int(input("Enter the first No:"))
num2=int(input("Enter the second No:"))
if aliquot(num1)==num2 and aliquot(num2)==num1:
    print("Amicable Numbers")
else:
    print("Not amicable numbers")

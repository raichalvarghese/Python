#Generate a list of four digit numbers in a given range with all their digits even and the
#number is a perfect square.

import math
num1=int(input("Enter the first limit"))
num2=int(input("Enter the final limit"))
def isPerfect(x):
    if x>0:
        p=math.sqrt(x)
        return ((p*p)==float(x))
    return false

s=[]
sm=0

for i in range(num1,num2):
        l=[]
        num=i
        while num>0:
            rem=num%10
            num=int(num/10)
            l.append(rem)
        if (l[0]%2==0) and (l[1]%2==0 and l[2]%2==0):
            s.append(i)
for x in s:
    if (isPerfect(x)==True):
        print(x)
    else:
        continue
        
        


    
        
        



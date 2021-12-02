# gcd of two numbers
a=int(input("Enter the 1st no:"))
b=int(input("Enter the 2nd no:"))
def gcd(a,b):
    if a==0:
        return a
    if b==0:
        return b
    if a==b:
        return a
    if a>b:
        return gcd(a-b,b)
    return gcd(b-a,a)
print("gcd(",a,",",b,") is",gcd(a,b))
            

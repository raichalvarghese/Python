#Factorial

prdt=1
n=int(input("Enter a number:"))
for i in range(1,n+1):
    if n!=0:
        prdt=prdt*i
    else:
        prdt=1
print("Factorial of ",n,"is",prdt)

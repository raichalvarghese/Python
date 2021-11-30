#Generate positive list of numbers from a given list of integers

l=[1,2,3,4,5,6,-8,9,-1]
for i in l:
    if i>0:
        print(i,end=" ")
print(" ")    
#Square of N numbers

for i in range(1,11):
    print(i**2,end=" ")
print(" ")
#Form a list of vowels selected from a given word

vowels="aeiou"
text="letter"
l=[]
for i in text:
    if i in vowels:
        l.append(i)
print(l)

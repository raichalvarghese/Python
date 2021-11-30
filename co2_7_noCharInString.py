#Add #‘ing’ at the end of a given string. If it already ends with ‘ing’, then add ‘ly
l=input()
lst=[]
for x in l:
    lst.append(x)

if lst[-3]=="i" and lst[-2]=="n" and lst[-1]=="g":
    lst.append("ly")
else:
    lst.append("ing")
lst[0:]=[''.join(lst[0:])]
print(lst[0])

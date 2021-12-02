#Accept a list of words and return length of longest word. 
txt= input().split()
k=[]
for x in txt:
    l=[]
    for y in x:
        l.append(y)
    k.append(len(l))
print(max(k))

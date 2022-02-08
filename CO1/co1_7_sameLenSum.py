lst1=[int(x) for x in input().split()]
lst2=[int(x) for x in input().split()]
if len(lst1)==len(lst2):
    print("Same length")
else:
    print("Not same length")
if sum(lst1)==sum(lst2):
    print("Same sum")
else:
    print("Not same sum")


for x in lst1:
    for y in lst2:
        if x==y:
            print(x,"occur in both")

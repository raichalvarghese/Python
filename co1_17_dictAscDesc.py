# Update
d={1:"Anu",2:"swathi",3:"abhijith"}
d1={4:"jack"}
d.update(d1)
print(d)


x={"January":31,"Eebruary":28}
sorted_x=sorted(x.items())
print(sorted_x)
print(sorted(x))

s={1:2,3:4,5:6,6:7}
sd=sorted(s.items())
sdr=sorted(s.items(),reverse=True)
print(sd)
print("Reverse sorting:",sdr)

farm={"sheep":5,"cows":2,"goats":10}
print(farm)
farm["duck"]=8
print(farm)
print(len(farm))
del(farm["cows"])
print(farm)

import operator
int_dict={"Jan":31,"Feb":28,"March":31,"April":30,"May":31,"June":30,"July":31,"Aug":31,"sep":30,"oct":31,"nov":30,"dec":31}
sorted_dict=dict(sorted(int_dict.items(),key=operator.itemgetter(0)))
sort_dict=dict(sorted(int_dict.items(),key=operator.itemgetter(1)))
print("Sorted on key",sorted_dict)
print("Sorted on values",sort_dict)
s=sorted(int_dict)
print("Keys in asc",s)
n=input("enter a month:")
print(int_dict[n])

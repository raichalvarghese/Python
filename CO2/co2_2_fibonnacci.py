#fibonacci

f1=1
f2=1
l=[]
l.append(f1)
l.append(f2)
fn=0
N=int(input("Enter N"))
while fn<N:
    fn=f1+f2
    if fn<N:
        l.append(fn)
    f1=f2
    f2=fn
print("fibonacci",l)

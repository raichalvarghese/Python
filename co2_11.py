# 
a,l,b,h,bs=[int(x) for x in input().split()]
x=lambda a:a*2
y=lambda l,b:l*b
z=lambda h,bs:0.5*(h*bs)
print("ar sq:",x(a))
print("ar rect",y(l,b))
print("ar triag",z(h,bs))


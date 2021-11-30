#question 16
text = "Hello World"
split = text.split()
#print(split)
w = split[0][0]
#print(w)
g = split[1][0]
#print(g)
r = g+split[0][1:]+ " " +w+split[1][1:]
print(r)

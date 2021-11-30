#Count the occurrences of each word in a line of text.

txt="Hello it is first class is it"
l=txt.split()
d={x:l.count(x) for x in l}
print(d)

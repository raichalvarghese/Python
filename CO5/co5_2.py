# program to copy odd lines of one file to other

f1 = open('test.txt','r')
f2 = open('f2test.txt','w')

content = f1.readlines()

for i in range(len(content)):
    if i%2==1:
        f2.write(content[i])

f2.close()
f2 = open('f2test.txt','r')
content1 = f2.read()
print(content1)

f1.close()
f2.close()

#Write a program to read a file and display the lines starting with capital letter and
#word count greater than 5.


fr = open('qn.txt','r')
fn1 = open('output.txt','w')

content = fr.readlines()
count = 0
for line in content:
    if line[0].isupper() and len(line)>5:
        fn1.write(line)

fn1.close()
fn1 = open('output.txt', 'r')

cont1 = fn1.read()
print(cont1)

fr.close()
fn1.close()

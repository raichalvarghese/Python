fn = open('file1.txt', 'r')
fn1 = open('ofile.txt','w')


content =fn.readlines()

print(content)

for line in content:
    l=line.title()
    fn1.write(l)
    
    
fn1.close()
fn1 = open('ofile.txt', 'r')


cont1 = fn1.read()
print(cont1)

fn.close()
fn1.close()

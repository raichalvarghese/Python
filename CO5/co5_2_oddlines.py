fn = open('file1.txt', 'r')
fn1 = open('ofile.txt', 'w')
content = fn.readlines()

for i in range(0, len(content)):
    if(i % 2== 0):
        fn1.write(content[i])
        
fn1.close()

fn1 = open('ofile.txt', 'r')

cont1 = fn1.read()

print(cont1)

fn.close()
fn1.close()

fn = open('file1.txt', 'r')
fn1 = open('ofile.txt','r')
fn2 = open('file2.txt','')

content1 = fn.readlines()
content2 = fn1.readlines()

content = fn1.append(fn2)
fn2.write(content)
    
fn2.close()
fn2 = open('file2.txt', 'r')


cont = fn2.read()
print(cont)

fn.close()
fn1.close()
fn2.close()

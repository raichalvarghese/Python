# program to read a file line by line and store it into a list

def read(fname):
    with open(fname) as f:
        content = f.readlines()
        print(content)



read('test.txt')

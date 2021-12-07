# pangram

def pangram(x):
    s=[]
    temp="abcdefghijklmnopqrstuvwxyz"
    for i in x:
        if i in temp:
            if i not in s:
                s.append(i)
    s = sorted(s)
    s = "".join(s)
    if s==temp:
        return True
    else:
        return False


txt=input("Enter the text:")
if pangram(txt):
    print("Is a pangram")
else:
    print("Not a pangram")

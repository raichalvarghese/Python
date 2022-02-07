import csv
dict_value = [
{"Name":"Riya","MFC":88,"DC":79,"DS":78,"ASE":58},
{"Name":"Anu","MFC":88,"DC":69,"DS":71,"ASE":58},
{"Name":"Deva","MFC":68,"DC":99,"DS":58,"ASE":88},
{"Name":"Anil","MFC":68,"DC":69,"DS":73,"ASE":88},
{"Name":"rahul","MFC":75,"DC":69,"DS":86,"ASE":78},
{"Name":"Ansa","MFC":88,"DC":100,"DS":75,"ASE":78},
{"Name":"Benchamin","MFC":84,"DC":95,"DS":98,"ASE":70},
{"Name":"Asan","MFC":51,"DC":99,"DS":97,"ASE":79},
{"Name":"Malavika","MFC":89,"DC":89,"DS":78,"ASE":87},
{"Name":"Kevin","MFC":85,"DC":69,"DS":78,"ASE":78},]


fields = ["Name","MFC","DC","DS","ASE"]

with open('dictexam.csv','w') as csvfile:
    writer = csv.DictWriter(csvfile,fieldnames=fields)
    writer.writeheader()
    writer.writerows(dict_value)
    csvfile.close()
print("percentage\n")
mfc=0
dc=0
ds=0
ase=0

with open('dictexam.csv','r') as csvfiles:
    readerobj = csv.DictReader(csvfiles)
    for row in readerobj:
         print(row['Name'],":",float(float(int(row['MFC'])+int(row['DC'])+int(row['DS'])+int(row['ASE']))/400)*100,"%")
         mfc=mfc+int(row['MFC'])
         dc=dc+int(row['DC'])
         ds=ds+int(row['DS'])
         ase=ase+int(row['ASE'])
print("average ")
print("MFC",mfc/10)
print("DC",dc/10)
print("DS",ds/10)
print("ASE",ase/10)

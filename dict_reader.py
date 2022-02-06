text = "button"

Dict = {i: text.count(i) for i in set(text)}
import csv
f = open("letters.csv","w")
writer = csv.DictWriter(f,fieldnames = ["letter","count"])
writer.writeheader()

for i in range(len(text)):
    write.writerow({"letter":,"count":Dict[i]})
    

#. Write a Python program to create a CSV file to store names of 10 students and their
#marks in four subjects. Find the percentage of each student and display the details.
#Also display the class average of each subject.

import csv

f = "mark.csv"
fields = []
rows = []
with open(f,'r') as csvfile:  
    csvreader = csv.reader(csvfile)
    fields = next(csvreader)
    for row in csvreader:
        rows.append(row)
        
    print("Total no. of rows: %d"%(csvreader.line_num))
    



    
print("% of each student")
s=0
for row in rows[:10]:
    
    for col in row:
        
        print(col[])
    print(s)
    

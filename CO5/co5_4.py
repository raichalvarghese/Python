#program to read specific columns of a given CSV file and print the content
#of the columns



import csv

with open('dep.csv') as csvfile:
    data = csv.reader(csvfile)
    for row in data:
        print(row[0]) #print the column of names from the file

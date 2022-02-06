#program to read each row from a given csv file and print a list of strings



import csv
with open('dep.csv') as csvfile:
    data = csv.reader(csvfile)
    for row in data:
        print(','.join(row))

#Write a Python program to write a Python dictionary to a csv file. After writing the CSV file
#read the CSV file and display the content.

import csv

d =[ {'l':'Adam'},{'l':'Ben'},{'l':'Cyril'},{'l':'David'}]

fieldname = ['letter']


with open("dict.csv" ,'w') as csvfile:
    writer = csv.DictWriter(csvfile,fieldnames=fieldname)
    writer.writeheader()
    writer.writerow(d)

""" Reads a csv with First and Last name columns.
    Produces a CSV file name guestInputs.csv that has columns
    First, Last, Email
    
    The domain for the email will be a funkydomain.com"""

import csv

newList = []
with open('fakeNames.csv', 'r', newline='') as infile:
    inreader = csv.reader(infile)
    for row in inreader:
        email = row[0][0:1]+row[1]+'@funkydomain.com'
        row.append(email)
        newList.append(row)
newList.pop(0) #remove headers

with open('guestInputs.csv','w') as outfile:
    csvout  = csv.writer(outfile)
    for row in newList:
        csvout.writerow(row)









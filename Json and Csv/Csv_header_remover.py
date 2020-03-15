'''
Program to take away headers and merge all *.csv file data
in a new *.csv file
'''

import csv
import os

#TODO Find all csv in the working dir
dirname = 'Header Removed'
os.makedirs(dirname, exist_ok=True)

for csvFilename in os.listdir('.'):
    if not csvFilename.endswith('.csv'):
        continue

    print('Removing header from ' + csvFilename)

#TODO Read every file
    csvRows = []
    csvFileObj = open(csvFilename)
    readerObj = csv.reader(csvFileObj)
    for row in readerObj:
        if readerObj.line_num == 1:
            continue
        csvRows.append(row)
    csvFileObj.close()

#TODO write content (except first line) to a new file
    csvFileObj = open(os.path.join(dirname, csvFilename), 'w', newline='')
    csvWriter = csv.writer(csvFileObj)
    for row in csvRows:
        csvWriter.writerow(row)
    csvFileObj.close()

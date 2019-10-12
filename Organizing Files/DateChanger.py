'''
CHANGES AMERICAN STYLE DATES TO EUROPEAN STYLE ONE
Here’s what the program does:
• It searches all the filenames in the current working directory for American-style dates.
• When one is found, it renames the file with the month and day swapped to make it European-style.

This means the code will need to do the following:
• Create a regex that can identify the text pattern of American-style dates.
• Call os.listdir() to find all the files in the working directory.
• Loop over each filename, using the regex to check whether it has a date.
• If it has a date, rename the file with shutil.move()
'''
#! python3
# renameDates.py - Renames filenames with American MM-DD-YYYY date format  
# to European DD-MM-YYYY

import shutil, os, re

count = 0
#Create the regex for dates
americanDate = re.compile(r"""^(.*?) # match the start in non greedy mode (look for anything before the pattern)
           ((0|1)?\d)-           # get the month even 1 digit only
           ((0|1|2|3)?\d)-       # get the day
           ((19|20)?\d{2})       # get the year, even in short format
           (.*?)$                # get the text after the date, if any
           """, re.VERBOSE)
# TODO: Loop over the files in the working directory.
for file in os.listdir('.'):
    mo = americanDate.search(file)
    # TODO: Skip files without a date.
    if mo == None:
        continue

    # TODO: Get the different parts of the filename.
    before = mo.group(1)
    month = mo.group(2)
    day = mo.group(3)
    year = mo.group(4)
    after = mo.group(5)

    # TODO: Form the European-style filename.
    europeFile = before + day + '-' + month + '-' + year + after 

    # TODO: Get the full, absolute file paths.
    abswd = os.path.abspath(path)
    americanFile = os.path.join(abswd, file)
    europeFile = os.path.join(abswd, europeFile)
    
    # TODO: Rename the files.
    shutil.move(americanFile, europeFile)
    count = count + 1

print('FINISHED! %d file renamed!' % (count))

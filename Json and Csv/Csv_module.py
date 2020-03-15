'''
CSV stands for “comma-separated values,” and CSV files are simplified spreadsheets 
stored as plaintext files. Python’s csv module makes it easy to parse CSV files.

CSV files are simple, lacking many of the features of an Excel spread-sheet. 
For example, CSV files
• Don’t have types for their values—everything is a string
• Don’t have settings for font size or color
• Don’t have multiple worksheets
• Can’t specify cell widths and heights
• Can’t have merged cells
• Can’t have images or charts embedded in them

On the other hand, this is also its biggest advantage: simplicity. Can be viewed even 
in text editors.

------------------------Reader Object------------------------
To read data from a CSV file, a Reader obj that let you cycle over lines is needed.
After storing datas in a variable, you can access single cells like data[row][col]

------------------------Writer Object------------------------
A Writer object lets you write data to a CSV file. 
To create a Writer object, you use the csv.writer() function.

------------------------Delimiter and Lineterminaotr Argunents------------------------
Passing arguments to the "writer" let you specify the 2 values.
If you want to separate cells with a tab character instead of a comma 
and you want the rows to be double-spaced, for example, you can do it!

'''

#============ Reader object (loop) ============#
import csv                                  # module needed
exFile = open("example.csv")                  
fReader = csv.reader(exFile)                # initialize reader
for row in fReader:
    print('Row #' + str(fReader.line_num)+ ' ' + str(row) )
data = list(fReader)                        # store rows in a list
data                                        # output in interactive shell
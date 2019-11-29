'''
Every spreadsheet document is called 'workbook' and has the .xlsx extension.
Every workbook is made of sheets (the one viewed is the 'active sheet').
Every sheet is made of columns (starting at A), and rows (starting at 1).
Every row and col is made up of cells, containing numbers or text.

In this guide, I'll use the OPENPYXL module to work with this type of files. (Currently 3.0.1)
In case of updates, look at the documentation: http://openpyxl.readthedocs.org/

The file I'm going to use is the 'example.xlsx' provided by nostarch.com .

------------------------Opening Files with OpenPyXL------------------------
The openpyxl.load_workbook() function takes in the filename and returns
a value of the workbook data type. This Workbook object represents the Excel
file, almost like how a File object represents an opened text file.

------------------------Useful functions for the Workbook------------------------
get_sheets_names()    |   return a list with the names of the sheets in the workbook
get_sheet_by_name()   |   return a Workbook object
get_active_sheet()    |   return the Workbook object of the currently active sheet
sheet['A1']           |   return a Cell object
sheet['A1'].value     |   return the content of the cell (like a getter)

The position of each cell can be determineed by sing sheet.cell(row= x, column= y)

------------------------h------------------------


'''
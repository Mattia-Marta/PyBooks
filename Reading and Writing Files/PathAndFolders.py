'''
cwd = current working directory; 
Double \\ is used, une for the path, one to escape the char.

To create a folder use: makedirs($PATH)
Appending smthing to path.* you can 
 - join: obtain a path, the best way is using os.path.join('dir1', 'dir2'..., 'dirn'); it will use the right os separator
 - abspath(path): return a string of the absolute path
 - isabs(path): boolean, return true if it is an absolute path
 - relpath('path', 'start'): return the rel path from the indicated start
 - dirname(path): return everything before the last slash 
 - basename(path): return everything after the last slash
 - split(path): return a tuple made of (dirname, basename)
 - getsize(path): return the size in bytes of the file in the path argument
 - listdir(path): return a list of filename strings for each file in the path argument
 - exists(path): bool, return true if the path exists
 - isfile(path): bool, return True if it exists and is a file
 - isdir(path): bool, return True if it exists and is a directory
'''

import os

#os.getcwd -> restituisce l'attuale cwd
os.getcwd()

#os.chdir('path') -> like cd, change the path of the cwd
os.chdir('C:\\Windows\\System32')

#creating folders
os.makedirs('path')

#print files path based on the os
myFiles = ['accounts.txt', 'details.csv', 'invite.docx']
for filename in myFiles:
    print(os.path.join('C:\\Users\\asweigart', filename))

#?Result:
#C:\Users\asweigart\accounts.txt
#C:\Users\asweigart\details.csv
#C:\Users\asweigart\invite.docx
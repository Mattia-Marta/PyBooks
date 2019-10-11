'''
SHUTIL MODULE

It means shell utilities:
shutil.*:
 - copy(source, destination): copy file from source to destination. Return the destination path
 - copytree(source, destination): copy folder (waterfall style) from src to dest.
 - move(source, destination): it's like the "cut" command, can even rename while moving
 - rmtree(path): remove, recursively, a folder with it's content.

Some os.*:
 - unlink(path): remove a file at path
 - rmdir(path): remove an empty folder

To safely delete a file is possible to use send2trash

To manage zip files, it's possible to use zipfile module and can be used with:
 - ZipFile('filename'): like open() func
 - obj.namelist(): return a list of the content
 - getinfo('filename'): it returns the a ZipInfo obj that knows
     - ZipInfoObj.file_size: return the decompressed file size
     - ZipInfoObj.compress_size: return the size of the zip file
 - extractall(): extract all the content of the ZipFile into the cwf
 - extract('filename', 'location'): extract the specified file into the location

'''

import shutil, os, send2trash

os.chdir('C:\\')
shutil.copy('C:\\spam.txt', 'C:\\Delicious')

#to rename eggs in chicken_alpha
shutil.move('C:\\eggs.txt', 'C:\\chicken_alpha.txt')

#to delete all the files with a certain extension
os.chdir('D:\Projects & courses\Python')
for file in os.listdir():
    if file.endswith('ext'):
        os.unlink(file)
        #print(file) #use to debug instead of f'in everything up

import send2trash>>> baconFile = open('bacon.txt', 'a')   # creates the file
baconFile.write('Bacon is not a vegetable.')
baconFile.close()
send2trash.send2trash('bacon.txt')


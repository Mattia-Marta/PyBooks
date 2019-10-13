'''
There are 3 steps in t/w a file in Python:
 1- Use open() to return a File object
 2- Use read() or write() on the File object
 3- Close the File using close().

The File object can be opened in 3 ways:
 - 'r' as a second argument to open() (default).
 - 'a' as a second argument to open() in append mode (strart writing at eof)
 - 'w' as a second argument to open() as write methon (overwrite everything) 
    if the file doesn't exist, it gets created

To see the content of a file, use read() method.
If the file is multi-lined (highly probable) readlines() get a list of strings, 1 for each line.

To save variables is possible to use the shelve Module. Once the file is open, it is on r/w mode
Il works almost like a dictionary and can conserve lists in variables.
Like dictionaries, shelve has keys() and values() methods.

Another method to store variables from dictionaries is to use pprint.pformat() wich will 
pprint text into a variable (String) which can be written into a .py file and imported whenever need.

'''
import os, shelve, pprint

helloFile = open('C:\\Users\\home_folder\\filename.txt')
helloFile = open('C:\Users\home_folder\filename.txt', 'r')
helloContent = helloFile.read()

#============ Create file, write, close, reopen in ============#
#============  append mode, close, read and print  ============#
baconFile = open('bacon.txt', 'w')
baconFile.write('Hello world!\n')
baconFile.close()
baconFile = open('bacon.txt', 'a')
baconFile.write('I like crispy bacon so much!\n')
baconFile.close()
text = baconFile.read()
baconFile.close()
print(text)


#============ Example of the shelve module ============#
shelfFile = shelve.open('mydata')
dogs = ['pippo', 'pluto', 'leone']
shelfFile['dogs'] = dogs
shelfFile.close()
#--- snip ---#
shelfFile = shelve.open('mydata')
type(shelfFile) #returns <class 'shelve.DbfilenameShelf'>
shelfFile['dogs'] #returns ['pippo', 'pluto', 'leone']
shelfFile.close()

shelfFile = shelve.open('mydata')
list(shelfFile.keys()) #return a list of the keys, in this case ['dogs']
list(shelfFile.values()) #return a list of the vals, in this case ['pippo', 'pluto', 'leone']


#============ Example of the pprint.pformat() method ============#
dogs = [{'name': 'pippo', 'desc': 'thin'}, {'name': 'pluto', 'desc': 'stupid'}]
pprint.pformat(dogs)
fileObj = open('myDogs.py', 'w')
fileObj.write('dogs = ' + pprint.pformat(dogs) + '\n')
fileObj.close()

import myDogs.py #once imported can be used as any dictionary

myDogs.dogs #will return the whole dictionary
myDogs.dogs[0] #will return the 1st term of the dictionary
myDogs.dogs[0]['name'] #will return the param 'name' of the 1st element.
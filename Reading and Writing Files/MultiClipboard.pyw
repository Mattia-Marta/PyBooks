'''
The program will save each piece of clipboard text under a keyword. 
For example, when you run py mcb.pyw save spam, the current contents of the clipboard 
will be saved with the keyword spam. 
This text can later be loaded to the clipboard again by running py mcb.pyw spam. 
And if the user forgets what keywords they have, 
they can run py mcb.pyw list to copy a list of all keywords to the clipboard.

Here’s what the program does:
• The command line argument for the keyword is checked.
• If the argument is save, then the clipboard contents are saved to the keyword.
• If the argument is list, then all the keywords are copied to the clipboard.
• Otherwise, the text for the keyword is copied to the keyboard.

This means the code will need to do the following:
• Read the command line arguments from sys.argv.
• Read and write to the clipboard.
• Save and load to a shelf file.

File is saved as pyw so that no terminal window is shown when run.
'''

#! python3
# MultiClipboard.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#        py.exe mcb.pyw list - Loads all keywords to clipboard.

import shelve, clipboard, sys

mcbShelf = shelve.open('mcb')

#TODO: save clipboard content
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = clipboard.paste()

#TODO: List keywords and load content
elif len(sys.argv == 2):
    if sys.argv[1].lower() == 'list':
        clipboard.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        clipboard.copy(str(mcbShelf[sys.argv[1]]))

mcbShelf.close()
'''
 Phone number and email Address extractor
 
 Say you have the boring task of finding every phone number and email address in a long web page or document. 
 If you manually scroll through thepage, you might end up searching for a long time. 
 But if you had a pro-gram that could search the text 
 in your clipboard for phone numbers and email addresses, 
 you could simply press ctrl-A to select all the text, press ctrl-c to copy it to the clipboard,
 and then run your program. It could replace the text on the clipboard 
 with just the phone numbers and email addresses it finds.
'''
#TODO: 
#? 1- Get the text from the clipboard 
#? 2- Look for patterns (numbers and mails) with regex
#? 3- "Edit" the clipboard.

import re, clipboard

#* Create the 2 objects for mail and phone numbers
phoneRegex = re.compile(r'''(    
    (\d{3}|\(\d{3}\))                 # area code    
    (\s|-|\.)?                        # separator    
    (\d{3})                           # first 3 digits    
    (\s|-|\.)?                        # separator    
    (\d{4})                           # last 4 digits    
    (\s*(ext|x|ext.)\s*(\d{2,5}))?    # extension    
    )''', re.VERBOSE)

mailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+      # username
    @                      # @ symbol
    [a-zA-Z0-9.-]+         # domain name
    (\.[a-zA-Z]{2,4})      # dot-something
    )''', re.VERBOSE)

#?Find matches in clipboard
text = str(clipboard.paste())

#Debugging test print (text)

matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':        
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
for groups in mailRegex.findall(text):
    matches.append(groups[0])
    
#?Re-"edit" the clipboard
if len(matches) == 0:
    matches = 'Nothing found, bro!'
else:
    clipboard.copy(str(matches))
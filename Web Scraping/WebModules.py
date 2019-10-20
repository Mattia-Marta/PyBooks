'''
------------------------WEB SCRAPING------------------------
Web scraping is the term for using a program to download and process content from the Web.

A little hand for this is given by python with:
• webbrowser:
    Comes with Python and opens a browser to a specific page.
• Requests:
    Downloads files and web pages from the Internet.
• Beautiful Soup:
    Parses HTML, the format that web pages are written in.
• Selenium:
    Launches and controls a web browser. Selenium can fill in forms and simulate mouse clicks

------------------------WEBBROWSER------------------------
It's open(url) function launch a new browser to a specified URL.
It cannot do much more than that.
Check "MapAddress.py to see a practical applicaiton of this command

------------------------REQUEST------------------------
This module needs to be installed using 'pip install requests', it returns a Response obj.
res.raise_for_status() output the captured exception.

It is possible to download files to the hard drive, only if saved in unicode (wb attribute).
It can be done using a for to iterate over the obj's iter_content() using write() on each iteration
to write the chunk to the file. After this, the file can be closed.

'''

import webbrowser
webbrowser.open('http://www.google.com') #launch default browser on a specific page.

#Example of request
import requests
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
print (res.text[250:])

#Managing errors with request
res = requests.get('https://automatetheboringstuff.com/files/romjul.txt')
try:
    res.raise_for_status()
except Exception as exc:
    print('There was a problem!. %s' % (exc))

#Downloading an internet page to hard drive:
import requests
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
res.raise_for_status()
playFile = open('RomeoAndJuliet.txt', 'wb')
for chunk in res.iter_content(100000):
    playFile.write(chunk)

playFile.close()
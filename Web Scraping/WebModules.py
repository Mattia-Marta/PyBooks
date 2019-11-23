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

------------------------BEAUTIFUL SOUP------------------------
This module needs to be installed using 'pip install bs4'. The object you will work with
can be obtained by a request.get() or using open('file.html') and then using bs4.BeautifulSoup(file)
Elements of the web page can be retrieved using select() passing a string of css selector.

soup.select('div')                   |  All elements named <div>
soup.select('#author')               |  The element with an id attribute of author
soup.select('.notice')               |  All elements that use a CSS class attribute named notice
soup.select('div span')              |  All elements named <span> that are within an element named <div>
soup.select('div > span')            |  All elements named <span> that are directly within an element named <div>, with no other element in between
soup.select('input[name]')           |  All elements named <input> that have a name attribute with any value
soup.select('input[type="button"]')  |  All elements named <input> that have an attribute named type with value button

After the select() function, you can extrapolate almost everything using:
results[i].getText()    |    returns the content without tags
results[i].attrs        |    returns the list of attributes catch in a json-like style
str(results[i])         |    returns the whole string, tags included.

where results[i] is the element at the i position of the BeautifulSoup.

To learn more about bs4: http://www.crummy.com/software/BeautifulSoup/bs4/doc/

------------------------SELENIUM------------------------
Selenium allows you to interact with web pages in a much more advanced way than Requests and Beautiful Soup; 
but because it launches a web browser, it is a bit slower and hard to run in the background.


'''

#the file i'll use for the explanation is example.html

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

#Getting data from Element's Attributes
import bs4
soup = bs4.BeautifulSoup(open('example.html'), features="html.parser")
spanEl = soup.select('span')[0]
str(spanEl)
spanEl.get('id')
spanEl.attrs
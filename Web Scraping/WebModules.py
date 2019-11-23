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
Selenium module is initialized as 'from selenium import webdriver'. using webdriver.Firefox() opens up the designed browser.

WebDriver objs have different methods for finding elements:
browser.find_element_* and browser.find_elements_*; the first return a WebElement corresponding to the firts match,
                                                    the second one, return a list with every match in the page.

by_css_selector(selector)   |  Elements that match the CSS selector
by_class_name(name)         |  Elements that use the CSS class name
by_name(name)               |  Elements with a matching nameattribute value
by_id(id)                   |  Elements with a matching id attribute value
by_tag_name(name)           |  Elements with a matching nameattribute value (case unsensitive)
by_link_text(text)          |  <a> elements that completely match the text provided 
by_partial_link_text(text)  |  <a> elements that contain the text provided

After the find_element function, you can navigate the content using:
tag_name             |  The tag name, such as 'a' for an <a> element
get_attribute(name)  |  The value for the element’s name attribute
text                 |  The text within the element, such as 'hello' in <span>hello</span>
clear()              |  For text field or text area elements, clears the text typed into it
is_displayed()       |  Returns True if the element is visible; otherwise returns False
is_enabled()         |  For input elements, returns True if the element is enabled; otherwise returns False
is_selected()        |  For checkbox or radio button elements, returns True if the element is selected; otherwise returns False
location             |  A dictionary with keys 'x' and 'y' for the position of the element in the page
click()              |  Emulate a click in the page.

Using selenium you can send keystrokes on a page if you find a textarea or an input field.
The elem.send_keys(key) can even send special keys:
Keys.ENTER/RETURN                |  The enter and return keys
Keys.DOWN/UP/LEFT/RIGHT          |  The keyboard arrow keys
Keys.HOME/END/PAGE_DOWN/PAGE_UP  |  The home, end, pagedown, and pageup keys
Keys.ESCAPE/BACK_SPACE/DELETE    |  The esc, backspace, and delete keys
Keys.F1/.../F12                  |  The F1 to F12 keys at the top of the keyboard
Keys.TAB                         |  The tab key

Some more useful commands, interacting with the browser window itself, are:
browser.back()     |  Clicks the back button, going back to the previous page
browser.forward()  |  Clicks the forward button, going to the next page
browser.refresh()  |  Clicks the reload button to refresh the page
browser.quit()     |  Clicks the 'x' closing the browser window

'''

#the file i'll use for this explanation is example.html

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

#Application of selenium (will return "Found <img> element with that class name!")
from selenium import webdriver
browser = webdriver.Firefox()
browser.get('http://inventwithpython.com')
try:    
    elem = browser.find_element_by_class_name('bookcover')    
    print('Found <%s> element with that class name!' % (elem.tag_name))
except:    
    print('Was not able to find an element with that name.')
    

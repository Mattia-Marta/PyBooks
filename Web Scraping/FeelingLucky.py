#! python3
#FeelingLucky.py - open several g-tab about a topic
'''
• Gets search keywords from the command line arguments.
• Retrieves the search results page.
• Opens a browser tab for each result.

This means your code will need to do the following:
• Read the command line arguments from sys.argv.
• Fetch the search result page with the requests module.
• Find the links to each search result.
• Call the webbrowser.open() function to open the web browser.

searches on google work like " https://www.google.com/search?q=stuff_to_find"

'''
import requests, sys, bs4, webbrowser

ans = input('Feeling Lucky?').lower()


if ans.startswith('y'):
    link = 'http://google.com/search?q=' + '+'.join(sys.argv[1:])
    print (link)
    res = requests.get(link)
    res.raise_for_status()
    #Retrive top search links
    soup = bs4.BeautifulSoup(res.text, features="html.parser")
    linkEls = soup.select('html', class_='riUh30 bc')
    #print(linkEls)
    #Opening brwser tabs for results
    numOpen = min(5, len(linkEls)) #Open 5 links or less if fewer
    for i in range(numOpen):
        print('http://google.com' + linkEls[i].get('href'))
        #webbrowser.open('http://google.com' + linkEls[i].get('href'))

else:
    print('go and google it yourself!')
    webbrowser.open('http://google.com')

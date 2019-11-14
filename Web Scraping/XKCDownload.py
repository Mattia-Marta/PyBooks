'''
• Loads the XKCD home page.
• Saves the comic image on that page.
• Follows the Previous Comic link.
• Repeats until it reaches the first comic.

This means your code will need to do the following:
• Download pages with the requests module.
• Find the URL of the comic image for a page using Beautiful Soup.
• Download and save the comic image to the hard drive with iter_content().
• Find the URL of the Previous Comic link, and repeat
'''
import requests, os, bs4
url = 'http://xkcd.com'               # starting url
os.makedirs('xkcd', exist_ok=True)    # store comics in ./xkcd

while not url.endswith('#'):    
    # TODO: Download the page.    
    print('Downloding %s...' % url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text)
    
    # TODO: Find the URL of the comic image.    
    comic = soup.select('#comic img')       #img tag inside a div with id = 'comic'
    if comic == []:
        print('No image found.')
    else:
        comicUrl = 'http:' + comic[0].get('src')    #get the content of the src attr of the comic
    
        # TODO: Download the image.    
        print('IMage found! %s...' % (comicUrl))
        res = requests.get(comicUrl)
        res.raise_for_status()
        
        # TODO: Save the image to ./xkcd.    
        imgFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
        for chunk in res.iter_content(100000):
            imgFile.write(chunk)
        imgFile.close()

    # TODO: Get the Prev button's url.
    previous = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + previous.get('href')

print('Done.')
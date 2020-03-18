'''
XKCD Downloader - threaded version
Just like the one found in "Web scraping" folder but working w\ threads
Now its download is in a range(x, y).
'''

import bs4, os, requests, threading

os.makedirs('xkcd', exist_ok=True)

def downloadXkcd(startComic, endComic):
    for urlNumber in range(startComic, endComic):
        print('Downloading page http://xkcd.com/%s...' % (urlNumber))
        res = requests.get('http://xkcd.com/%s' % (urlNumber))
        res.raise_for_status()

        soup = bs4.BeautifulSoup(res.text)

        comicElem = soup.select('#comic img')
        if comicElem == []:
            print('Could not find img')
        else:
            comicUrl = comicElem[0].get('src')
            print('Downloading image %s...' % (comicUrl))
            print(comicUrl)
            res = requests.get(comicUrl)
            res.raise_for_status()

            imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()

#TODO Create and start the Threads
downloadThreads = []
for i in range(0, 1400, 100):
    downloadThread = threading.Thread(target=downloadXkcd, args=(i, i+99))
    downloadThreads.append(downloadThread)
    downloadThread.start()

#TODO Wait for all threads to end
for downloadThread in downloadThreads:
    downloadThread.join()
print('Done!')

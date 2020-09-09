#! python3
# downloadXkcd - Download evert single Xkcd comic.

import bs4
import requests
import os
import threading

if not os.path.exists('xkcd'):
    os.mkdir('xkcd')


def downloadXkcd(startNum, endNum):
    for comicNum in range(startNum, endNum):
        # Download the page.
        url = 'http://xkcd.com/%s' % comicNum
        print('Downloading page %s......' % url)
        res = requests.get(url)
        res.raise_for_status()

        soup = bs4.BeautifulSoup(res.text, features='html.parser')

        # Find the URL of the comic image.
        linkElem = soup.select('#comic img')
        if not linkElem:
            print('Could not find the comic')
        else:
            comicURL = 'http:' + linkElem[0].get('src')
            # Download the image.
            print('Downloading comic %s' % comicURL)
            res = requests.get(comicURL)
            res.raise_for_status()

            # Save the image to ./xkcd
            imageFile = open(os.path.join('xkcd', os.path.basename(comicURL)), 'wb')
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()

        # # Get the prev button's url
        # prevLink = soup.select('a[rel = "prev"]')[0]
        # url = 'http://xkcd.com' + prevLink.get('href')


downloadThreads = []
for i in range(0, 1400, 100):
    downloadThread = threading.Thread(target=downloadXkcd, args=(i, i + 99))
    downloadThreads.append(downloadThread)
    downloadThread.start()

for downloadThread in downloadThreads:
    downloadThread.join()
print('Done.')

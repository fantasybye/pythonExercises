#! python3
# feelingLuckyGoogle.py - Open several Google search results.

import sys
import requests
import webbrowser
import bs4

print('Googling......') # display text while downloading the Google page
res = requests.get('https://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

# Retrieve top search result links
soup = bs4.BeautifulSoup(res.text)

# Open a browser tab for each result
linkElem = soup.select('.r a')
numOpen = min(3, len(linkElem))
for i in range(numOpen):
    webbrowser.open('https://google.com' + linkElem[i].get('href'))

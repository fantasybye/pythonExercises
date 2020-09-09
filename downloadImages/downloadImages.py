#! python3
# downloadImages.py - download the images searched on baidu.com

import sys
import requests
import os
import re

url = 'https://image.baidu.com/search/index?tn=baiduimage&word='

if len(sys.argv) < 1:
    print('Need a key word')
else:
    if not os.path.exists(str(sys.argv[1])):
        os.mkdir(str(sys.argv[1]))
    # print(url + str(sys.argv[1]))
    res = requests.get(url + str(sys.argv[1]))
    res.raise_for_status()
    imgLinks = re.findall(r'"thumbURL":".*?\.jpg', res.text)
    links = []
    for link in imgLinks:
        links.append(link[12:])
    # soup = bs4.BeautifulSoup(res.text, features='html.parser')
    # imageElems = soup.select('#imgid div')
    # if not imageElems:
    #     print('Could not find any images')
    # else:
    #     for i in range(len(imageElems)):
    #         imageURL = imageElems[i].get('data-thumburl')
    #         print('downloading image' + str(i))
    i = 1
    for imageURL in links:
        res = requests.get(imageURL)
        res.raise_for_status()
        imageFile = open(os.path.join(str(sys.argv[1]), str(sys.argv[1]) + str(i)) + '.jpg', 'wb')
        # print(os.path.join(str(sys.argv[1]), str(sys.argv[1]) + str(i)) + '.jpg')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()
        i += 1


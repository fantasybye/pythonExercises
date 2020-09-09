#! python3
# 写一个函数，它接受一个字符串，做的事情和 strip()字符串方法一样。如果只
# 传入了要去除的字符串，没有其他参数，那么就从该字符串首尾去除空白字符。否
# 则，函数第二个参数指定的字符将从该字符串中去除。

import re

print('Enter the text to be stripped')
text = input()
print('Enter the word to strip')
word = input()

def myStrip(text, word = ''):
    if word:
        regex = re.compile(word)       
    else:
        regex = re.compile(r'^\s+|\s+$')
    return regex.sub('', text)

print(myStrip(text, word))

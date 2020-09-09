#! python3
# strongPassword - create a Regex to test strong passwords like this:
# 长度不少于8个字符
# 同时包含大写和小写字符
# 至少有一位数字

import re

#input the password
print('Please enter a password:')
password = input()

#Create a password regex
def test(password):
    if len(password) < 8:
        return False
    
    lowerAlphabetRegex = re.compile(r'[a-z]+') 
    if lowerAlphabetRegex.findall(password) == []:
        return False

    upperAlphabetRegex = re.compile(r'[A-Z]+')
    if upperAlphabetRegex.findall(password) == []:
        return False

    demicalRegex = re.compile(r'\d+')
    if demicalRegex.findall(password) == []:
        return False

    return True

print(test(password))

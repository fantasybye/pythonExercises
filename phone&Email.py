#! python3
# phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard.

import pyperclip,re

#Create phone regex.
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?  #area code
    (\s|-|\.)?          #first 3 digits
    (\d{3})             #separator
    (\s?|-|\.)          #last 4 digits
    (\d{4})             #extension
    (\s*(ext|x|ext.)\s*(\d{2,5}))?
    )''', re.VERBOSE)

#Create email regex.
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+   #username
    @
    [a-zA-Z0-9.-]+      #domain name
    (\.[a-zA-Z]{2,4})   #dot-something
    )''', re.VERBOSE)

#Find matches in clipboard text.
text= str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3],groups[5]])
    if groups[8] != '':
        phoneNum += 'x' + groups[8]
    matches.append(phoneNum)

for groups in emailRegex.findall(text):
    matches.append(groups[0])

#Copy results to the clipboard.
if len(matches) > 0:
    result = '\n'.join(matches)
    pyperclip.copy(result)
    print('Copied to clipboard:')
    print(result)
else:
    print('No phone number or email address found.')

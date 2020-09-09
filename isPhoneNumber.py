import re

phoneNumRegex = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
mo = phoneNumRegex.findall('My number is 415-555-4242.')
string = ''.join(str(mo))
print('Phone number found: ' + string)

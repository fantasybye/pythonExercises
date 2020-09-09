import re


madLibsTxt = open('madLibsTxt.txt')
content = madLibsTxt.read()
madLibsTxt.close()

WORDS = ['ADJECTIVE', 'NOUN', 'VERB']
wordRegex = '|'.join(WORDS)

mo = re.compile(wordRegex)
result = mo.search(content)

while result != None:
    change = result.group()
    answer = input(f"Enter an {change.lower()}:\n")
    content = mo.sub(str(answer),content,1)
    result = mo.search(content)

madLibsTxt = open('madLibsTxt.txt', 'w')
madLibsTxt.write(content)
madLibsTxt.close()

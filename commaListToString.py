def commaListToString(spam):
    result = ''
    if(len(spam) == 1):
        return spam[0]
    elif(len(spam) > 1):
        for i in range(len(spam) - 1):
            result = result + spam[i] + ','
        result = result + 'and ' + spam[-1]
    else:
        result = 'Bad input'
    return result

print('Please enter a list, commas for spacing plz:')
string = input()
temp = string.split(',')
spam = []
for i in range(len(temp)):
    spam.append(temp[i])
print(commaListToString(spam))

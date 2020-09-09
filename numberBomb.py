# This is a guess the number game.
# @Author _ffffrank

import random

class colors:
    YELLOW = '\033[33m'
    RED = '\033[31m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    
def colorPrint(color, string):
    try:
        if color == 'yellow':
            return colors.YELLOW + string + colors.ENDC
        elif color == 'red':
            return colors.RED + string + colors.ENDC
        else:   
            return string
    except Exception as e:
        print(e)
#windows IDLE 不支持\033显示，需要linux

secret = random.randint(1,100)
print('I am thinking a number between 1 and 100.')

while True:
    print('Take a guess')
    guess = int(input())

    if guess < secret:
        print('Low!')

    elif guess > secret:
        print('High!')

    else:
        print('Bomb!!!')
        break

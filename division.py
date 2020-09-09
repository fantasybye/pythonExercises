def division(divisor):
    try:
        return 40 / divisor
    except ZeroDivisionError:
        print('error')

spam = division(0)
print(spam)

print(None == spam)
              
    

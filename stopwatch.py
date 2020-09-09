#! python3
# stopwatch.py - A simple stopwatch program

import time

print('Press ENTER to begin.Afterwards, press ENTER to "click" the stopwatch.')
print('Press Ctrl+C to exit')

input()
print('Started')

startTime = time.time()
lastTime = startTime
lapNum = 1

try:
    while True:
        input()
        totalTime = round(time.time() - startTime, 2)
        lapTime = round(time.time() - lastTime, 2)
        print('Lap #%s: %s, total:%s' % (lapNum, lapTime, totalTime), end='')
        lapNum += 1
        lastTime = time.time()
except KeyboardInterrupt:
    print('\nDone')

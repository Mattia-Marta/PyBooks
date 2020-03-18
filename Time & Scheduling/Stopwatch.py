'''
A simple stopwatch program.

At a high level, here’s what your program will do:
• Track the amount of time elapsed between presses of the enter key, 
  with each key press starting a new “lap” on the timer.
• Print the lap number, total time, and lap time.
'''
import time, random

print('Hit ENTER to begin. Afterwards, press ENTER to click the stopwatch. (Ctrl+C to quit)')
input()
print('Started')
start = time.time()
last = start
lapNum = 1
best = [0, 100]
try:
    while True:
        input()
        lapTime = round(time.time() - last, 2)
        if lapTime < float(best[1]):
            best = [lapNum, lapTime]

        last = time.time()
        total = round(time.time() - start, 2)
        print('Lap %s) %s (%s)' % (lapNum, total, lapTime), end='')
        lapNum += 1 
except KeyboardInterrupt:
    print('\nLap #%s was your fastest lap! Time : %s\n' % (best[0], best[1]))
    
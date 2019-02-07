#! python3
# stopwatch.py - A simple stopwatch program.
import time
import pyperclip
# Display the program's instructions.
print('Press ENTER to begin. Afterwards, press ENTER to "click" the stopwatch.\
Press Ctrl-C to quit.')
input()
# press Enter to begin
print('Started.')
startTime = time.time()
# get the first lap's start time
lastTime = startTime
lapNum = 1
totalOutputString = ''

try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        totalTime = str(totalTime).rjust(5)
        lapTime = str(lapTime).rjust(5)
        outputString = 'Lap # ' + str(lapNum) + ': ' +\
            totalTime + ' (' + lapTime + ')'
        totalOutputString += outputString + '\n'
        print(outputString, end='')
        lapNum += 1
        lastTime = time.time()  # reset the last lap time
        pyperclip.copy(totalOutputString)
except KeyboardInterrupt:
    # Handle the Ctrl-C exception to keep its error message from displaying.
    print('\nDone.')

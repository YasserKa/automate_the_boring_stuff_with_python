import os
# frameArr
prefix = 'spam'
dirPath = 'filling_in_the_gaps'

givenNumbers = []

# get the numbers gives for the needed
for fileName in os.listdir(dirPath):
    if (fileName.startswith(prefix)):
        givenNumbers.append(int(fileName[4:len(fileName)-4]))

# sort them
givenNumbers.sort()

# create all the files that doesn't exist
firstNumber = givenNumbers[0]
lastNumber = givenNumbers[len(givenNumbers)-1]
for i in range(firstNumber, lastNumber):
    fileName = prefix+str(i)+'.txt'
    filePath = os.path.join(dirPath, fileName)
    if (not os.path.isfile(filePath)):
        fileStream = open(filePath, 'w')
        print('creating ' + filePath)
        fileStream.close()

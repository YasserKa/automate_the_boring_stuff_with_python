import re, sys, os

def isValidFileName(fileName):
    nameContent = fileName.split('.')
    return len(nameContent) > 1 and nameContent[1] == 'txt'

def processFile(fileName):
    fileStream = open('./regex_search_folder/'+fileName, 'r')
    lines = fileStream.readlines()
    for line in lines:
        if userRegex.match(line) != None:
            print(line)
    fileStream.close()

# get the user regex
if len(sys.argv) != 2:
    print('you should input a regex expression')
    sys.exit()

userRegex = re.compile(sys.argv[1])

# get all the .txt files in a folder
filesList = os.listdir('./regex_search_folder')

# loop through their content
for fileName in filesList:
    if (isValidFileName(fileName)):
        processFile(fileName)

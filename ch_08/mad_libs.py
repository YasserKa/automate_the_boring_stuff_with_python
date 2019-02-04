# get user's input
adjective = input('Enter an adjective:\n')
noun1 = input('Enter a noun:\n')
verb = input('Enter a verb:\n')
noun2 = input('Enter a noun:\n')

# open the file
inputFile   = open('mad_libs_input.txt', 'r')
fileContent = inputFile.read()
inputFile.close()

# adjust the content
fileContent = fileContent.replace('ADJECTIVE', adjective, 1)
fileContent = fileContent.replace('NOUN', noun1, 1)
fileContent = fileContent.replace('VERB', verb, 1)
fileContent = fileContent.replace('NOUN', noun2, 1)

#save the file
inputFile   = open('mad_libs_input.txt', 'w')
inputFile.write(fileContent)
print(fileContent)

#  print(fileContent)
inputFile.close()

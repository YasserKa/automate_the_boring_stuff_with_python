def formStringFromList(myList):

    statement = ''

    for i in range(len(myList)-1):
        statement += myList[i]+', '

    # append an and if there's more than one element
    if (len(myList) > 1):
        statement += 'and '
    elif(len(myList) > 0):
        statement += myList[-1]

    return statement

spam = ['apples', 'bananas', 'tofu', 'cats']
spam1 = ['apples', 'bacon']
spam2 = ['apples']
spam3 = []

print(formStringFromList(spam))
print(formStringFromList(spam1))
print(formStringFromList(spam2))
print(formStringFromList(spam3))

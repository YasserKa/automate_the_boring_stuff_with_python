import re

def myStrip(string, char = None):
    # remove whitespace at the end and the start of the string
    if char == None:
        trimRegex = re.compile(r'^\s*|\s*$')
        result = trimRegex.sub(r'\0', string)
    # remove the character from the string
    else:
        trimRegex = re.compile('['+char+']')
        result = trimRegex.sub(r'\0', string)
        pass

    print(result)

myStrip('  Hello ')
myStrip('  Hello Hello ')
myStrip('  Hello Hello Hello   ')
myStrip('    Hello')
myStrip('Hello')

myStrip('Hello', 'l')
myStrip('  Hello', 'l')

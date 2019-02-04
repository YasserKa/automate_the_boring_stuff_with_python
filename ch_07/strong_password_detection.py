# Note: the chapter doesn't explain about ? inside the (), which is necessary to solve the exercise
import re

def checkPasswordStrength(password):
    strongPasswordRegex = re.compile(r'''
            ^(?=.*[a-z]) # at least one lower case
            (?=.*[A-Z])  # at least one upper case
            (?=.*\d)     # at least one digit
            .{8,}$       # at least 8 characters
            ''',
            re.VERBOSE)
    mo = strongPasswordRegex.match(password)
    if (mo == None):
        print(password + ' is weak password')
    else:
        print(password + ' is strong password')

password1 = '123456'
password1 = 'aB23456'
password2 = '123456789'
password3 = '12345678a'
password4 = '12345678A'
password5 = 'abcdefghI1'
password6 = 'abcdefgH123'

checkPasswordStrength(password1)
checkPasswordStrength(password2)
checkPasswordStrength(password3)
checkPasswordStrength(password4)
checkPasswordStrength(password5)
checkPasswordStrength(password6)

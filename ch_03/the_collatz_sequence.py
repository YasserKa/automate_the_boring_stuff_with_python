def collatz(number):

    if (number % 2 == 0):
        value = number // 2
    else:
        value = 3 * number + 1

    print(value)
    return value

print('Enter number:')

while True:
    try:
        user_input = int(input())
        if collatz(user_input) == 1:
            break
    except Exception:
        print('the input must be integer')

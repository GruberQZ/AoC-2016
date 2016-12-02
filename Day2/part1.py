file = open('input.txt','r')

password = ''

for line in file:
    # Starting number
    number = 5
    # Go character by character
    for char in line:
        if char == 'U':
            if number != 1 and number != 2 and number != 3:
                number = number - 3
        elif char == 'D':
            if number != 7 and number != 8 and number != 9:
                number = number + 3
        elif char == 'R':
            if number != 3 and number != 6 and number != 9:
                number = number + 1
        elif char == 'L':
            if number != 1 and number != 4 and number != 7:
                number = number - 1
    password = password + str(number)

print(password)
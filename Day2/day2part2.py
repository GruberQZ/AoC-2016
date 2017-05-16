

file = open('input.txt','r')

password = ''
cannotMoveLeft = [1,2,5,10,13]
cannotMoveRight = [1,4,9,12,13]
cannotMoveUp = [1,2,4,5,9]
cannotMoveDown = [5,9,10,12,13]

for line in file:
    # Starting number
    number = 5
    # Go character by character
    for char in line:
        if char == 'U':
            if number not in cannotMoveUp:
                if number in [3,13]:
                    number = number - 2
                elif number in [6,7,8]:
                    number = number - 4
                elif number in [10,11,12]:
                    number = number - 4
        elif char == 'D':
            if number not in cannotMoveDown:
                if number in [1,11]:
                    number = number + 2
                elif number in [2,3,4]:
                    number = number + 4
                elif number in [6,7,8]:
                    number = number + 4
        elif char == 'R':
            if number not in cannotMoveRight:
                number = number + 1
        elif char == 'L':
            if number not in cannotMoveLeft:
                number = number - 1
    # Add character to the password string
    password = password + str(number) + ','

# Decode password
split = password.split(',')
finalPass = ''
for char in split:
    if char != '':
        if int(char) < 10:
            finalPass = finalPass + char
        elif char == '10':
            finalPass = finalPass + 'A'
        elif char == '11':
            finalPass = finalPass + 'B'
        elif char == '12':
            finalPass = finalPass + 'C'
        elif char == '13':
            finalPass = finalPass + 'D'

print(finalPass)
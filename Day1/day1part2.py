import sys
# Get the input file
file = open('input.txt', 'r')
# Create a list of spaces to walk
commandList = []
# Past locations
pastLocations = []
# Read through the file and add the commands to the list
command = ''
while True:
    chunk = file.read(1)
    if chunk != ' ' and chunk != ',' and chunk != '':
        command = command + chunk
    elif chunk == ' ' or chunk == ',':
        if command != '':
            commandList.append(command)
            command = ''
    elif chunk == '':
        # Done
        commandList.append(command)
        break
    # else:
    #     commandList.append(command.rstrip())
    #     command = ''

# Directions: 1 = North, 2 = East, 3 = South, 4 = West
direction = 1
xcord = 0
ycord = 0
pastLocations.append([xcord,ycord])
for step in commandList:
    # Figure out direction to walk
    if step[0] == 'R':
        # Increment
        if direction < 4:
            direction = direction + 1
        else:
            direction = 1
    else:
        # Decrement
        if direction > 1:
            direction = direction - 1
        else:
            direction = 4
    # Figure out how many spaces to walk
    for i in range(int(step[1:])):
        if direction == 1:
            ycord = ycord + 1
        elif direction == 2:
            xcord = xcord + 1
        elif direction == 3:
            ycord = ycord - 1
        elif direction == 4:
            xcord = xcord - 1
        else:
            print("Wrong direction")
        # Create an entry for the location history
        historyEntry = [xcord, ycord]
        # Check to see if this location is already in the history
        for location in pastLocations:
            if xcord == location[0] and ycord == location[1]:
                distance = abs(xcord) + abs(ycord)
                print(distance)
                sys.exit()
        # Append it to the history
        pastLocations.append(historyEntry)
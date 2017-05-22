puzzleinput = "fbgdceah"
scramble = list(puzzleinput)

def GetRightRotationsByIndex(index):
    if index == 0:
        return 7
    elif index == 1:
        return 7
    elif index == 2:
        return 2
    elif index == 3:
        return 6
    elif index == 4:
        return 1
    elif index == 5:
        return 5
    elif index == 6:
        return 0
    elif index == 7:
        return 4

# Reverse the list of instructions
instructions = []
for line in open("input.txt","r"):
    instructions.insert(0, line)

for line in instructions:
    command = line.rstrip().split(" ")
    if command[0] == "swap":
        if command[1] == "position":
            pos1 = int(command[2])
            pos2 = int(command[5])
            temp = scramble[pos1]
            scramble[pos1] = scramble[pos2]
            scramble[pos2] = temp
        elif command[1] == "letter":
            pos1 = scramble.index(command[2])
            pos2 = scramble.index(command[5])
            temp = scramble[pos1]
            scramble[pos1] = scramble[pos2]
            scramble[pos2] = temp
    elif command[0] == "rotate":
        if command[1] == "left":
            steps = int(command[2])
            for i in range(steps):
                scramble = list(scramble[-1]) + scramble[:-1]
        elif command[1] == "right":
            steps = int(command[2])
            for i in range(steps):
                scramble = scramble[1:] + list(scramble[0])
        elif command[1] == "based":
            steps = GetRightRotationsByIndex(scramble.index(command[6]))
            for i in range(steps):
                scramble = list(scramble[-1]) + scramble[:-1]
    elif command[0] == "reverse":
        low = int(command[2])
        high = int(command[4])
        steps = int((high-low)/2) + ((high-low)%2)
        for i in range(steps):
            temp = scramble[low + i]
            scramble[low + i] = scramble[high - i]
            scramble[high - i] = temp
    elif command[0] == "move":
        char = scramble.pop(int(command[5]))
        scramble.insert(int(command[2]),char)
    else:
        print("Invalid command: " + command)

password = ""
for char in scramble:
    password += char

print("Unscrambled password: " + password)
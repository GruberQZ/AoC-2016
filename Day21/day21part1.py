puzzleinput = "abcdefgh"
scramble = list(puzzleinput)

for line in open("input.txt","r"):
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
                scramble = scramble[1:] + list(scramble[0])
        elif command[1] == "right":
            steps = int(command[2])
            for i in range(steps):
                scramble = list(scramble[-1]) + scramble[:-1]
        elif command[1] == "based":
            steps = scramble.index(command[6])
            if steps >= 4:
                steps += 2
            else:
                steps += 1
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
        char = scramble.pop(int(command[2]))
        scramble.insert(int(command[5]),char)
    else:
        print("Invalid command: " + command)

password = ""
for char in scramble:
    password += char

print("Scrambled password: " + password)
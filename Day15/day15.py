import re
import sys

# Use 'input.txt' for part 1, 'input2.txt' for part 2
file = open('input2.txt','r')
regex = re.compile(r'Disc #(\d+) has (\d+) positions; at time=0, it is at position (\d+).')

discs = {}
numDiscs = 0

for line in file:
    input = line.rstrip()
    r = regex.match(input)
    discNumber = int(r.group(1))
    positions = int(r.group(2))
    startingPos = int(r.group(3))
    discs[discNumber] = {}
    discs[discNumber]["position"] = startingPos
    discs[discNumber]["maxposition"] = positions
    discs[discNumber]["desiredposition"] = positions - discNumber
    # Account for when disc number is greater than positions
    # Use circular math to figure out the desired position
    if discs[discNumber]["desiredposition"] < 0:
        discs[discNumber]["desiredposition"] = discNumber
        while discs[discNumber]["desiredposition"] > 0:
            discs[discNumber]["desiredposition"] -= positions
        discs[discNumber]["desiredposition"] *= -1
    numDiscs += 1

def IncrementDiscPositions():
    for discNumber in discs:
        if discs[discNumber]["position"] + 1 is discs[discNumber]["maxposition"]:
            discs[discNumber]["position"] = 0
        else:
            discs[discNumber]["position"] += 1

timeFound = False
time = 0
while not timeFound:
    for discNumber in discs:
        if discs[discNumber]["position"] is not discs[discNumber]["desiredposition"]:
            IncrementDiscPositions()
            time += 1
            break
        elif discNumber is numDiscs:
            print("First time the button can be pressed to get a capsule: " + str(time))
            timeFound = True
            break
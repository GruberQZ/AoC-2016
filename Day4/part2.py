import re

file = open('input.txt','r')
pattern = r'(\d+)\[(\w+)\]'
regex = re.compile(pattern)
sum = 0
validRooms = []

for line in file:
    chars = ""
    id = ""
    verify = ""
    computedVerify = ""
    charCount = [0]*26
    segments = line.split('-')
    for i in range(len(segments)):
        if i == len(segments)-1:
            r = regex.search(segments[i].rstrip())
            id = r.group(1)
            verify = r.group(2)
            continue
        chars += segments[i]
    # Count the characters in each position
    for char in chars:
        charCount[ord(char)-97] += 1
    # Get the highest value in the array
    largestVal = 0
    for val in charCount:
        if val > largestVal:
            largestVal = val
    # Look for values at this value in order
    done = False
    for i in range(largestVal,0,-1):
        for j in range(0,26):
            if charCount[j] == i:
                computedVerify += chr(j+97)
                if len(computedVerify) == 5:
                    done = True
                    break
        if done == True:
            break

    if computedVerify == verify:
        validRooms.append(line)

pattern = r'(.*?)-(\d+)'
regex = re.compile(pattern)
for room in validRooms:
    r = regex.search(room)
    encrypted = r.group(1)
    rotations = int(r.group(2))
    for i in range(rotations):
        for j in range(len(encrypted)):
            if encrypted[j] == "-":
                continue
            elif encrypted[j] == "z":
                encrypted = encrypted[:j] + "a" + encrypted[j+1:]
            else:
                encrypted = encrypted[:j] + chr(ord(encrypted[j]) + 1) + encrypted[j+1:]
    if "north" in encrypted:
        print(encrypted + " is in sector " + str(rotations))

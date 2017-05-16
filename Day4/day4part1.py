import re

file = open('input.txt','r')
pattern = r'(\d+)\[(\w+)\]'
regex = re.compile(pattern)
sum = 0

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
        sum += int(id)

print(sum)
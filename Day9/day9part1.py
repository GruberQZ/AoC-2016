import re
import sys
file = open('input.txt','r')
regex = re.compile(r'(\d+)x(\d+)')
input = ""
output = ""

for line in file:
    input += line.rstrip()

consuming = True
repeating = False
patterning = False
repeatStr = ""
patternStr = ""
repetitions = 0
numChars = 0
for char in input:
    # Looking for the start of the next pattern
    if consuming:
        # Beginning of pattern
        if char == '(':
            consuming = False
            repeating = False
            patterning = True
            patternStr = ""
        else:
            output += char

    # Getting parts of the pattern string
    elif patterning:
        # End of pattern
        if char == ')':
            r = regex.match(patternStr)
            numChars = int(r.group(1))
            repetitions = int(r.group(2))
            repeatStr = ""
            consuming = False
            repeating = True
            patterning = False
        else:
            patternStr += char

    # Working out some repeating sequence
    elif repeating:
        repeatStr += char
        numChars -= 1
        if numChars == 0:
            for i in range(repetitions):
                output += repeatStr
            consuming = True
            repeating = False
            patterning = False

print(len(output))
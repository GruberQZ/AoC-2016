
file = open('input.txt','r')

chars = []
for i in range(8):
    chars.append([0] * 26)

for line in file:
    currentLine = line.rstrip()
    for i in range(len(currentLine)):
        chars[i][ord(currentLine[i])-97] += 1

message = ""
for i in range(8):
    # Find the position with the highest index
    largestVal = 0
    char = ""
    for j in range(26):
        if chars[i][j] > largestVal:
            largestVal = chars[i][j]
            char = chr(j+97)
    message += char

print(message)
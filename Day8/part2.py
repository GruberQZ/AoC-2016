import re
import sys
file = open('input.txt','r')
initrows = 6
initcols = 50

rectpattern = r'rect\s(\d+)x(\d+)'
rectregex = re.compile(rectpattern)
colpattern = r'rotate column x=(\d+)\sby\s(\d+)'
colregex = re.compile(colpattern)
rowpattern = r'rotate row y=(\d+)\sby\s(\d+)'
rowregex = re.compile(rowpattern)
count = 0

def printScreen():
    for row in screen:
        print(row)

screen = []
for i in range(initrows):
    screen.append([0]*initcols)

for line in file:
    line = line.rstrip()
    if count == 2:
        sys.exit()
    rectmatch = rectregex.match(line)
    if rectmatch != None:
        columns = int(rectmatch.group(1))
        rows = int(rectmatch.group(2))
        # Color in the upper left quadrant
        for i in range(rows):
            for j in range(columns):
                screen[i][j] = 1
        continue

    colmatch = colregex.match(line)
    if colmatch != None:
        column = int(colmatch.group(1))
        rotations = int(colmatch.group(2))
        for i in range(rotations):
            # Save the lowest value
            temp = screen[initrows-1][column]
            for j in range(initrows-2,-1,-1):
                screen[j+1][column] = screen[j][column]
            screen[0][column] = temp
        continue

    rowmatch = rowregex.match(line)
    if rowmatch != None:
        row = int(rowmatch.group(1))
        rotations = int(rowmatch.group(2))
        for i in range(rotations):
            temp = screen[row][initcols-1]
            for j in range(initcols-2,-1,-1):
                screen[row][j+1] = screen[row][j]
            screen[row][0] = temp
        continue
    count += 1

for row in screen:
    line = ""
    for col in row:
        if col == 1:
            line += "O"
        else:
            line += " "
    print(line)
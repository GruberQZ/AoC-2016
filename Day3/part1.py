import re

file = open('input.txt','r')
pattern = r'(\d+)\s+(\d+)\s+(\d+)'
regex = re.compile(pattern)
triangles = []
count = 0

for line in file:
    result = re.search(pattern,line)
    triangles.append([int(result.group(1)),int(result.group(2)),int(result.group(3))])

for entry in triangles:
    first = entry[0]
    second = entry[1]
    third = entry[2]
    if first + second > third:
        if first + third > second:
            if second + third > first:
                count = count + 1

print(count)
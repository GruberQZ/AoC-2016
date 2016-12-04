import re

file = open('input.txt','r')
pattern = r'(\d+)\s+(\d+)\s+(\d+)'
regex = re.compile(pattern)
triangles = []
count = 0
one = []
two = []
three = []

for line in file:
    result = re.search(pattern,line)
    one.append(int(result.group(1)))
    two.append(int(result.group(2)))
    three.append(int(result.group(3)))
    if len(one) == 3:
        triangles.append(one)
        triangles.append(two)
        triangles.append(three)
        one = []
        two = []
        three = []

for entry in triangles:
    first = entry[0]
    second = entry[1]
    third = entry[2]
    if first + second > third:
        if first + third > second:
            if second + third > first:
                count = count + 1

print(count)
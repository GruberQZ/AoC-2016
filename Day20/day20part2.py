import re

file = open('input.txt','r')
regex = re.compile(r'(\d+)-(\d+)')

ipranges = []

for line in file:
    line = line.rstrip()
    r = regex.match(line)
    range = {}
    range["low"] = int(r.group(1))
    range["high"] = int(r.group(2))
    ipranges.append(range)

testIP = 0
count = 0
while True:
    restartSearch = False
    # Check to see if the current IP falls within any of the ranges
    for range in ipranges:
        if testIP >= range["low"] and testIP <= range["high"]:
            testIP = range["high"] + 1
            ipranges.remove(range)
            restartSearch = True
            break
    if not restartSearch:
        testIP += 1
        count += 1
    if testIP > 4294967295:
        break

print("Number of non-blocked IP addresses: " + str(count))
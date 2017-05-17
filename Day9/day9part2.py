import re
import sys
file = open('input.txt','r')
regex = re.compile(r'\((\d+)x(\d+)\)')
input = ""
outlen = 0

for line in file:
    input += line.rstrip()

def decompress(input):
    chunklength = 0
    chars = input
    while len(chars):
        r = regex.match(chars)
        if r is not None:
            numChars = int(r.group(1))
            repetitions = int(r.group(2))
            matchlength = int(len(r.group(0)))
            chunklength += repetitions*decompress(chars[matchlength : matchlength + numChars])
            chars = chars[matchlength + numChars :]
        else:
            chars = chars[1:]
            chunklength += 1
    return chunklength

print("Decompressed length: " + str(decompress(input)))
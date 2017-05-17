puzzleinput = "10111011111001111"

def ReverseString(data):
    output = ""
    for i in range(len(data)-1,-1,-1):
        output += data[i]
    return output

def InvertBinaryString(data):
    output = ""
    for i in range(len(data)):
        if data[i] is "0":
            output += "1"
        else:
            output += "0"
    return output

# Create data from input as described in puzzle
def CreateData(data):
    # Starting data is "a"
    a = data
    # Make "b", a reversed copy of "a"
    b = ReverseString(a)
    # Invert "b"
    b = InvertBinaryString(b)
    # Resulting data is "a", single "0", then "b"
    return a + "0" + b

# Calculate the checksum of given data
def CalculateChecksum(data):
    input = data
    while len(input) % 2 is not 1:
        output = ""
        for i in range(0,len(input),2):
            if input[i] is input[i+1]:
                output += "1"
            else:
                output += "0"
        input = output
    return input

# Part 1
# Create data recursively until the length is at least 272, starting with puzzle input
data = puzzleinput
while len(data) < 272:
    data = CreateData(data)
# Trim data to size
data = data[0:272]
# Create a checksum of the data
print("Part 1 checksum: " + CalculateChecksum(data))
# Part 2
data = puzzleinput
while len(data) < 35651584:
    data = CreateData(data)
# Trim data to size
data = data[0:35651584]
# Create a checksum of the data
print("Part 2 checksum: " + CalculateChecksum(data))
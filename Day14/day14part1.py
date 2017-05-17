import hashlib

puzzleInput = "abc"
numKeys = 0
increasingIndex = 0

def LookForTriple(hash):
    for i in range(len(hash)-2):
        if hash[i] is hash[i+1] is hash[i+2]:
            return True, hash[i]
    return False, None

def LookForQuintuple(repeatingChar):
    hashesToTry = 1000
    indexToTest = increasingIndex + 1
    while hashesToTry:
        input = puzzleInput + str(indexToTest)
        hash = hashlib.md5(input.encode('utf-8')).hexdigest()
        for i in range(len(hash) - 4):
            if hash[i] is hash[i + 1] is hash[i + 2] is hash[i + 3] is hash[i + 4] is repeatingChar:
                return True
        hashesToTry -= 1
        indexToTest += 1
    return False

while True:
    input = puzzleInput + str(increasingIndex)
    result = hashlib.md5(input.encode('utf-8')).hexdigest()
    foundTriple, repeatingChar = LookForTriple(result)
    if foundTriple:
        valid = LookForQuintuple(repeatingChar)
        if valid:
            numKeys += 1
    if numKeys is 64:
        break
    increasingIndex += 1

print("The 64th one-time pad key is produced by index " + str(increasingIndex))

numKeys = 0
increasingIndex = 0

while True:
    input = puzzleInput + str(increasingIndex)
    result = hashlib.md5(input.encode('utf-8')).hexdigest()
    for i in range(2016):
        result = hashlib.md5(result.encode('utf-8')).hexdigest()
    foundTriple, repeatingChar = LookForTriple(result)
    if foundTriple:
        valid = LookForQuintuple(repeatingChar)
        if valid:
            numKeys += 1
    if numKeys is 64:
        break
    increasingIndex += 1

print("Using key stretching, the 64th one-time pad key is produced by index " + str(increasingIndex))
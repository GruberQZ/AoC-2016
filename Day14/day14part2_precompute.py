import hashlib

puzzleInput = "qzyelonm"
numKeys = 0
increasingIndex = 0

precomputedHashes = {}

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
        hash = precomputedHashes[input]
        for i in range(len(hash) - 4):
            if hash[i] is hash[i + 1] is hash[i + 2] is hash[i + 3] is hash[i + 4] is repeatingChar:
                return True
        hashesToTry -= 1
        indexToTest += 1
    return False

# Precompute hashes
for index in range(25000):
    input = puzzleInput + str(index)
    hash = hashlib.md5(input.encode('utf-8')).hexdigest()
    for i in range(2016):
        hash = hashlib.md5(hash.encode('utf-8')).hexdigest()
    precomputedHashes[input] = hash

while True:
    input = puzzleInput + str(increasingIndex)
    hash = precomputedHashes[input]
    foundTriple, repeatingChar = LookForTriple(hash)
    if foundTriple:
        valid = LookForQuintuple(repeatingChar)
        if valid:
            print("Found key with index " + str(increasingIndex))
            numKeys += 1
    if numKeys is 64:
        break
    increasingIndex += 1

print("Using key stretching, the 64th one-time pad key is produced by index " + str(increasingIndex))
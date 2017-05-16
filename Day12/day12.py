
instructions = [line.rstrip().split(" ") for line in open("input.txt", "r")]

reg = {
    "a": 0,
    "b": 0,
    "c": 1,
    "d": 0
}

def RepresentsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

i = 0
numInstructions = 0

while i in range(len(instructions)):
    inst = instructions[i]
    numInstructions += 1
    # Process instructions
    if inst[0] == "cpy":
        if RepresentsInt(inst[1]):
            reg[inst[2]] = int(inst[1])
        else:
            reg[inst[2]] = reg[inst[1]]
        i += 1
    elif inst[0] == "inc":
        reg[inst[1]] += 1
        i += 1
    elif inst[0] == "dec":
        reg[inst[1]] -= 1
        i += 1
    elif inst[0] == "jnz":
        if not RepresentsInt(inst[1]) and reg[inst[1]] is not 0:
            i += int(inst[2])
        elif RepresentsInt(inst[1]) and int(inst[1]) is not 0:
            i += int(inst[2])
        else:
            i += 1

print("Value of register 'a': " + str(reg["a"]))
print("Number of instructions executed: " + str(numInstructions))
instructions = [line.rstrip().split(" ") for line in open("input.txt", "r")]

# Set the value of a to 7 for part 1
# Set the value of a to 12 for part 2
reg = {
    "a": 7,
    "b": 0,
    "c": 0,
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
        if RepresentsInt(inst[2]):
            pass
        elif RepresentsInt(inst[1]):
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
            if RepresentsInt(inst[2]):
                i += int(inst[2])
            else:
                i += reg[inst[2]]
        elif RepresentsInt(inst[1]) and int(inst[1]) is not 0:
            if RepresentsInt(inst[2]):
                i += int(inst[2])
            else:
                i += reg[inst[2]]
        else:
            i += 1
    elif inst[0] == "tgl":
        if RepresentsInt(inst[1]):
            offset = int(inst[1])
        else:
            offset = reg[inst[1]]
        # Make sure offset is not out of bounds
        if i + offset < 0 or i + offset >= len(instructions):
            i += 1
            continue
        # One argument instructions
        if len( instructions[ i + offset ] ) == 2:
            if instructions[ i + offset ][ 0 ] == "inc":
                instructions[i + offset][ 0 ] = "dec"
            else:
                instructions[i + offset][ 0 ] = "inc"
            i += 1
        # Two argument instructions
        elif len( instructions[ i + offset ] ) == 3:
            if instructions[ i + offset ][ 0 ] == "jnz":
                instructions[i + offset][ 0 ] = "cpy"
            else:
                instructions[i + offset][ 0 ] = "jnz"
            i += 1

print("Value of register 'a': " + str(reg["a"]))
print("Number of instructions executed: " + str(numInstructions))
import sys
instructions = [line.rstrip().split(" ") for line in open("input.txt", "r")]

def Run(valueOfA):
    # print("Output for initial a value of", str(valueOfA))
    reg = {
        "a": valueOfA,
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
    #numInstructions = 0

    prevOut = 1
    outCount = 0

    while i in range(len(instructions)):
        inst = instructions[i]
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
        elif inst[0] == "out":
            outCount += 1
            # sys.stdout.write(str(reg[inst[1]]))
            if reg[inst[1]] != 0 and reg[inst[1]] != 1:
                return False
            if reg[inst[1]] == prevOut:
                return False
            if outCount == 200:
                return True
            prevOut = reg[inst[1]]
            i += 1

    # If while loop is broken, clock signal is not infinite, fails test
    return False

startingValue = 1
while not Run(startingValue):
    startingValue += 1
    # if startingValue % 100 == 0:
    #     print(startingValue)

print("Starting value of a for infinite clock signal:",str(startingValue))
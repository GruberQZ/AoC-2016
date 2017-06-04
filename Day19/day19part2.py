def isPower(num, base):
    if num == base:
        return True
    if base == 1:
        return False
    temp = base
    while temp <= num:
        if temp == num:
            return True
        else:
            temp *= base
    return False

def Solve(puzzleinput):
    if puzzleinput <= 0:
        return None
    elif puzzleinput == 1 or puzzleinput == 2:
        return 1
    elif isPower(puzzleinput, 3):
        return puzzleinput
    else:
        # Figure out what powers of 3 surround the puzzle input
        power = 0
        temp = 1
        while temp < puzzleinput:
            temp *= 3
            power += 1
        upperPower = temp
        lowerPower = 3 ** (power - 1)
        # Figure out seat number based on position between upper and lower powers
        halfway = upperPower - int((upperPower - lowerPower) / 2)
        if puzzleinput <= halfway:
            return puzzleinput - lowerPower
        else:
            return (halfway - lowerPower) + ((puzzleinput - halfway) * 2)

puzzleinput = 3017957
solution = Solve(puzzleinput)
if solution is not None:
    print("Elf with all of the presents:", str(solution))
else:
    print("Invalid number of elves:", str(puzzleinput))
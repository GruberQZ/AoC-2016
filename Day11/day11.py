import sys
import itertools
import copy

def printFloors(floors):
    for floor in reversed(range(len(floors))):
    #for floor in range(3,-1,-1):
        sys.stdout.write("F" + str(floor) + "  ")
        for pos in floors[floor]:
            if pos == None:
                sys.stdout.write(".  ")
            elif pos == "E":
                sys.stdout.write("E  ")
            else:
                sys.stdout.write(pos + " ")
        sys.stdout.write("\n")

def isValidLayout(floors):
    # Validate floors one at a time
    # If any floors are not valid, return false.
    # Otherwise, return true
    for floor in range(len(floors)):
        if not validateFloor(floors[floor]):
            return False
    return True

def validateFloor(floor):
    # Find all of the exposed
    exposedMC = False
    existsGen = False
    for i in range(len(floor)):
        if i % 2 == 0:
            continue
        if floor[ i ] == None and floor[ i + 1 ] != None:
            exposedMC = True
        elif floor[ i ] != None:
            existsGen = True
    # If there are exposed microchips and unsafe generators, return False
    if exposedMC and existsGen:
        return False
    else:
        return True

def getListOfPossibleOutcomes(floors):
    elevatorPosition = getElevatorPosition(floors)
    floor = floors[elevatorPosition]
    occupiedPositions = []
    for i in range(1,len(floor),1):
        if floor[i] != None:
            occupiedPositions.append(i)
    lengthTwoCombinations = itertools.combinations(occupiedPositions, 2)
    possibleLayouts = []
    # Equipment moving up
    if elevatorPosition < 3:
        # Single equipment move
        for i in occupiedPositions:
            # Copy original floor layout
            tempFloors = copy.deepcopy(floors)
            # Move item up one floor
            tempFloors[elevatorPosition + 1][ i ] = tempFloors[ elevatorPosition ][ i ]
            # Erase item from original position
            tempFloors[ elevatorPosition ][ i ] = None
            # Move elevator
            tempFloors[elevatorPosition + 1][0] = tempFloors[elevatorPosition][0]
            tempFloors[elevatorPosition][0] = None
            # Add layout to possible layouts
            possibleLayouts.append(tempFloors)
        # Double equipment move
        for firstPos,secondPos in lengthTwoCombinations:
            # Copy original floor layout
            tempFloors = copy.deepcopy(floors)
            # Move first item
            # Move item up one floor
            tempFloors[elevatorPosition + 1][firstPos] = tempFloors[elevatorPosition][firstPos]
            # Erase item from original position
            tempFloors[elevatorPosition][firstPos] = None
            # Move second item
            # Move item up one floor
            tempFloors[elevatorPosition + 1][secondPos] = tempFloors[elevatorPosition][secondPos]
            # Erase item from original position
            tempFloors[elevatorPosition][secondPos] = None
            # Move elevator
            tempFloors[elevatorPosition + 1][0] = tempFloors[elevatorPosition][0]
            tempFloors[elevatorPosition][0] = None
            # Add layout to possible layouts
            possibleLayouts.append(tempFloors)
    # Equipment moving down
    if elevatorPosition > 0:
        # Single equipment move
        for i in occupiedPositions:
            # Copy original floor layout
            tempFloors = copy.deepcopy(floors)
            # Move item up one floor
            tempFloors[elevatorPosition - 1][i] = tempFloors[elevatorPosition][i]
            # Erase item from original position
            tempFloors[elevatorPosition][i] = None
            # Move elevator
            tempFloors[elevatorPosition - 1][0] = tempFloors[elevatorPosition][0]
            tempFloors[elevatorPosition][0] = None
            # Add layout to possible layouts
            possibleLayouts.append(tempFloors)
        # Double equipment move
        for firstPos, secondPos in lengthTwoCombinations:
            # Copy original floor layout
            tempFloors = copy.deepcopy(floors)
            # Move first item
            # Move item up one floor
            tempFloors[elevatorPosition - 1][firstPos] = tempFloors[elevatorPosition][firstPos]
            # Erase item from original position
            tempFloors[elevatorPosition][firstPos] = None
            # Move second item
            # Move item up one floor
            tempFloors[elevatorPosition - 1][secondPos] = tempFloors[elevatorPosition][secondPos]
            # Erase item from original position
            tempFloors[elevatorPosition][secondPos] = None
            # Move elevator
            tempFloors[elevatorPosition - 1][0] = tempFloors[elevatorPosition][0]
            tempFloors[elevatorPosition][0] = None
            # Add layout to possible layouts
            possibleLayouts.append(tempFloors)
    # Return list of possible layouts
    return possibleLayouts

def getElevatorPosition(floors):
    for i in range(len(floors)):
        if floors[i][0] != None:
            return i
    return False

def isComplete(floors):
    # If any position in the 3rd floor is None, not done
    return not None in floors[3]

def Solve(floors):
    # List of valid paths
    layouts = []
    # Add starting path to list of valid paths
    layouts.append(floors)
    steps = 0
    while True:
        newLayouts = []
        steps += 1
        print(str(len(layouts)),"layouts about to try adding step number",str(steps))
        while layouts:
            # Take the first path from the list of paths
            currentLayout = layouts.pop(0)
            # Build a list of all possible moves from the current path
            possibleLayouts = getListOfPossibleOutcomes(currentLayout)
            # Iterate through all possible paths
            while possibleLayouts:
                possibleLayout = possibleLayouts.pop(0)
                # If layout has exit condition, return number of steps taken
                if isComplete(possibleLayout):
                    printFloors(possibleLayout)
                    return steps
                # If layout is valid, add it to newLayouts
                if isValidLayout(possibleLayout):
                    newLayouts.append(possibleLayout)
        # Copy new layouts to layouts
        layouts = copy.deepcopy(newLayouts)

# Initialize floors and equipment for example
floorsEx = [[None] * 5, [None] * 5, [None] * 5, [None] * 5]
floorsEx[0][0] = "E"
floorsEx[1][1] = "HG"
floorsEx[0][2] = "HM"
floorsEx[2][3] = "LG"
floorsEx[0][4] = "LM"

# Initialize floors and equipment for part 1
floors1 = [[None] * 11, [None] * 11, [None] * 11, [None] * 11]
floors1[0][0] = "E"
floors1[0][1] = "SG"
floors1[0][2] = "SM"
floors1[0][3] = "PG"
floors1[0][4] = "PM"
floors1[1][5] = "TG"
floors1[2][6] = "TM"
floors1[1][7] = "RG"
floors1[1][8] = "RM"
floors1[1][9] = "CG"
floors1[1][10] = "CM"

print("Minimum number of steps for example:",str(Solve(floorsEx)))

print("Minimum number of steps for part 1:",str(Solve(floors1)))
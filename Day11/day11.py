import itertools


def validatefloor(floorwithelevator):
    # Remove elevator from floor
    floor = floorwithelevator[1:]
    # Find all of the exposed
    exposedmc = False
    existsgen = False
    for i in range(0, len(floor), 2):
        # Microchip present but corresponding generator is not
        if floor[i: i + 2] == "01":
            exposedmc = True
        # Generator for this pair is present, regardless of microchip
        elif floor[i] == "1":
            existsgen = True
        # If there are exposed microchips and unsafe generators, return False
        if exposedmc and existsgen:
            return False
    return True


def computevalidfloors(floorlength):
    # Generate all combinations of 0s and 1s of length floorlength
    validfloors = set()
    products = itertools.product(("0", "1"), repeat=floorlength)
    for prod in products:
        floor = "".join(prod)
        if validatefloor(floor):
            validfloors.add(int(floor, 2))
    return validfloors


def getfloor(state, floornumber, floorlength):
    floors = bin(state)[2:].zfill(4 * floorlength)
    if floornumber == 3:
        return floors[0 : floorlength]
    elif floornumber == 2:
        return floors[floorlength : floorlength * 2]
    elif floornumber == 1:
        return floors[floorlength * 2 : floorlength * 3]
    elif floornumber == 0:
        return floors[floorlength * 3 : floorlength * 4]
    else:
        return None


def getelevatorpositionandfloor(state, floorlength):
    floors = bin(state)[2:].zfill(4 * floorlength)
    if floors[0] == "1":
        return 3, floors[0 : floorlength]
    elif floors[floorlength] == "1":
        return 2, floors[floorlength : floorlength * 2]
    elif floors[floorlength * 2] == "1":
        return 1, floors[floorlength * 2 : floorlength * 3]
    elif floors[floorlength * 3] == "1":
        return 0, floors[floorlength * 3 : floorlength * 4]
    else:
        return None, None


def findneighborstates(state, statedistance, validfloors, statestovisit, floorlength):
    if state == 19809:
        print("Found it!")
    elevatorposition, floor = getelevatorpositionandfloor(state, floorlength)
    currentdistance = statedistance[state]
    revFloor = floor[::-1]
    occupiedPositions = []
    for i in range(0,len(revFloor)-1,1):
        if revFloor[i] == "1":
            occupiedPositions.append(i)
    doublemoves = itertools.combinations(occupiedPositions, 2)
    newstates = []
    # Precompute current elevator mask because it will not change
    currentelevatormask = 1 << ((floorlength - 1) + (elevatorposition * floorlength))
    # Find all possible single moves
    for i in occupiedPositions:
        mask = 1 << i
        currentfloormask = mask << (elevatorposition * floorlength)
        # Single move up
        if elevatorposition < 3:
            higherfloormask = currentfloormask << floorlength
            higherelevatormask = 1 << ((floorlength - 1) + ((elevatorposition + 1) * floorlength))
            potentialstate = state + higherfloormask + higherelevatormask - currentfloormask - currentelevatormask
            if potentialstate < 0:
                print("Found it!")
            newstates.append(potentialstate)
        # Single move down
        if elevatorposition > 0:
            lowerfloormask = currentfloormask >> floorlength
            lowerelevatormask = 1 << ((floorlength - 1) + ((elevatorposition - 1) * floorlength))
            potentialstate = state + lowerfloormask + lowerelevatormask - currentfloormask - currentelevatormask
            if potentialstate < 0:
                print("Found it!")
            newstates.append(potentialstate)
    # Find all possible double moves
    for i, j in doublemoves:
        mask = 1 << i
        mask += 1 << j
        currentfloormask = mask << (elevatorposition * floorlength)
        # Single move up
        if elevatorposition < 3:
            higherfloormask = currentfloormask << floorlength
            higherelevatormask = 1 << ((floorlength - 1) + ((elevatorposition + 1) * floorlength))
            potentialstate = state + higherfloormask + higherelevatormask - currentfloormask - currentelevatormask
            if potentialstate < 0:
                print("Found it!")
            newstates.append(potentialstate)
        # Single move down
        if elevatorposition > 0:
            lowerfloormask = currentfloormask >> floorlength
            lowerelevatormask = 1 << ((floorlength - 1) + ((elevatorposition - 1) * floorlength))
            potentialstate = state  + lowerfloormask + lowerelevatormask - currentfloormask - currentelevatormask
            if potentialstate < 0:
                print("Found it!")
            newstates.append(potentialstate)
    # Check through list of new states
    for newstate in newstates:
        # If new state in state distance already, it has already been validated
        # Check to see if distance can be updated
        if newstate in statedistance:
            statestovisit.append(newstate)
            if statedistance[newstate] > currentdistance + 1:
                statedistance[newstate] = currentdistance + 1
        # Validate state before adding it to statedistance
        else:
            if int(getfloor(newstate, 3, floorlength), 2) in validfloors and \
                    int(getfloor(newstate, 2, floorlength), 2) in validfloors and \
                    int(getfloor(newstate, 1, floorlength), 2) in validfloors and \
                    int(getfloor(newstate, 0, floorlength), 2) in validfloors:
                statestovisit.append(newstate)
                statedistance[newstate] = currentdistance + 1
    # Return current distance for progress tracking
    return currentdistance

# Find the unvisited state with the smallest distance
def findnextcurrentstate(statestovisit, visitedstates):
    while statestovisit:
        nextstate = statestovisit.pop(0)
        if nextstate not in visitedstates:
            return nextstate
    return None

    # mindist = 50000
    # savedstate = None
    # for state in statedistance:
    #     if state not in visitedstates:
    #         if statedistance[state] < mindist:
    #             mindist = statedistance[state]
    #             savedstate = state
    # return savedstate

def solve(initialstate, floorlength):
    largestdistance = 0
    # Compute final state
    finalstate = int("1" * floorlength + "0" * floorlength * 3, 2)
    # Compute all of the valid floors and add them to a map
    validfloors = computevalidfloors(floorlength)
    # Dict for keeping track of distances
    statedistance = {}
    # Set for tracking visited nodes
    visitedstates = set()
    # Queue of states to visit
    statestovisit = []
    # Set the starting node and set its distance to 0
    currentstate = initialstate
    statedistance[currentstate] = 0
    # Iterate until all nodes have been visited
    while currentstate != None:
        # Find neighbor states for the current state
        workingdistance = findneighborstates(currentstate, statedistance, validfloors, statestovisit, floorlength)
        # Print out if new working distance
        if workingdistance > largestdistance:
            largestdistance = workingdistance
            print(workingdistance)
        # Mark current state visited
        visitedstates.add(currentstate)
        # Look for the next state to visit
        currentstate = findnextcurrentstate(statestovisit, visitedstates)
    # Return distance of final state
    return statedistance[finalstate]

examplefloor = int("00000000100100010101", 2)
examplefloorlength = 5
part1floor = int("00000000000000000100000000010111111111000000", 2)
part1floorlength = 11
part2floor = int("000000000000000000000100000000000001011110000111110000001111", 2)
part2floorlength = 15
# print("Minimum steps for example:", str(solve(examplefloor, examplefloorlength)))
print("Minimum steps for part 1:", str(solve(part1floor, part1floorlength)))
print("Minimum steps for part 2:", str(solve(part2floor, part2floorlength)))
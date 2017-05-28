from itertools import permutations

# Get the puzzle input
gridlines = []
for line in open("input.txt","r"):
    gridlines.append(line.rstrip())

# Create a list of valid locations
# Mark the interesting locations (the ones marked with numbers)
nodeDistanceMaster = {}
notableLocations = {}
for i in range(len(gridlines)):
    line = gridlines[i]
    for j in range(len(line)):
        char = line[j]
        if char == "#":
            continue
        nodeDistanceMaster[(i,j)] = 50000
        if char != ".":
            notableLocations[int(char)] = (i,j)

def Djikstra(startingNode):
    # Make a copy of the floor layout
    nodeDistance = dict(nodeDistanceMaster)
    # Start with the starting node and set its distance to 0
    currentNode = startingNode
    nodeDistance[currentNode] = 0
    # Fill the list of unvisited nodes
    unvisitedNodes = []
    for node in nodeDistance:
        unvisitedNodes.append(node)

    # Define function to find the unvisited node with the smallest distance
    def NextCurrentNode():
        mindist = 50000
        savednode = (-1, -1)
        for node in nodeDistance:
            if node in unvisitedNodes:
                if nodeDistance[node] < mindist:
                    mindist = nodeDistance[node]
                    savednode = node
        return savednode

    # Iterate until all nodes have been visited
    while unvisitedNodes:
        # Get the current node's distance from (1,1)
        currentDistance = nodeDistance[currentNode]
        # Get the coordinates of the current node
        curx, cury = currentNode[0], currentNode[1]
        # Consider all of the neighbors of the current node if they are valid
        if (curx + 1, cury) in nodeDistance and nodeDistance[(curx + 1, cury)] > currentDistance + 1:
            nodeDistance[(curx + 1, cury)] = currentDistance + 1
        if (curx - 1, cury) in nodeDistance and nodeDistance[(curx - 1, cury)] > currentDistance + 1:
            nodeDistance[(curx - 1, cury)] = currentDistance + 1
        if (curx, cury + 1) in nodeDistance and nodeDistance[(curx, cury + 1)] > currentDistance + 1:
            nodeDistance[(curx, cury + 1)] = currentDistance + 1
        if (curx, cury - 1) in nodeDistance and nodeDistance[(curx, cury - 1)] > currentDistance + 1:
            nodeDistance[(curx, cury - 1)] = currentDistance + 1
        # Mark current node visited by removing it from unvisited nodes
        unvisitedNodes.remove(currentNode)
        # Try to get the next current node
        currentNode = NextCurrentNode()
        # If currentnode is (-1,-1), algorithm is finished
        if currentNode == (-1, -1):
            break

    # Return the distances to locations 0-7 from the starting node
    return nodeDistance[ notableLocations[ 0 ] ], nodeDistance[ notableLocations[ 1 ] ], nodeDistance[ notableLocations[ 2 ] ], nodeDistance[ notableLocations[ 3 ] ],nodeDistance[ notableLocations[ 4 ] ],nodeDistance[ notableLocations[ 5 ] ],nodeDistance[ notableLocations[ 6 ] ],nodeDistance[ notableLocations[ 7 ] ]

# Perform Djikstra's algorithm for each notable location
distanceFrom = {}
for marker in notableLocations:
    coords = notableLocations[marker]
    distanceFrom[ marker ] = {}
    distanceFrom[ marker ][ 0 ], distanceFrom[ marker ][ 1 ], distanceFrom[ marker ][ 2 ], distanceFrom[ marker ][ 3 ], distanceFrom[ marker ][ 4 ], distanceFrom[ marker ][ 5 ], distanceFrom[ marker ][ 6 ], distanceFrom[ marker ][ 7 ] = Djikstra(coords)
    # for entry in distanceFrom[marker]:
    #     print("Distance from", str(marker), "to", str(entry), "is", str(distanceFrom[marker][entry]))

locations = [1,2,3,4,5,6,7]
minDistance = 1000000
for order in permutations(locations):
    listOrder = [0] + list(order)
    distance = 0
    for i in range(len(listOrder)-1):
        distance += distanceFrom[ listOrder[ i ] ][ listOrder[ i + 1 ] ]
    if distance < minDistance:
        minDistance = distance

print("Minimum distance without returning to 0: " + str(minDistance))

minDistance = 1000000
for order in permutations(locations):
    listOrder = [0] + list(order) + [0]
    distance = 0
    for i in range(len(listOrder)-1):
        distance += distanceFrom[ listOrder[ i ] ][ listOrder[ i + 1 ] ]
    if distance < minDistance:
        minDistance = distance

print("Minimum distance including returning to 0: " + str(minDistance))
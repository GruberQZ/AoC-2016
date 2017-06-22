import re
import sys

# Build the grid of data nodes
nodes = {}
nodedistance = {}
nodeXMin = 0
nodeXMax = 0
nodeYMin = 0
nodeYMax = 0
regex = re.compile(r"\/dev\/grid\/node-x(\d+)-y(\d+)\s+(\d+)T\s+(\d+)T\s+(\d+)T\s+(\d+)%")

for line in open("input.txt", "r"):
    # Remove newline character
    nodeInfo = line.rstrip()
    # Match regex to line in file
    r = regex.match(nodeInfo)
    # Extract node info from line
    nodeX = int(r.group(1))
    nodeY = int(r.group(2))
    nodeUsed = int(r.group(4))
    nodeAvail = int(r.group(5))
    # Check for xmax and ymax
    if nodeX > nodeXMax:
        nodeXMax = nodeX
    if nodeY > nodeYMax:
        nodeYMax = nodeY
    # Build node with coordinates as dictionary key
    key = (nodeX, nodeY)
    # If used space on node is greater than 200, mark as blocked
    if nodeUsed >= 200:
        nodes[key] = "#"
    else:
        nodes[key] = "."
        if nodeUsed == 0:
            startingLocation = key
        # Add node to unvisited nodes
        nodedistance[key] = 50000

# Fill the list of unvisited nodes
unvisitednodes = []
for node in nodedistance:
    unvisitednodes.append(node)

# Find the unvisited node with the smallest distance
def NextCurrentNode():
    mindist = 50000
    savednode = (-1,-1)
    for node in nodedistance:
        if node in unvisitednodes:
            if nodedistance[node] < mindist:
                mindist = nodedistance[node]
                savednode = node
    return savednode

# Mark node as visited
def MarkNodeVisited(node):
    unvisitednodes.remove(node)

# Start at the empty node and set its distance to 0
currentnode = startingLocation
nodedistance[currentnode] = 0

# Iterate until all nodes have been visited
while unvisitednodes:
    # Get the current node's distance from (1,1)
    currentdistance = nodedistance[currentnode]
    # Get the coordinates of the current node
    curx, cury = currentnode[0], currentnode[1]
    # Consider all of the neighbors of the current node if they are valid
    if (curx + 1, cury) in nodedistance and nodedistance[(curx + 1, cury)] > currentdistance + 1:
        nodedistance[(curx + 1, cury)] = currentdistance + 1
    if (curx - 1, cury) in nodedistance and nodedistance[(curx - 1, cury)] > currentdistance + 1:
        nodedistance[(curx - 1, cury)] = currentdistance + 1
    if (curx, cury + 1) in nodedistance and nodedistance[(curx, cury + 1)] > currentdistance + 1:
        nodedistance[(curx, cury + 1)] = currentdistance + 1
    if (curx, cury - 1) in nodedistance and nodedistance[(curx, cury - 1)] > currentdistance + 1:
        nodedistance[(curx, cury - 1)] = currentdistance + 1
    # Mark current node visited
    MarkNodeVisited(currentnode)
    # Try to get the next current node
    currentnode = NextCurrentNode()
    # If currentnode is (-1,-1), algorithm is finished
    if currentnode == (-1,-1):
        break

# Set goal node label
nodes[(nodeXMax, 0)] = "G"

# Set starting location of empty node and label it
currLoc = [nodeXMax - 1, 0]
nodes[tuple(currLoc)] = "_"

# Look in nodedistance to find the shortest distance to one node left of the goal data's starting node
distance = nodedistance[tuple(currLoc)]

def printGrid(nodes, xLength, yLength):
    for i in range(yLength):
        for j in range(xLength):
            sys.stdout.write(nodes[(j,i)])
        print()

# Perform the first swap so the empty node is in the top right corner
tupCurrLoc = tuple(currLoc)
tupNewLoc = (currLoc[0] + 1, currLoc[1])
temp = nodes[tupNewLoc]
nodes[tupNewLoc] = nodes[tupCurrLoc]
nodes[tupCurrLoc] = temp
currLoc = list(tupNewLoc)
distance += 1

def moveEmptyNode(current, new):
    temp = nodes[new]
    nodes[new] = nodes[current]
    nodes[current] = temp

# Rotate the empty space around the goal data repeatedly to move it left
# Keep moving it left until it reaches position (0,0)
while nodes[(0, 0)] != "G":
    # Move empty node down
    newLoc = [currLoc[0], currLoc[1] + 1]
    moveEmptyNode(tuple(currLoc), tuple(newLoc))
    currLoc = newLoc
    # Move empty node left twice
    newLoc = [currLoc[0] - 2, currLoc[1]]
    moveEmptyNode(tuple(currLoc), tuple(newLoc))
    currLoc = newLoc
    # Move empty node up
    newLoc = [currLoc[0], currLoc[1] - 1]
    moveEmptyNode(tuple(currLoc), tuple(newLoc))
    currLoc = newLoc
    # Move empty node right
    newLoc = [currLoc[0] + 1, currLoc[1]]
    moveEmptyNode(tuple(currLoc), tuple(newLoc))
    currLoc = newLoc
    # Increment distance by 5
    distance += 5

print("Fewest number of steps required:", str(distance))
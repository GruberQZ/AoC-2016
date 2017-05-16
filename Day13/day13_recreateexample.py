# Create list of locations (nodes) (0,0) thru (99,99)
# Calculate whether or not each node is legal (open) or not (wall)
# Legal nodes are marked as unvisited
nodedistance = {}
for x in range(10):
    for y in range(10):
        value = x*x + 3*x + 2*x*y + y + y*y
        binvalue = bin(value + 10)
        count = 0
        for index, char in enumerate(binvalue):
            if char == "1":
                count += 1
        if count % 2 == 0:
            nodedistance[(x,y)] = 50000

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

# Start with node (1,1) and set its distance to 0
currentnode = (1,1)
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

print("Minimum distance to (7,4): " + str(nodedistance[(7,4)]))
import re

nodes = {}
nodeXMin = 0
nodeXMax = 0
nodeYMin = 0
nodeYMax = 0
regex = re.compile(r"\/dev\/grid\/node-x(\d+)-y(\d+)\s+(\d+)T\s+(\d+)T\s+(\d+)T\s+(\d+)%")

for line in open("input.txt","r"):
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
    key = (nodeX,nodeY)
    nodes[key] = {}
    nodes[key]["used"] = nodeUsed
    nodes[key]["avail"] = nodeAvail

def SearchForViablePairs(nodeA):
    count = 0
    for x in range(nodeXMin, nodeXMax + 1, 1):
        for y in range(nodeYMin, nodeYMax + 1, 1):
            nodeB = (x,y)
            # Nodes A and B cannot be the same
            if nodeB == nodeA:
                continue
            # The data on node A fits on node B
            if nodes[ nodeA ][ "used" ] <= nodes[ nodeB ][ "avail" ]:
                count += 1
    return count

# Iterate through all nodes looking for viable pairs
# Check each node against every other node (except itself)
count = 0
for i in range(nodeXMin, nodeXMax + 1, 1):
    for j in range(nodeYMin, nodeYMax + 1 , 1):
        nodeA = (i, j)
        # Node A cannot be empty
        if nodes[ nodeA ][ "used" ] == 0:
            continue
        else:
            count += SearchForViablePairs( nodeA )

print("Number of viable pairs: " + str(count))
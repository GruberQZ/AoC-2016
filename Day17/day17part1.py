import hashlib

puzzleInput = "udskfozm"

# Start with an empty list of paths
paths = []

# Find current position based on path taken
def GetCurrentPosition(path):
    position = [0,0]
    for index, char in enumerate(path):
        if char is "U":
            position[1] -= 1
        elif char is "D":
            position[1] += 1
        elif char is "L":
            position[0] -= 1
        elif char is "R":
            position[0] += 1
    return position

# Get the open doors for a given path
def FindOpenDoors(path):
    input = puzzleInput + path
    hash = hashlib.md5(input.encode('utf-8')).hexdigest()
    upOpen, downOpen, leftOpen, rightOpen = False, False, False, False
    openChars = ["b","c","d","e","f"]
    if hash[0] in openChars:
        upOpen = True
    if hash[1] in openChars:
        downOpen = True
    if hash[2] in openChars:
        leftOpen = True
    if hash[3] in openChars:
        rightOpen = True
    return upOpen, downOpen, leftOpen, rightOpen

# Grid
   # 0 1 2 3
   # ########
#0 # S| | | #
   # -#-#-#-#
#1 #  | | | #
   # -#-#-#-#
#2 #  | | | #
   # -#-#-#-#
#3 #  | | |
   # ###### V

# Main loop
# Add an empty path to start with
paths.append("")
VaultReached = False
while not VaultReached and paths:
    temppaths = []
    for path in paths:
        # Figure out the current position
        position = GetCurrentPosition(path)
        if position[0] is 3 and position[1] is 3:
            print("Valid path found: " + path)
            VaultReached = True
            break
        # Find the open doors for the current position
        upOpen, downOpen, leftOpen, rightOpen = FindOpenDoors(path)
        # Rule out certain doors based on position in grid
        if position[0] is 0:
            leftOpen = False
        if position[0] is 3:
            rightOpen = False
        if position[1] is 0:
            upOpen = False
        if position[1] is 3:
            downOpen = False
        # Create a new potential path for any open doors
        if upOpen:
            temppaths.append(path + "U")
        if downOpen:
            temppaths.append(path + "D")
        if rightOpen:
            temppaths.append(path + "R")
        if leftOpen:
            temppaths.append(path + "L")
    paths = temppaths.copy()

if not paths and not temppaths:
    print("No valid paths found")
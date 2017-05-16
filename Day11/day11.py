import sys

# Initialize floors
floors = [[None] * 11, [None] * 11, [None] * 11, [None] * 11]
# Initialize equipment
floors[0][0] = "E"
floors[0][1] = "SG"
floors[0][2] = "SM"
floors[0][3] = "PG"
floors[0][4] = "PM"
floors[1][5] = "TG"
floors[2][6] = "TM"
floors[1][7] = "RG"
floors[1][8] = "RM"
floors[1][9] = "CG"
floors[1][10] = "CM"

def printFloors():
    for floor in range(3,-1,-1):
        sys.stdout.write("F" + str(floor) + "  ")
        for pos in floors[floor]:
            if pos == None:
                sys.stdout.write(".  ")
            elif pos == "E":
                sys.stdout.write("E  ")
            else:
                sys.stdout.write(pos + " ")
        sys.stdout.write("\n")

printFloors()
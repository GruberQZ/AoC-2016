
puzzleinput = ".^^^^^.^^.^^^.^...^..^^.^.^..^^^^^^^^^^..^...^^.^..^^^^..^^^^...^.^.^^^^^^^^....^..^^^^^^.^^^.^^^.^^"

tilesPerRow = len(puzzleinput)

# List of rows where first row is puzzle input
rows = [list(puzzleinput)]

# Number of rows to generate
numRows = 400000

# ^ represents a trap, . represents a safe tile

for prevRow in range(numRows-1):
    nextRow = [None] * tilesPerRow
    for i in range(tilesPerRow):
        # Imaginary "safe" tiles unless replaced
        left = "."
        right = "."
        if i is not 0:
            left = rows[prevRow][i - 1]
        if i is not tilesPerRow-1:
            right = rows[prevRow][i + 1]
        center = rows[prevRow][i]
        # The next tile is a trap if it meets one of the following conditions
        if left is "^" and center is "^" and right is ".":
            nextRow[i] = "^"
        elif left is "." and center is "^" and right is "^":
            nextRow[i] = "^"
        elif left is "^" and center is "." and right is ".":
            nextRow[i] = "^"
        elif left is "." and center is "." and right is "^":
            nextRow[i] = "^"
        else:
            nextRow[i] = "."
    rows.append(nextRow)

safetiles = 0
for row in rows:
    for tile in row:
        if tile is ".":
            safetiles += 1

print("There are " + str(safetiles) + " safe tiles")
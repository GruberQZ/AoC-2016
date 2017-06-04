from itertools import cycle

puzzleinput = 3017957

elves = []
indices = []

# Build a list of all of the elves
for i in range(1,puzzleinput+1,1):
    elves.append(i)
    indices.append(i-1)

# Create queue of elves and initialize index
elfQueue = cycle(indices)
elfIndex = next(elfQueue)
elvesRemoved = 0

while True:
    if elves[elfIndex] is None:
        # Skip this elf
        elfIndex = next(elfQueue)
    else:
        # Find the next non-None position
        elfIndex = next(elfQueue)
        while elves[elfIndex] is None:
            elfIndex = next(elfQueue)
        # Remove the elf at this index
        elves[elfIndex] = None
        elvesRemoved += 1
        elfIndex = next(elfQueue)
        if elvesRemoved == puzzleinput - 1:
            break

# Find the only elf that remains
for elf in elves:
    if elf is not None:
        print("Elf with all of the presents: " + str(elf))
        break

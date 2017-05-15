
file = open("input.txt")

# structs contains all of the places chips can be passed
bots = {}
outputs = {}
instructions = {}

def checkBot(botNumber):
    if botNumber in bots and len(bots[botNumber]["chips"]) == 2:
        # Check for puzzle solution
        if bots[botNumber]["chips"] == [17, 61]:
            print("Part 1 solution: " + str(botNumber))
        # Can only move chips if there are instructions provided
        if botNumber in instructions:
            # Give chips to other bots
            # Move lower chip
            chipValue = bots[botNumber]["chips"][0]
            if instructions[botNumber]["lowStruct"] == "bot":
                giveChip("bot", instructions[botNumber]["lowNumber"], chipValue)
                checkBot(instructions[botNumber]["lowNumber"])
            else:
                giveChip("output", instructions[botNumber]["lowNumber"], chipValue)
            # Move higher chip
            chipValue = bots[botNumber]["chips"][1]
            if instructions[botNumber]["highStruct"] == "bot":
                giveChip("bot", instructions[botNumber]["highNumber"], chipValue)
                checkBot(instructions[botNumber]["highNumber"])
            else:
                giveChip("output", instructions[botNumber]["lowNumber"], chipValue)
            # Clear this bot's list of chips
            bots[botNumber]["chips"] = []

def giveChip(structure, number, chipValue):
    if structure == "bot":
        # Give microchip to bot
        if number in bots:
            bots[number]["chips"].append(chipValue)
            bots[number]["chips"].sort()
        else:
            bots[number] = {}
            bots[number]["chips"] = [chipValue]
    else:
        # Put microchip in output
        if number in outputs:
            outputs[number]["chips"].append(chipValue)
            outputs[number]["chips"].sort()
        else:
            outputs[number] = {}
            outputs[number]["chips"] = [chipValue]

# Main loop
for line in file:
    line = line.rstrip()
    if line.startswith("v"):
        # Gives a microchip to a bot
        # Extract info from line
        words = line.split(" ")
        chipValue = int(words[1])
        botNumber = words[5]
        # Give microchip to bot
        giveChip("bot", botNumber, chipValue)
        # Check to see if bot is ready to transfer chips
        checkBot(botNumber)

    else:
        # Tells bot what to do with high and low chips
        # Extract info from line
        words = line.split(" ")
        botNumber = words[1]
        lowStruct = words[5]
        lowStructNumber = words[6]
        highStruct = words[10]
        highStructNumber = words[11]
        # Assign instructions for high and low
        if botNumber not in instructions:
            instructions[botNumber] = {}
        instructions[botNumber]["lowStruct"] = lowStruct
        instructions[botNumber]["lowNumber"] = lowStructNumber
        instructions[botNumber]["highStruct"] = highStruct
        instructions[botNumber]["highNumber"] = highStructNumber
        # Check to see if bot is ready to transfer chips
        checkBot(botNumber)

print("Part 2 solution: " + str(int(outputs["0"]["chips"][0])*int(outputs["1"]["chips"][0])*int(outputs["2"]["chips"][0])))
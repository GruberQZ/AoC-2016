file = open('input.txt','r')
count = 0

def checkForTLS(value):
    for i in range(len(value)-3):
        if value[i] != value[i+1] and value[i] == value[i+3] and value[i+1] == value[i+2]:
            return True

for line in file:
    tlsEnabled = False
    tlsBlocked = False
    string = ""
    for char in line:
        if char == "[":
            # Done with enable string
            if not tlsEnabled and not tlsBlocked:
                # Check to see if string enables TLS
                if checkForTLS(string) == True:
                    tlsEnabled = True
            # Reset string for next input
            string = ""
        elif char == "]":
            # Done with disable string
            if not tlsBlocked:
                # Check to see if string blocks TLS
                if checkForTLS(string) == True:
                    tlsBlocked = True
            # Reset string for next input
            string = ""
        else:
            # Add character to running string
            string += char
    # End of string check
    if len(string) != 0 and not tlsBlocked and not tlsEnabled:
        if checkForTLS(string) == True:
            tlsEnabled = True
    if tlsEnabled and not tlsBlocked:
        count += 1

print(count)
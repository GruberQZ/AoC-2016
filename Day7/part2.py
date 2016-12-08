file = open('input.txt','r')
count = 0
aba = []
bab = []

def generate(value, method):
    for i in range(len(value)-2):
        if value[i] != value[i+1] and value[i] == value[i+2]:
            if method == 'aba':
                aba.append(value[i] + value[i+1] + value[i+2])
            elif method == 'bab':
                bab.append(value[i+1] + value[i] + value[i+1])

for line in file:
    string = ""
    aba = []
    bab = []
    for char in line:
        if char == "[":
            generate(string,'aba')
            # Reset string for next input
            string = ""
        elif char == "]":
            generate(string, 'bab')
            # Reset string for next input
            string = ""
        else:
            # Add character to running string
            string += char
    # End of string check
    if len(string) != 0:
        generate(string, 'aba')
    # See if SSL is supported
    for entry in aba:
        if entry in bab:
            count += 1
            break

print(count)
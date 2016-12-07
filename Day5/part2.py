import hashlib

basePattern = "ugkcyxxp"
baseInt = 0
count = 0
password = [None] * 8

while True:
    # Build the string to hash
    pattern = basePattern + str(baseInt)
    result = hashlib.md5(pattern.encode('utf-8')).hexdigest()
    if result.startswith("00000"):
        print(result)
        if result[5] in ['0','1','2','3','4','5','6','7'] and password[int(result[5])] == None:
            password[int(result[5])] = result[6]
        print(password)
        if None not in password:
            break
    baseInt += 1

finalPass = ""
for char in password:
    finalPass += char

print("Password: " + finalPass)
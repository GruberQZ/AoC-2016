import hashlib

basePattern = "ugkcyxxp"
baseInt = 0
count = 0
password = ""

while True:
    # Build the string to hash
    pattern = basePattern + str(baseInt)
    result = hashlib.md5(pattern.encode('utf-8')).hexdigest()
    if result.startswith("00000"):
        print(result)
        password += result[5]
        if len(password) == 8:
            break
    baseInt += 1

print("Password: " + password)
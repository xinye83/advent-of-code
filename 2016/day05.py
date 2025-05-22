data = "reyedfim"

import hashlib

# --- part 1 ---

id = 0
password = ""

while len(password) < 8:
    hash = hashlib.md5((data + str(id)).encode("utf-8")).hexdigest()
    if hash[:5] == "00000":
        password += hash[5]
    id += 1

print(password)

# --- part 2 ---

id = 0
c = 0
password2 = ["*"] * 8
print("".join(password2), end="\r")

while c < 8:
    hash = hashlib.md5((data + str(id)).encode("utf-8")).hexdigest()
    if hash[:5] == "00000" and hash[5] in "01234567" and password2[int(hash[5])] == "*":
        password2[int(hash[5])] = hash[6]
        print("".join(password2), end="\r")
        c += 1
    id += 1

print("".join(password2))

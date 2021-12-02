# --- Day 25: Combo Breaker ---

card_public_key = 9717666
door_public_key = 20089533

# --- part 1 ---

subject_number = 7
divisor = 20201227

card_loop_size = 0
door_loop_size = 0

found1 = False
found2 = False

key = 1

while not found1 or not found2:

    if not found1:
        card_loop_size += 1
    if not found2:
        door_loop_size += 1

    key *= subject_number
    key %= divisor

    if key == card_public_key:
        found1 = True
    if key == door_public_key:
        found2 = True

encryption_key = 1

for i in range(card_loop_size):
    encryption_key *= door_public_key
    encryption_key %= divisor

print(encryption_key)

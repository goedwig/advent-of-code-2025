with open("input.txt") as f:
    moves = [(l[0], int(l[1:])) for l in f]

position, password_1, password_2 = 50, 0, 0
for direction, distance in moves:
    delta = 1
    if direction == "L":
        delta = -1
    for _ in range(distance):
        position += delta
        if position < 0:
            position = 99
        elif position > 99:
            position = 0

        if position == 0:
            password_2 += 1

    if position == 0:
        password_1 += 1

print(password_1)  # part 1
print(password_2)  # part 2

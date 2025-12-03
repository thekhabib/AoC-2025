import os

base = os.path.dirname(__file__)
path = os.path.join(base, "input")

s = 50
cnt = 0

with open(path) as file:
    for line in file:
        direction, value = line[0], int(line[1:])
        if direction == 'L':
            s -= value
        elif direction == 'R':
            s += value
        s %= 100
        if s == 0:
            cnt += 1
        
        # print(direction, value, cnt)

print(cnt)

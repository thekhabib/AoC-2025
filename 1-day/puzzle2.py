import os

base = os.path.dirname(__file__)
path = os.path.join(base, "input")

s = 50
cnt = 0

with open(path) as file:
    for line in file:
        direction, value = line[0], int(line[1:])

        cnt += value // 100
        value %= 100

        if direction == 'L':
            if value >= s > 0:
                cnt += 1
            s = (s - value) % 100
        elif direction == 'R':
            if s + value > 99:
                cnt += 1
            s = (s + value) % 100
        
        # print(direction, value, cnt)

print(cnt)

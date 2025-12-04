import os

base = os.path.dirname(__file__)
input_file = os.path.join(base, "input")

with open(input_file) as f:
    grid = [list(line.strip()) for line in f]

dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
R, C = len(grid), len(grid[0])

removed = 0

while True:
    to_remove = []

    for i in range(R):
        for j in range(C):
            if grid[i][j] == '@':
                neigh = 0
                for dx, dy in dirs:
                    x, y = i + dx, j + dy
                    if 0 <= x < R and 0 <= y < C and grid[x][y] == '@':
                        neigh += 1
                if neigh < 4:
                    to_remove.append((i, j))

    if not to_remove:
        break

    for i, j in to_remove:
        grid[i][j] = '.'

    removed += len(to_remove)

print(removed)

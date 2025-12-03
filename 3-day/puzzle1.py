import os

base = os.path.dirname(__file__)
input_file = os.path.join(base, "input")

with open(input_file) as f:
    banks = f.read().strip().splitlines()

total = 0

for bank in banks:
    a, b = bank[0], bank[1]

    for i, d in enumerate(bank):
        if d > a and i < len(bank) - 1:
            a = d
            b = bank[i + 1]
        elif d > b and i > 0:
            b = d
            
    # print(bank, a+b)
    total += int(a + b)

print(total)

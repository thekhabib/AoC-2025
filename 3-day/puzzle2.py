import os

base = os.path.dirname(__file__)
input_file = os.path.join(base, "input")

with open(input_file) as f:
    banks = f.read().strip().splitlines()

total = 0
need = 12

for bank in banks:
    best = []
    l = len(bank)

    for i, d in enumerate(bank):
        while best and best[-1] < d and (len(best) - 1 + l - i) >= 12:
            best.pop()
        
        if len(best) < need:
            best.append(d)

    # print(bank, int(''.join(best)))

    total += int(''.join(best))

print(total)

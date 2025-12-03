import os

base = os.path.dirname(__file__)
input_file = os.path.join(base, "input")

total = 0

with open(input_file) as f:
    for r in f.read().split(','):
        first, last = map(int, r.split('-'))

        lf = len_f = len(str(first))
        ll = len_l = len(str(last))

        if (lf & 1) and (ll & 1) and lf == ll:
            continue

        if lf & 1:
            first = 10 ** lf
            lf += 1

        if ll & 1:
            last = 10 ** (ll - 1) - 1
            ll -= 1

        if first > last:
            continue

        half_start = int(str(first)[:lf // 2])
        half_end   = int(str(last) [:ll // 2])

        for h in range(half_start, half_end + 1):
            n = int(f"{h}{h}")
            if n > last:
                break
            if n >= first:
                total += n

print(total)
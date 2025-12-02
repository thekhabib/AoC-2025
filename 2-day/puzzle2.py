import os
import bisect

base = os.path.dirname(__file__)
input_file = os.path.join(base, "input")

total = 0
seen = set()

with open(input_file) as f:
    ranges = sorted([list(map(int, r.split('-'))) for r in f.read().split(',')], key=lambda x: x[0])
    starts = [r[0] for r in ranges]

max_len = len(str(ranges[-1][1]))

for p in range(1, 10 ** (max_len // 2)):
    s = str(p)
    for k in range(2, max_len // len(s) + 1):
        x = int(s * k)
        i = bisect.bisect_right(starts, x) - 1
        if i >= 0:
            lo, hi = ranges[i]
            if lo <= x <= hi and x not in seen:
                seen.add(x)
                total += x

print(total)

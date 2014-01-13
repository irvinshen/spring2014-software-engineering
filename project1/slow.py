import sys

def calc_collatz(num, val):
    if num == 1:
        return val + 1
    # num is even
    elif num % 2 == 0:
        return calc_collatz(num / 2, val + 1)
    # num must be odd
    else:
        return calc_collatz(3 * num + 1, val + 1)

cache = {}
temp = {}
lines = []
for line in sys.stdin:
    if line.isspace():
        break
    lines.append(line)
    # print(line)
    m = 0
    lower = int(line.split()[0])
    upper = int(line.split()[1])

    for x in range(lower, upper + 1):
        t = calc_collatz(x, 0)
        if t > m:
            m = t

    temp[line] = m
    # print(line.rstrip() + ' ' + str(m))

for l in lines:
    print(l.rstrip() + ' ' + str(temp[l]))
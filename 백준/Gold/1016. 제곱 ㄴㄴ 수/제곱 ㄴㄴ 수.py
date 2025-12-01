min, max = map(int, input().split())

length = max - min + 1
is_checked = [False] * length

i = 2
while i * i <= max:
    square = i * i

    start = ((min + square - 1) // square) * square

    for x in range(start, max + 1, square):
        is_checked[x - min] = True

    i += 1

print(is_checked.count(False))
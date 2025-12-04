s, l = map(int, input().split())
answer = []

while l <= 100:
    m = 0
    for i in range(0, l):
        m += i

    first = (s - m) / l
    if first.is_integer():
        if first < 0:
            l += 1
            continue
        else:
            for j in range(0, l):
                answer.append(int(first + j))
            print(*answer)
            break

    l += 1

if l > 100:
    print(-1)
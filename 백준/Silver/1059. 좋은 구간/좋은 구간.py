size = int(input().strip())
s = list(map(int, input().split()))
n = int(input().strip())

s.sort()

if n in s:
    print(0)

else:
    left = 0
    right = 0

    temp = 0
    for i in s:
        if i > n:
            right = i
            left = temp
            break
        temp = i

    count = (n - left) * (right - n) - 1
    print(count)
X, Y = map(int, input().split())

Z = (Y * 100) // X

if Z >= 99:
    print(-1)

else:
    left, right = 0, 1000000000
    answer = 1000000000

    while left <= right:
        mid = (left + right) // 2
        newZ = (Y + mid) * 100 // (X + mid)

        if newZ > Z:
            answer = mid
            right = mid - 1

        else:
            left = mid + 1

    print(answer)
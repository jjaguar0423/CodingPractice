n = int(input().strip())

divs = list(map(int, input().split()))
divs.sort()

if n % 2 == 0:
    print(divs[0] * divs[n - 1])
else:
    print(divs[(n // 2)] ** 2)
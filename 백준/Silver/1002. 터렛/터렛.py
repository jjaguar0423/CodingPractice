import math

n = int(input().strip())

for _ in range(n):
    # x1, y1를 중심으로 하고 반지름이 r1인 원
    # x2, y2를 중심으로 하고 반지름이 r2인 원
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    br = max(r1, r2)
    sr = min(r1, r2)
    d = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

    # 두 원이 동일할 경우
    if (x1, y1, r1) == (x2, y2, r2):
        print(-1)
        continue

    # 한 원이 다른 원 내부에 있는 경우
    elif d + sr < br:
        print(0)

    # 한 원이 다른 원 외부에 있는 경우
    elif d > sr + br:
        print(0)

    # 두 원이 내접하는 경우
    elif d + sr == br:
        print(1)

    # 두 원이 외접하는 경우
    elif d == sr + br:
        print(1)

    # 두 원이 교차하는 경우
    else:
        print(2)
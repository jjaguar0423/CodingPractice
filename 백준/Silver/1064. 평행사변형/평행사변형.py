import math

ax, ay, bx, by, cx, cy = map(int, input().split())
leng = []

if (bx - ax) * (cy - ay) == (by - ay) * (cx - ax):
    print(-1.0)

else:
    AB = math.sqrt((ax - bx) ** 2 + (ay - by) ** 2)
    AC = math.sqrt((ax - cx) ** 2 + (ay - cy) ** 2)
    BC = math.sqrt((bx - cx) ** 2 + (by - cy) ** 2)

    # AB AC * 2
    len1 = (AB + AC) * 2
    leng.append(len1)

    # AB BC * 2
    len2 = (AB + BC) * 2
    leng.append(len2)

    # AC BC * 2
    len3 = (AC + BC) * 2
    leng.append(len3)

    leng.sort()
    print(leng[2] - leng[0])
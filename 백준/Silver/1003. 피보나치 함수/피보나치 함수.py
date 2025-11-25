n = int(input().strip())
nl = []
c0 = [0] * 41
c1 = [0] * 41

c0[0], c1[0] = 1, 0
c0[1], c1[1] = 0, 1

for i in range(2, 41):
    c0[i] = c0[i - 1] + c0[i - 2]
    c1[i] = c1[i - 1] + c1[i - 2]

for j in range(n):
    m = int(input().strip())
    nl.append(m)

for k in nl:
    print(c0[k], c1[k])
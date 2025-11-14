from math import comb

n = int(input().strip())
for _ in range(n):
    N, M = map(int, input().split())
    print(comb(M, N))
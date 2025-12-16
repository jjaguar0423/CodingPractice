N, K = map(int, input().split())
num = [i for i in range(1, N + 1)]
ans = []

for _ in range(N):
    idx = (K - 1) % len(num)
    num = num[idx:] + num[:idx]
    ans.append(num.pop(0))

print("<" + ", ".join(map(str, ans)) + ">")
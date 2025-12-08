from itertools import combinations

N = int(input())
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
ans = []

for i in range(1, 11):
    for comb in combinations(nums, i):
        lst = sorted(comb, reverse=True)
        s = ''.join(map(str, lst))
        ans.append(int(s))

ans.sort()

if N >= len(ans):
    print(-1)
else:
    print(ans[N])
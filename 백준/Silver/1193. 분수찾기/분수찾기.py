K = int(input())

n = 1

while K > n:
    K -= n
    n += 1

if n % 2 == 0:
    num = K
    den = n - K + 1
else:
    num = n - K + 1
    den = K

print(f"{num}/{den}")
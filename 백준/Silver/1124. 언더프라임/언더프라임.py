n, m = map(int, input().split())

def factorization(n):
    primes = []
    counts = []
    sum = 0

    d = 2
    while d * d <= n:
        cnt = 0
        while n % d == 0:
            n //= d
            cnt += 1
        if cnt > 0:
            primes.append(d)
            counts.append(cnt)
        d += 1

    if n > 1:
        primes.append(n)
        counts.append(1)

    for num in counts:
        sum += num

    return sum

def is_prime(n):
    if n < 2:
        return False

    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1

    return True

count = 0

for i in range(n, m + 1):
    if is_prime(factorization(i)):
        count += 1

print(count)
n = int(input())
count = 0

for i in range(2, len(bin(n))):
    s = str(bin(n))
    if s[i] == '1':
        count += 1

print(count)
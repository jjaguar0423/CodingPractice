n = int(input())

list1 = []

if n == 1:
    s = input()
    print(s)

# 파일 이름 입력
else:
    files = [input() for i in range(n)]

    result = ''
    for chars in zip(*files):
        if all(ch == chars[0] for ch in chars):
            result += chars[0]
        else:
            result += '?'

    print(result)
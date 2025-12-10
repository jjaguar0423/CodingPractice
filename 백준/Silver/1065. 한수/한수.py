N = int(input())

i = 1
han = []

def check_han(i):

    if len(str(i)) <= 2:
        han.append(i)

    else:
        one = int(str(i)[0])
        two = int(str(i)[1])
        three = int(str(i)[2])
        if three - two == two - one:
            han.append(i)

while i <= N:
    check_han(i)
    i += 1

print(len(han))
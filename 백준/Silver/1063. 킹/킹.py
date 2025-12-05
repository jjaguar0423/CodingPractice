king, stone, n = input().split()
n = int(n)

board = [['A8', 'B8', 'C8', 'D8', 'E8', 'F8', 'G8', 'H8'],
         ['A7', 'B7', 'C7' ,'D7', 'E7', 'F7', 'G7', 'H7'],
         ['A6', 'B6' ,'C6', 'D6', 'E6', 'F6', 'G6', 'H6'],
         ['A5', 'B5' ,'C5', 'D5', 'E5', 'F5', 'G5', 'H5'],
         ['A4', 'B4' ,'C4', 'D4', 'E4', 'F4', 'G4', 'H4'],
         ['A3', 'B3' ,'C3', 'D3', 'E3', 'F3', 'G3', 'H3'],
         ['A2', 'B2' ,'C2', 'D2', 'E2', 'F2', 'G2', 'H2'],
         ['A1', 'B1' ,'C1', 'D1', 'E1', 'F1', 'G1', 'H1']]

def get_pos(obj):
    col = ord(obj[0]) - ord('A')
    row = 8 - int(obj[1])
    return row, col

def move(x, y, dir):
    if dir == 'R':
        if y < 7:
            y += 1
    elif dir == 'L':
        if y > 0:
            y -= 1
    elif dir == 'B':
        if x < 7:
            x += 1
    elif dir == 'T':
        if x > 0:
            x -= 1
    elif dir == 'RT':
        if x > 0 and y < 7:
            x -= 1
            y += 1
    elif dir == 'LT':
        if x > 0 and y > 0:
            x -= 1
            y -= 1
    elif dir == 'RB':
        if x < 7 and y < 7:
            x += 1
            y += 1
    elif dir == 'LB':
        if x < 7 and y > 0:
            x += 1
            y -= 1

    return x, y

def move_king(sx, sy, kx, ky, dir):
    new_kx, new_ky = move(kx, ky, dir)

    if sx == new_kx and sy == new_ky:
        new_sx, new_sy = move(sx, sy, dir)
        if new_sx == sx and new_sy == sy:
            return sx, sy, kx, ky
        else:
            return new_sx, new_sy, new_kx, new_ky
    else:
        return sx, sy, new_kx, new_ky

kx, ky = get_pos(king)
sx, sy = get_pos(stone)

for i in range(n):
    dir = input()
    sx, sy, kx, ky = move_king(sx, sy, kx, ky, dir)

print(board[kx][ky])
print(board[sx][sy])
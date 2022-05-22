n, m = map(int, input().split())
store = int(input())
matrix = []
length = 0
for _ in range(store):
    x, y = map(int, input().split())
    if x == 1:
        x = y
        y = m
    elif x == 2:
        x = y
        y = 0
    elif x == 3:
        x = 0
        y = m-y
    elif x == 4:
        x = n
        y = m-y
    matrix.append((x, y))


pos_x, pos_y = map(int, input().split())
if pos_x == 1:
    pos_x = pos_y
    pos_y = m
elif pos_x == 2:
    pos_x = pos_y
    pos_y = 0
elif pos_x == 3:
    pos_x = 0
    pos_y = m-pos_y
elif pos_x == 4:
    pos_x = n
    pos_y = m-pos_y

for store_x, store_y in matrix:
    if not abs(store_x-pos_x) == n and not abs(store_y-pos_y) == m:
        length += abs(store_x-pos_x) + abs(store_y-pos_y)
    else:
        length += min(pos_x+pos_y+store_x+store_y, 2*n +
                      2*m-(pos_x+pos_y+store_x+store_y))
print(length)

r, c = map(int, input().split())
row = [0, r]
col = [0, c]

n = int(input())

for _ in range(n):
    type, num = map(int, input().split())

    if type == 0:
        col.append(num)
    else:
        row.append(num)

    row.sort()
    col.sort()

result_row = []
result_col = []

for i in range(len(row)-1):
    result_row.append(row[i+1] - row[i])

for i in range(len(col)-1):
    result_col.append(col[i+1] - col[i])

print(max(result_col) * max(result_row))

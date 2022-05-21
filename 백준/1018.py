import sys

white_board = ['WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW',
               'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW']

black_board = ['BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB',
               'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB']

data = []
result = 100000
n, m = map(int, sys.stdin.readline().split())

for _ in range(n):
    data.append(input())

for i in range(n-8+1):
    for j in range(m-8+1):
        count = 0
        for k in range(8):
            for l in range(8):
                if data[i+k][j+l] != white_board[k][l]:
                    count += 1
        result = min(result, count)
        count = 0
        for k in range(8):
            for l in range(8):
                if data[i+k][j+l] != black_board[k][l]:
                    count += 1
        result = min(result, count)

print(result)

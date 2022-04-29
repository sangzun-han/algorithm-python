N = 8
str1 = "WBWBWBWB"
str2 = "BWBWBWBW"
chess1 = [str1, str2, str1, str2, str1, str2, str1, str2]
chess2 = [str2, str1, str2, str1, str2, str1, str2, str1]
result = float('inf')

n, m = [int(x) for x in input().split()]
arr = []
for i in range(n):
    arr.append(input())
for i in range(n-N+1):
    for j in range(m-N+1):
        count = 0
        for k in range(N):
            for z in range(N):
                if arr[i+k][j+z] != chess1[k][z]:
                    count += 1
        result = min(result, count)
        count = 0
        for k in range(N):
            for z in range(N):
                if arr[i+k][j+z] != chess1[k][z]:
                    count += 1
        result = min(result, count)

print(result)

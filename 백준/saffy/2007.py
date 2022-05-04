n = int(input())

for i in range(n):
    pascal = []
    t = int(input())

    for i in range(t):
        temp = []
        for j in range(i+1):
            if j == 0 or j == i:
                temp.append(1)
            else:
                temp.append(pascal[i-1][j] + pascal[i-1][j-1])
        pascal.append(temp)


print(pascal)

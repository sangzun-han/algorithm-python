a = int(input())
for i in range(a, 0, -1):
    for j in range(i):
        print("", end=' ')
    for k in range(i):
        print("*",end=' ')
    print("")

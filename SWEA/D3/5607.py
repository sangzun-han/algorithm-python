t = int(input())

for tc in range(t):
    n, r = map(int, input().split())
    temp1 = 1
    temp2 = 1
    for i in range(n, n-r, -1):
        temp1 *= i

    for i in range(r, 1, -1):
        temp2 *= i

    print(f"#{tc+1} {(temp1//temp2)%1234567891}")

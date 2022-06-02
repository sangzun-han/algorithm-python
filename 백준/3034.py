n, w, h = map(int, input().split())

for _ in range(n):
    k = int(input())

    if k <= w or k <= h or k <= int((w*w + h*h)**0.5):
        print("DA")
    else:
        print("NE")

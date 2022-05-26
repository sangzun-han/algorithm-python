t = int(input())
for tc in range(t):
    n = int(input())  # 몇명

    print(f"#{tc+1}", end=' ')
    for _ in range(n):
        print(f"{1}/{n}", end=' ')
    print()

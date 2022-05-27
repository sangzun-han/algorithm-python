t = int(input())

for _ in range(t):
    dp = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9] + ([0] * 91)
    n = int(input())
    if n <= 9:
        print(dp[n-1])
    else:
        for i in range(10, n+1):
            dp[i] = dp[i-2] + dp[i-3]

        print(dp[n-1])

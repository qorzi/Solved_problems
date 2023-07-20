n = int(input())
l = list(map(int, input().split()))
r = list(map(int, input().split()))

dp = [[0]*(n+1) for _ in range(n+1)]
for i in range(n-1, -1, -1):
    for j in range(n-1, -1, -1):
        if l[i] > r[j]:
            dp[i][j] = dp[i][j+1] + r[j]
        else:
            dp[i][j] = max(dp[i+1][j], dp[i+1][j+1])

print(dp[0][0])

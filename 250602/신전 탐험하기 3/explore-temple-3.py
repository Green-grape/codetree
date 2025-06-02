import sys

n, m=map(int, input().split())

rewards=[list(map(int, input().split())) for _ in range(n)]

dp=[[-1]*(m) for _ in range(n)]

def get_max_rewards(i, j):
    if i==n:
        return 0
    if dp[i][j]!=-1:
        return dp[i][j]
    for idx in range(m):
        if idx!=j:
            dp[i][j]=max(dp[i][j], rewards[i][idx]+get_max_rewards(i+1, idx))
    return dp[i][j]


ret=0
for j in range(m):
    ret=max(ret, rewards[0][j]+get_max_rewards(1, j))
print(ret)
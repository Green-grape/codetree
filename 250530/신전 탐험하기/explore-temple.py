import sys

n=int(input())

rewards=[tuple(map(int, input().split())) for _ in range(n)]

dp=[[-1]*3 for _ in range(n)]

def get_max_rewards(i, j):
    if i==n:
        return 0
    if dp[i][j]!=-1:
        return dp[i][j]
    dp[i][j]=0
    for move in [0, 1, 2]:
        if move!=j:
            dp[i][j]=max(dp[i][j], rewards[i][move]+get_max_rewards(i+1, move))
    return dp[i][j]

ret=0;
for j in [0,1,2]:
    ret=max(ret, rewards[0][j]+get_max_rewards(1, j))
print(ret)
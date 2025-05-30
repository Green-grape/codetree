import sys

n, max_move=map(int, input().split())

phylons=[0 if s=='L' else 1 for s in input()]

dp=[[[-1]*(max_move+1) for _ in range(2)] for _ in range(n)]

def get_max_phylon(i, j, k):
    if i==n:
        return 0
    if dp[i][j][k]!=-1:
        return dp[i][j][k]
    dp[i][j][k]=0
    cur_ret=1 if phylons[i]==j else 0
    dp[i][j][k]=max(dp[i][j][k], cur_ret+get_max_phylon(i+1, j, k))
    if k<max_move:
        dp[i][j][k]=max(dp[i][j][k], cur_ret+get_max_phylon(i+1, (j+1)%2, k+1))
    return dp[i][j][k]

print(get_max_phylon(0, 0, 0))
    
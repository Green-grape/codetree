n=int(input())

dp=[[-1]*10 for _ in range(n+1)]

MOD=10**9+7

def mod_add(a,b):
    return ((a%MOD)+(b%MOD))%MOD

def get_stair_num_cnt(i, j):
    if i==n:
        return 1
    if dp[i][j]!=-1:
        return dp[i][j]
    dp[i][j]=0
    if j>0:
        dp[i][j]=mod_add(dp[i][j], get_stair_num_cnt(i+1, j-1))
    if j<9:
        dp[i][j]=mod_add(dp[i][j], get_stair_num_cnt(i+1, j+1))
    return dp[i][j]

ret=0
for j in range(1, 10):
    ret=mod_add(ret, get_stair_num_cnt(1, j))
print(ret)
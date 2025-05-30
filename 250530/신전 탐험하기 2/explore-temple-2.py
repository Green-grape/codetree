import sys

input=sys.stdin.readline

n=int(input())

rewards=[tuple(map(int, input().split())) for _ in range(n)]

dp=[[[-sys.maxsize]*3 for _ in range(3)] for _ in range(n)]

def get_max_rewards(i, j, k):
    if i==n:
        if j==k:
            return -sys.maxsize
        return 0
    if dp[i][j][k]!=-sys.maxsize:
        return dp[i][j][k]
    for move in [0,1,2]:
        if move!=j:
            cand=get_max_rewards(i+1, move, k)
            if cand!=-sys.maxsize:
                dp[i][j][k]=max(dp[i][j][k], cand+rewards[i][move])
    return dp[i][j][k]

ret=0
for j in range(3):
    ret=max(ret, rewards[0][j]+get_max_rewards(1, j, j))
print(ret)
        
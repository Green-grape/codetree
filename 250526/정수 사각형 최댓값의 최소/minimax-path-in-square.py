import sys

input=sys.stdin.readline

n=int(input())

MAX_NUM=1000001

boards=[list(map(int, input().split())) for _ in range(n)]
dp=[[MAX_NUM]*n for _ in range(n)]

move_dirs=[(-1, 0), (0, -1)]
def find_max_min(i, j):
    if dp[i][j]!=MAX_NUM:
        return dp[i][j]
    if i==0 and j==0:
        return boards[i][j]
    for dy, dx in move_dirs:
        y=i+dy
        x=j+dx
        if 0<=x<n and 0<=y<n:
            dp[i][j]=min(dp[i][j], max(find_max_min(y, x), boards[i][j]))
    return dp[i][j]


print(find_max_min(n-1, n-1))
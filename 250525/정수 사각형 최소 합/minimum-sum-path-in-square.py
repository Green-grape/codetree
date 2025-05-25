import sys

input=sys.stdin.readline

n=int(input())

boards=[list(map(int, input().split())) for _ in range(n)]

move_dirs=[(-1, 0), (0, 1)]
MAX=100*1000000
dp=[[MAX]*n for _ in range(n)]

def find_max_num(i, j):
    if dp[i][j]!=MAX:
        return dp[i][j]
    if i==0 and j==(n-1):
        return boards[i][j]

    for dy, dx in move_dirs:
        y=i+dy
        x=j+dx
        if 0<=x<n and 0<=y<n:
            dp[i][j]=min(dp[i][j], find_max_num(y, x)+boards[i][j])
    return dp[i][j]

print(find_max_num(n-1, 0))
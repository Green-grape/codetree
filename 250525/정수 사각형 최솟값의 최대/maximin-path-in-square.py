import sys

input=sys.stdin.readline

n=int(input())

MAX=1000001

boards=[list(map(int, input().split())) for _ in range(n)]
dp=[[0]*n for _ in range(n)]

move_dirs=[(-1, 0), (0, -1)]
def find_min_num_in_path(i, j):
    if dp[i][j]!=0:
        return dp[i][j]
    if i==0 and j==0:
        return boards[i][j]
    for dy, dx in move_dirs:
        y=i+dy
        x=j+dx
        if 0<=x<n and 0<=y<n:
            dp[i][j]=max(dp[i][j], min(find_min_num_in_path(y,x), boards[i][j]))
    return dp[i][j]

print(find_min_num_in_path(n-1, n-1))
    
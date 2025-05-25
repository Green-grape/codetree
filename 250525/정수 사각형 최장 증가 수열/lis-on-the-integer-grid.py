import sys

input=sys.stdin.readline

n=int(input())

boards=[list(map(int, input().split())) for _ in range(n)]
dp=[[0]*n for _ in range(n)]

move_dirs=[(-1, 0), (1, 0), (0, -1), (0, 1)]
def find_max_path(i, j):
    # i, j부터 이동해서 밟고 지나갈 수 있는 최대 칸의 수
    if dp[i][j]!=0:
        return dp[i][j]
    ret=1
    for dy, dx in move_dirs:
        y=i+dy
        x=j+dx
        if 0<=x<n and 0<=y<n and boards[i][j]<boards[y][x]:
            ret=max(ret, find_max_path(y, x)+1)
    dp[i][j]=ret
    return dp[i][j]

ret=0;
for i in range(n):
    for j in range(n):
        ret=max(ret, find_max_path(i, j))

print(ret)
import sys

input=sys.stdin.readline

n=int(input())

boards=[list(map(int, input().split())) for _ in range(n)]

dp=[[0]*n for _ in range(n)]


move_dirs=[(-1, 0), (0, -1)]
def find_max_num(i, j):
    # 0, 0~ i,j까지 움직였을때 거쳐간 숫자들의 합의 최대값을 반환
    if i==0 and j==0:
        return boards[i][j]
    for dy, dx in move_dirs:
        y=i+dy
        x=j+dx
        if 0<=x<n and 0<=y<n:
            dp[i][j]=max(dp[i][j], find_max_num(y, x)+boards[i][j])
    return dp[i][j]


print(find_max_num(n-1, n-1))
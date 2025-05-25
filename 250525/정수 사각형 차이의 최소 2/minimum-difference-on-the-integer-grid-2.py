import sys

input=sys.stdin.readline

n=int(input())

boards=[list(map(int, input().split())) for _ in range(n)]

dp=[[(-1, 101)]*n for _ in range(n)]

move_dirs=[(-1, 0), (0, -1)]
def find_min_max_in_path(i, j):
    # i, j까지의 경로중 최소값이 가장 작고 최대값이 가장 큰 경로의 (최소, 최대)쌍 반환
    if dp[i][j][0]!=-1 and dp[i][j][1]!=101:
        return dp[i][j]
    if i==0 and j==0:
        return (boards[i][j], boards[i][j])
    for dy, dx in move_dirs:
        y=i+dy
        x=j+dx
        if 0<=x<n and 0<=y<n:
            before_min, before_max=find_min_max_in_path(y, x)
            cur_min, cur_max=(min(before_min, boards[i][j]), max(before_max, boards[i][j]))
            if dp[i][j][1]-dp[i][j][0]>cur_max-cur_min:
                dp[i][j]=(cur_min, cur_max)
    return dp[i][j]

cur_min, cur_max=find_min_max_in_path(n-1, n-1)
print(cur_max-cur_min)
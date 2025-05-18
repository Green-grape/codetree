import os
import sys

input=sys.stdin.readline

sys.setrecursionlimit(100000)

n, m=map(int, input().split())

boards=[]

for _ in range(n):
    boards.append(list(map(int, input().split())))

move_dirs=[(-1, 0), (1, 0), (0,-1), (0,1)]
visit=[[False]*m for _ in range(n)]

def dfs(i, j):
    if visit[i][j]:
        return
    visit[i][j]=True
    for dy, dx in move_dirs:
        y=i+dy
        x=j+dx
        if x<0 or y<0 or x>=m or y>=n:
            continue
        if boards[y][x]==1:
            dfs(y, x)


dfs(0, 0)
print(1 if visit[n-1][m-1] else 0)
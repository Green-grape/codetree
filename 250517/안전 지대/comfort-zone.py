import os

data=os.read(0, os.fstat(0).st_size).splitlines()

ptr=0
n, m=map(int, data[ptr].decode().split())
ptr+=1

boards=[]
visit=[[False]*m for _ in range(n)]

for i in range(n):
    boards.append(list(map(int, data[ptr].decode().split())))
    ptr+=1

k=1
move_dirs=[(1,0), (-1, 0), (0, 1), (0, -1)]
def dfs(i, j):
    global k
    if visit[i][j]:
        return
    visit[i][j]=True
    for dy, dx in move_dirs:
        y=i+dy
        x=j+dx
        if x<0 or y<0 or x>=m or y>=n:
            continue
        if boards[y][x]<=k:
            continue
        dfs(y, x)

max_num=0
max_k=1
while k<=100:
    num=0;
    for i in range(n):
        for j in range(m):
            if (not visit[i][j]) and boards[i][j]>k:
                dfs(i, j)
                num+=1
    if num>max_num:
        max_k=k
        max_num=num
    k+=1
    visit=[[False]*m for _ in range(n)]


print(max_k, max_num)


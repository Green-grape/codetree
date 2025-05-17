import os

data=os.read(0, os.fstat(0).st_size).splitlines()
ptr=0

n=int(data[ptr])
ptr+=1

boards=[]
visit=[[False]*n for _ in range(n)]

for i in range(n):
    boards.append(list(map(int, data[ptr].decode().split())))
    ptr+=1

move_dirs=[(1, 0), (-1, 0), (0, 1), (0, -1)]
def dfs(i, j):
    if visit[i][j]:
        return 0
    visit[i][j]=True
    ret=1
    for dy, dx in move_dirs:
        y=dy+i
        x=dx+j
        if y<0 or x<0 or y>=n or x>=n:
            continue
        if boards[y][x]!=boards[i][j]:
            continue
        ret+=dfs(y, x)
    return ret

max_size=0
total_cnt=0
for i in range(n):
    for j in range(n):
        if visit[i][j]==0:
            cand=dfs(i, j)
            max_size=max(cand, max_size)
            if cand>=4:
                total_cnt+=1

print(str(total_cnt)+" "+str(max_size))



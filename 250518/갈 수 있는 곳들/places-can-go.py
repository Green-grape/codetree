import sys

input=sys.stdin.readline

n, k=map(int, input().split())
boards=[]

for _ in range(n):
    boards.append(list(map(int, input().split())))

move_dirs=[(-1, 0), (1, 0), (0, 1), (0, -1)]
bfs_visit=[[False]*n for _ in range(n)]
for _ in range(k):
    i, j=map(int, input().split())
    i-=1
    j-=1
    if bfs_visit[i][j]:
        continue
    queue=[(i, j)]
    while len(queue)>0:
        i, j=queue.pop(0)
        for dy, dx in move_dirs:
            y=i+dy
            x=j+dx
            if 0<=x<n and 0<=y<n and not bfs_visit[y][x] and boards[y][x]==0:
                queue.append((y, x))
                bfs_visit[y][x]=True


ret=0
for i in range(n):
    for j in range(n):
        if bfs_visit[i][j]:
            ret+=1
print(ret)
        


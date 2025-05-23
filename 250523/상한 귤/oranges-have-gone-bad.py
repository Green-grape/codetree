import sys

input=sys.stdin.readline

n, k=map(int, input().split())

boards=[list(map(int, input().split())) for _ in range(n)]

ORANGE=1
R_ORANGE=2

step=[[-1]*n for _ in range(n)]
queue=[]
for i in range(n):
    for j in range(n):
        if boards[i][j]==R_ORANGE:
            step[i][j]=0
            queue.append((i, j, 0))

move_dirs=[(-1, 0), (1, 0), (0, 1), (0, -1)]
ret=0
while len(queue)>0:
    i, j, cur_move=queue.pop(0)
    for dy, dx in move_dirs:
        y=i+dy
        x=j+dx
        if 0<=x<n and 0<=y<n:
            if boards[y][x]==ORANGE and step[y][x]==-1:
                step[y][x]=cur_move+1
                boards[y][x]=R_ORANGE
                ret=max(ret, cur_move+1)
                queue.append((y,x, cur_move+1))

for i in range(n):
    for j in range(n):
        if boards[i][j]==ORANGE:
            step[i][j]=-2

print("\n".join([" ".join([str(num) for num in row]) for row in step]))



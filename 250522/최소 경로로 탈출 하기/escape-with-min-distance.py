import sys

input=sys.stdin.readline

n, m=map(int, input().split())

boards=[]

for i in range(n):
    boards.append(list(map(int, input().split())))

visit=[[False]*m for _ in range(n)]
step=[[0]*m for _ in range(n)]

queue=[(0, 0, 0)]
move_dirs=[(1, 0), (-1, 0), (0, 1), (0, -1)]
while len(queue)>0:
    i, j, cur_move=queue.pop(0)
    visit[i][j]=True
    step[i][j]=cur_move
    for dy, dx in move_dirs:
        y=i+dy
        x=j+dx
        if y<0 or x<0 or x>=m or y>=n:
            continue
        if not visit[y][x] and boards[y][x]==1:
            queue.append((y, x, cur_move+1))
            visit[y][x]=True
            
print(step[n-1][m-1] if step[n-1][m-1]!=0 else -1)
        

    
    
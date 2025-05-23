import sys
from itertools import combinations

input=sys.stdin.readline

n, k=map(int, input().split())

boards=[list(map(int, input().split())) for _ in range(n)]

start_r, start_c=map(int, input().split())
end_r, end_c=map(int, input().split())
start_r-=1
start_c-=1
end_r-=1
end_c-=1

walls=[]
WALL=1
for i in range(n):
    for j in range(n):
        if boards[i][j]==WALL:
            walls.append(i*n+j)

move_dirs=[(-1,0), (1, 0), (0, 1), (0, -1)]
ret=n*n
for wall_idx_list in combinations(walls, k):
    for wall_idx in wall_idx_list:
        y, x=wall_idx//n, wall_idx%n
        boards[y][x]=0
    visit=[[False]*n for _ in range(n)]
    step=[[-1]*n for _ in range(n)]
    queue=[(start_r, start_c, 0)]
    step[start_r][start_c]=0;
    is_end=False
    while len(queue)>0:
        i, j, cur_move=queue.pop(0)
        for dy, dx in move_dirs:
            next_y=i+dy
            next_x=j+dx
            if 0<=next_y<n and 0<=next_x<n:
                if not visit[next_y][next_x] and boards[next_y][next_x]!=WALL:
                    visit[next_y][next_x]=True
                    step[next_y][next_x]=cur_move+1
                    if next_y==end_r and next_x==end_c:
                        is_end=True
                        break
                    queue.append((next_y, next_x, cur_move+1))
        if is_end:
            break
    if step[end_r][end_c]!=-1:
        ret=min(ret, step[end_r][end_c])
    for wall_idx in wall_idx_list:
        y, x=wall_idx//n, wall_idx%n
        boards[y][x]=WALL

print(ret if ret<n*n else -1)
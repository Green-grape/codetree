import sys
import itertools 

input=sys.stdin.readline

n, k, u, d=map(int, input().split())

boards=[list(map(int, input().split())) for _ in range(n)]

combs=itertools.combinations([i for i in range(n*n)], k)
move_dirs=[(1, 0), (-1, 0), (0, 1), (0, -1)]
ret=0;
for comb in combs:
    visit=[[False]*n for _ in range(n)]
    find_cnt=0;
    for idx in comb:
        y, x=idx//n, idx%n
        if visit[y][x]:
            continue
        visit[y][x]=True
        find_cnt+=1
        queue=[(y, x)]
        while len(queue)>0:
            i, j=queue.pop(0)
            cur_height=boards[i][j]
            for dy, dx in move_dirs:
                next_y=i+dy
                next_x=j+dx
                if next_x<0 or next_y<0 or next_x>=n or next_y>=n:
                    continue
                height_diff=abs(cur_height-boards[next_y][next_x])
                if visit[next_y][next_x]==False and (height_diff<=d and height_diff>=u):
                    visit[next_y][next_x]=True
                    find_cnt+=1
                    queue.append((next_y, next_x))
    ret=max(ret, find_cnt)
print(ret)    



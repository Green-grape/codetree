import sys
import itertools

input=sys.stdin.readline

n, k, m=map(int, input().split())

boards=[list(map(int, input().split())) for _ in range(n)]

start_pos=[tuple(x-1 for x in map(int, input().split())) for _ in range(k)]

stones=[]
for i in range(n):
    for j in range(n):
        if boards[i][j]==1:
            stones.append((i, j))

combinations=itertools.combinations([i for i in range(len(stones))], m)

ret=0
move_dirs=[(-1, 0), (1, 0), (0, 1), (0, -1)]
for comb in combinations:
    visit=[[False]*n for _ in range(n)]
    for idx in comb:
        boards[stones[idx][0]][stones[idx][1]]=0
    find_cnt=0
    for y, x in start_pos:
        if visit[y][x]:
            continue
        queue=[(y, x)]
        visit[y][x]=True
        find_cnt+=1
        while len(queue)>0:
            i, j=queue.pop(0)
            for dy, dx in move_dirs:
                next_y=i+dy
                next_x=j+dx
                if next_x<0 or next_y<0 or next_x>=n or next_y>=n:
                    continue
                if visit[next_y][next_x]==False and boards[next_y][next_x]==0:
                    visit[next_y][next_x]=True
                    find_cnt+=1
                    queue.append((next_y, next_x))
    ret=max(ret, find_cnt)
    for idx in comb:
        boards[stones[idx][0]][stones[idx][1]]=1

print(ret)
import sys

input=sys.stdin.readline

n, m=map(int, input().split())

boards=[list(map(int, input().split())) for _ in range(n)]

move_dirs=[(-1, 0), (1, 0), (0, -1), (0, 1)]

iter_cnt=0;
before_size=0;
while True:
    visit=[[False]*m for _ in range(n)]
    cand_pos=[]
    queue=[(0, 0)]
    visit[0][0]=True
    while len(queue)>0:
        i, j=queue.pop(0)
        for dy, dx in move_dirs:
            y=i+dy
            x=j+dx
            if x<0 or y<0 or x>=m or y>=n:
                continue
            if visit[y][x]:
                continue
            visit[y][x]=True
            if boards[y][x]==1:
                cand_pos.append((y, x))
            else:
                queue.append((y, x))
    if len(cand_pos)==0:
        break
    for y, x in cand_pos:
        boards[y][x]=0
    before_size=len(cand_pos)
    iter_cnt+=1
    
print(iter_cnt, before_size)

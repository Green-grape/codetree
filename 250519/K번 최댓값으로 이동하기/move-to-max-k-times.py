import sys
input=sys.stdin.readline

n, m=map(int, input().split())

boards=[list(map(int, input().split())) for _ in range(n)]

r, c=map(int, input().split())
r-=1
c-=1

move_dirs=[(-1, 0), (1, 0), (0, 1), (0, -1)]
for _ in range(m):
    visit=[[False]*n for _ in range(n)]
    queue=[(r, c)]
    cur_max=-1
    cur_max_pos=[]
    init_num=boards[r][c]
    while len(queue)>0:
        i, j=queue.pop(0)
        for dy, dx in move_dirs:
            y=i+dy
            x=j+dx
            if x<0 or y<0 or x>=n or y>=n:
                continue
            if visit[y][x]==False and boards[y][x]<init_num:
                visit[y][x]=True
                queue.append((y, x))
                if boards[y][x]>cur_max:
                    cur_max=boards[y][x]
                    cur_max_pos=[(y, x)]
                elif boards[y][x]==cur_max:
                    cur_max_pos.append((y, x))
    if len(cur_max_pos)>0:
        cur_max_pos.sort(lambda x: (x[0], x[1]))
        r, c=cur_max_pos[0]
    else:
        break

print(r+1, c+1)
    


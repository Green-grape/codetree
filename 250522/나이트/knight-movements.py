import sys

input=sys.stdin.readline

n=int(input())

start_r, start_c, end_r, end_c=map(int, input().split())
start_r-=1
start_c-=1
end_r-=1
end_c-=1

move_dirs=[(-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2)]
boards=[[False]*n for _ in range(n)]
step=[[-1]*n for _ in range(n)]

queue=[(start_r, start_c, 0)]
boards[start_r][start_c]=True
step[start_r][start_c]=0
while len(queue)>0:
    i, j, cur_move=queue.pop(0)
    for dy, dx in move_dirs:
        y=i+dy
        x=j+dx
        if x<0 or y<0 or x>=n or y>=n:
            continue
        if not boards[y][x]:
            boards[y][x]=True
            step[y][x]=cur_move+1
            queue.append((y,x, cur_move+1))

print(step[end_r][end_c])
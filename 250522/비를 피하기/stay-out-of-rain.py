import sys

input = sys.stdin.readline

n, h, m = map(int, input().split())

boards = [list(map(int, input().split())) for _ in range(n)]
ret = [[0] * n for _ in range(n)]

MOVEABLE = 0
WALL = 1
PERSON = 2
AVOID_RAIN = 3

move_dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
for i in range(n):
    for j in range(n):
        if boards[i][j] == PERSON:
            is_end = False
            visit = [[False] * n for _ in range(n)]
            visit[i][j] = True
            queue = [(i, j, 0)]
            while len(queue) > 0:
                y, x, cur_move = queue.pop(0)
                for dy, dx in move_dirs:
                    next_y = dy + y
                    next_x = dx + x
                    if next_x < 0 or next_y < 0 or next_x >= n or next_y >= n:
                        continue
                    if (not visit[next_y][next_x]) and (boards[next_y][next_x] != WALL):

                        if boards[next_y][next_x] == AVOID_RAIN:
                            ret[i][j] = cur_move + 1
                            is_end = True
                            break
                        visit[next_y][next_x] = True
                        queue.append((next_y, next_x, cur_move + 1))
                if is_end:
                    break
            if is_end == False:
                ret[i][j] = -1

print("\n".join([" ".join([str(num) for num in row]) for row in ret]))

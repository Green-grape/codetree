import os

data = os.read(0, os.fstat(0).st_size).splitlines()
ptr = 0
n, m = map(int, data[ptr].decode().split())
ptr += 1

boards = []
visit = [[False] * m for _ in range(n)]

for i in range(n):
    boards.append(list(map(int, data[ptr].decode().split())))
    ptr += 1

move_dirs = [(1, 0), (0, 1)]


def dfs(i, j):
    if visit[i][j]:
        return
    visit[i][j] = True
    for dy, dx in move_dirs:
        y = i + dy
        x = j + dx
        if y < 0 or x < 0 or x >= m or y >= n:
            continue
        if boards[y][x] == 0:
            continue
        dfs(y, x)


dfs(0, 0)
print(1 if visit[n - 1][m - 1] == True else 0)

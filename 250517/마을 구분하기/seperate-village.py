import os

data = os.read(0, os.fstat(0).st_size).splitlines()
ptr = 0

n = int(data[ptr])
ptr += 1

boards = []
visit = [[False] * n for _ in range(n)]

for _ in range(n):
    boards.append(list(map(int, data[ptr].decode().split())))
    ptr += 1

move_dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
vilages = []


def dfs(i, j, cur_val):
    if visit[i][j]:
        return
    visit[i][j] = True
    if len(vilages) == cur_val:
        vilages.append(1)
    else:
        vilages[cur_val] += 1
    for dy, dx in move_dirs:
        y = i + dy
        x = j + dx
        if y < 0 or x < 0 or x >= n or y >= n:
            continue
        if boards[y][x] == 0:
            continue
        dfs(y, x, cur_val)


num = 0
for i in range(n):
    for j in range(n):
        if visit[i][j] == False and boards[i][j] == 1:
            dfs(i, j, num)
            num += 1

vilages.sort()
print(len(vilages))
print("\n".join([str(num) for num in vilages]))

import sys

input = sys.stdin.readline

n = int(input())

boards = [list(map(int, input().split())) for _ in range(n)]

MAX_NUM = 101
dp = [[[None] * MAX_NUM for _ in range(n)] for _ in range(n)]
dp2 = [[[None] * MAX_NUM for _ in range(n)] for _ in range(n)]

move_dirs = [(-1, 0), (0, -1)]


def find_min_max_in_path(i, j, k):
    # i, j까지의 경로에서 k이상의 값만을 사용하여 지나가는 경로들의 최대값의 최소
    if dp[i][j][k] != None:
        return dp[i][j][k]
    if i == 0 and j == 0:
        if boards[i][j] >= k:
            dp[i][j][k] = boards[i][j]
        else:
            dp[i][j][k] = MAX_NUM
        return dp[i][j][k]
    dp[i][j][k] = MAX_NUM
    for dy, dx in move_dirs:
        y = i + dy
        x = j + dx
        if 0 <= x < n and 0 <= y < n and boards[y][x] >= k:
            cand = find_min_max_in_path(y, x, k)
            if cand == MAX_NUM:
                continue
            cur_max = max(boards[i][j], cand)
            dp[i][j][k] = min(dp[i][j][k], cur_max)
    return dp[i][j][k]


def find_real_min_value_in_path(i, j, k):
    # i, j까지의 경로에서 k이상의 값만을 사용하여 지나가는 경로들의 실제 최소값
    if dp2[i][j][k] != None:
        return dp2[i][j][k]
    if i == 0 and j == 0:
        return boards[i][j]
    dp2[i][j][k] = boards[i][j]
    for dy, dx in move_dirs:
        y = i + dy
        x = j + dx
        if 0 <= x < n and 0 <= y < n and boards[y][x] >= k:
            cand = find_real_min_value_in_path(y, x, k)
            dp2[i][j][k] = min(dp2[i][j][k], cand)
    return dp2[i][j][k]


ret = MAX_NUM
for k in range(1, MAX_NUM):
    cur_max = find_min_max_in_path(n - 1, n - 1, k)
    cur_min = find_real_min_value_in_path(n - 1, n - 1, k)
    if cur_max == MAX_NUM:
        continue
    ret = min(ret, cur_max - cur_min)
print(ret)

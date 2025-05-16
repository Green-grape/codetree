n = int(input())

boards = [list(map(int, input().split())) for _ in range(n)]
visit = [0] * n
visit[0] = 1

ret = 10000 * 10


def search_min_path(idx, cur_val):
    global ret
    if sum(visit) == n and boards[idx][0] != 0:
        ret = min(ret, cur_val + boards[idx][0])
        return
    for i in range(1, n):
        if visit[i] == 0 and boards[idx][i] != 0:
            visit[i] = 1
            search_min_path(i, cur_val + boards[idx][i])
            visit[i] = 0


search_min_path(0, 0)
print(ret)

import os
import sys


input = sys.stdin.readline


sys.setrecursionlimit(100000)

n, m = map(int, input().split())

boards = []

for _ in range(n):
    boards.append(list(map(int, input().split())))

move_dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
bfs_visited = [[False] * m for _ in range(n)]


def bfs(i, j):
    queue = [(i, j)]
    bfs_visited[i][j] = True
    while len(queue) > 0:
        i, j = queue.pop(0)
        for move_dir in move_dirs:
            ni, nj = i + move_dir[0], j + move_dir[1]
            if (
                0 <= ni < n
                and 0 <= nj < m
                and not bfs_visited[ni][nj]
                and boards[ni][nj] == 1
            ):
                bfs_visited[ni][nj] = True
                queue.append((ni, nj))


bfs(0, 0)
print(1 if bfs_visited[n - 1][m - 1] else 0)

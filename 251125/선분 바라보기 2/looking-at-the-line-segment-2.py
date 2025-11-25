from sortedcontainers import SortedList

# f = open("./test_case.txt", "r")
# input = f.readline

n = int(input())
points = []

for i in range(n):
    y, x1, x2 = map(int, input().split())
    points.append((x1, +1, i, y))
    points.append((x2, -1, i, y))

points.sort()

y_set = SortedList()
ret = 0
prev_min_y = None

visited = [False] * n

for x, typ, idx, y in points:
    if typ == 1:
        y_set.add((y, idx))
    else:
        y_set.remove((y, idx))
    if not y_set:
        continue
    _, target_idx = y_set[0]
    visited[target_idx] = True

print(sum(visited))
 
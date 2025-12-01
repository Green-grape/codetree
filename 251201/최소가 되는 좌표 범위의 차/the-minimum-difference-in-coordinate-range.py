from sortedcontainers import SortedList, SortedSet

# input = open("./test_case.txt", "r").readline

n, d = map(int, input().split())

coords = []

for i in range(n):
    x, y = map(int, input().split())
    coords.append((x, y))

coords.sort()

j = 1
x_min_diff = float("inf")
sorted_y = SortedList()
is_inserted = [False] * n
for i in range(n):
    if not is_inserted[i]:
        sorted_y.add(coords[i][1])
    while j < n and sorted_y[-1] - sorted_y[0] < d:
        if not is_inserted[j]:
            is_inserted[j] = True
            sorted_y.add(coords[j][1])
        j += 1
    if sorted_y[-1] - sorted_y[0] >= d:
        x_min_diff = min(x_min_diff, coords[j - 1][0] - coords[i][0])
    sorted_y.remove(coords[i][1])

print(x_min_diff if x_min_diff != float("inf") else -1)

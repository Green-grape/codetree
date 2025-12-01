n, d = map(int, input().split())

coords = []

for i in range(n):
    x, y = map(int, input().split())
    coords.append((x, y))

coords.sort()

j = 1
x_min_diff = float("inf")
for i in range(n):
    y_min = coords[i][1]
    y_max = coords[i][1]
    while j < n and y_max - y_min <= d:
        y_max = max(y_max, coords[j][1])
        y_min = min(y_min, coords[j][1])
        j += 1
    if y_max - y_min >= d:
        x_min_diff = min(x_min_diff, coords[j - 1][0] - coords[i][0])

print(x_min_diff if x_min_diff != float("inf") else -1)

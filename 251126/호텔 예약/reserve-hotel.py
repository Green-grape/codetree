n = int(input())

points = []

for i in range(n):
    a, b = map(int, input().split())
    points.append((a, i, 1))
    points.append((b + 1, i, -1))


cur_concurrency = 0
max_concurrency = 0
for point in sorted(points):
    cur_concurrency += point[2]
    max_concurrency = max(max_concurrency, cur_concurrency)
print(max_concurrency)

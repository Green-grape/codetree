n = int(input())

points = []
for _ in range(n):
    x, y = map(int, input().split())
    points.append((x, 1))
    points.append((y, -1))

points.sort()
current_coverage = 0
max_coverage = 0
for point, delta in points:
    current_coverage += delta
    max_coverage = max(max_coverage, current_coverage)
print(max_coverage)

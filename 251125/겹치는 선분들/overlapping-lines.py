n, k = map(int, input().split())

before_end = 0
points = []
for _ in range(n):
    delta, pos = input().split()
    delta = int(delta)
    if pos == "L":
        cur_end = before_end - delta
    else:
        cur_end = before_end + delta

    if cur_end > before_end:
        points.append((before_end, 1))
        points.append((cur_end, -1))
    else:
        points.append((cur_end, 1))
        points.append((before_end, -1))

points.sort()

coverage = 0
ret = 0
for _ in range(len(points)):
    coverage += points[_][1]
    if coverage >= k:
        ret += 1
print(ret)

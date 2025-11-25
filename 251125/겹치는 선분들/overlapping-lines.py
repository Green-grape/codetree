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
    before_end = cur_end

points.sort()

coverage = 0
ret = 0
for i in range(len(points) - 1):
    coverage += points[i][1]
    if coverage >= k:
        ret += points[i + 1][0] - points[i][0]
print(ret) 

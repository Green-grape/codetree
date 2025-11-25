n = int(input())

points = []

for i in range(n):
    a, b = map(int, input().split())
    points.append((a, i, 1))
    points.append((b, i, -1))

points.sort()

remain_line_count = 0
cur_min = None
cur_max = None

ret = 0
for x, idx, v in points:
    if v == 1:
        if remain_line_count == 0:
            cur_min = x
        remain_line_count += 1
    else:
        remain_line_count -= 1
        if remain_line_count == 0:
            cur_max = x
            ret =max(ret, cur_max - cur_min)
            cur_min = None
            cur_max = None

print(ret)

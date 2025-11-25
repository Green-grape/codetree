n = int(input())

points = []

for i in range(n):
    x, y = map(int, input().split())
    points.append((x, i, 1))
    points.append((y, i, -1))
points.sort()

active = set()
union_length = 0
unique = [0] * n

last_x = points[0][0]
for x, i, typ in points:
    dx = x - last_x
    if dx > 0:
        if active:
            union_length += dx
            if len(active) == 1:
                only = next(iter(active))
                unique[only] += dx

    if typ == 1:
        active.add(i)
    else:
        active.remove(i)
    last_x = x

min_unique = min(unique)
print(union_length - min_unique)

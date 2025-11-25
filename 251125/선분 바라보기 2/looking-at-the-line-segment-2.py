from sortedcontainers import SortedList

n = int(input())
points = []

for i in range(n):
    y, x1, x2 = map(int, input().split())
    points.append((x1, y, 1))  # start
    points.append((x2, y, -1))  # end

# x 기준 정렬
points.sort()

y_set = SortedList()
ret = 0
prev_min_y = None

for x, y, typ in points:
    if typ == 1:  # interval enters
        y_set.add(y)
    else:  # interval leaves
        y_set.remove(y)

    # 현재 최소 y 계산
    curr_min_y = y_set[0] if y_set else None

    # 변화 감지
    if curr_min_y != prev_min_y and curr_min_y is not None:
        ret += 1

    prev_min_y = curr_min_y

print(ret)

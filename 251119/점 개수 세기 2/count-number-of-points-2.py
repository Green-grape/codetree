from bisect import bisect_left, bisect_right

n, q = map(int, input().split())

coords = []
set_x = set()
set_y = set()
for _ in range(n):
    x, y = map(int, input().split())
    coords.append((x, y))
    set_x.add(x)
    set_y.add(y)


sorted_x = sorted(set_x)
sorted_y = sorted(set_y)
compressed_grid = [[0] * (len(sorted_y)) for _ in range(len(sorted_x))]
for x, y in coords:
    cx = bisect_left(sorted_x, x)
    cy = bisect_left(sorted_y, y)
    compressed_grid[cx][cy] += 1

prefix_sum = [[0] * (len(sorted_y) + 1) for _ in range(len(sorted_x) + 1)]
for i in range(1, len(sorted_x) + 1):
    for j in range(1, len(sorted_y) + 1):
        prefix_sum[i][j] = (
            prefix_sum[i - 1][j]
            + prefix_sum[i][j - 1]
            - prefix_sum[i - 1][j - 1]
            + compressed_grid[i - 1][j - 1]
        )

ret = []
for _ in range(q):
    x1, y1, x2, y2 = map(int, input().split())
    cx1 = bisect_left(sorted_x, x1) + 1
    cy1 = bisect_left(sorted_y, y1) + 1
    cx2 = bisect_right(sorted_x, x2)
    cy2 = bisect_right(sorted_y, y2)

    result = (
        prefix_sum[cx2][cy2]
        - prefix_sum[cx1 - 1][cy2]
        - prefix_sum[cx2][cy1 - 1]
        + prefix_sum[cx1 - 1][cy1 - 1]
    )
    ret.append(str(result))
print("\n".join(ret))

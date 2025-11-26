n = int(input())

MAX_N = 1000
boards = [[0 for _ in range(MAX_N + 1)] for _ in range(MAX_N + 1)]
prefix_sums = [[0 for _ in range(MAX_N + 2)] for _ in range(MAX_N + 2)]
x_counts = [0 for _ in range(MAX_N + 1)]
y_counts = [0 for _ in range(MAX_N + 1)]

for _ in range(n):
    x, y = map(int, input().split())
    boards[y][x] += 1
    x_counts[x] += 1
    y_counts[y] += 1

for i in range(1, MAX_N + 2):
    for j in range(1, MAX_N + 2):
        prefix_sums[i][j] = (
            prefix_sums[i - 1][j]
            + prefix_sums[i][j - 1]
            - prefix_sums[i - 1][j - 1]
            + boards[i - 1][j - 1]
        )


def get_area_sum(x1, y1, x2, y2):
    return (
        prefix_sums[y2 + 1][x2 + 1]
        - prefix_sums[y1][x2 + 1]
        - prefix_sums[y2 + 1][x1]
        + prefix_sums[y1][x1]
    )


ret = float("inf")
for y in range(MAX_N):
    for x in range(MAX_N):
        if x_counts[x] == 0 and y_counts[y] == 0:
            area_sum1 = get_area_sum(0, 0, x - 1, y - 1)
            area_sum2 = get_area_sum(x + 1, 0, MAX_N - 1, y - 1)
            area_sum3 = get_area_sum(0, y + 1, x - 1, MAX_N - 1)
            area_sum4 = get_area_sum(x + 1, y + 1, MAX_N - 1, MAX_N - 1)
            max_sum = max(area_sum1, area_sum2, area_sum3, area_sum4)
            ret = min(ret, max_sum)
print(ret)

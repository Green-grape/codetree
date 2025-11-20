n = int(input())

coords = []
for _ in range(n):
    x, y = map(int, input().split())
    coords.append((x, y))

left_sums = []  # left_sums[i]=0~i번째 까지의 manhattan 거리 합
right_sums = []  # right_sums[i]=i~n-1번째 까지의 manhattan 거리 합


def get_manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


left_sum = 0
left_sums.append(0)
for i in range(1, n):
    left_sum += get_manhattan_distance(coords[i - 1], coords[i])
    left_sums.append(left_sum)

right_sum = 0
right_sums.append(0)
for i in range(n - 2, -1, -1):
    right_sum += get_manhattan_distance(coords[i], coords[i + 1])
    right_sums.append(right_sum)
right_sums.reverse()

ret = float("inf")
for j in range(1, n - 1):
    left_sum = left_sums[j - 1]
    right_sum = right_sums[j + 1]
    skip_distance = get_manhattan_distance(coords[j - 1], coords[j + 1])
    total_distance = left_sum + right_sum + skip_distance
    ret = min(ret, total_distance)
print(ret)

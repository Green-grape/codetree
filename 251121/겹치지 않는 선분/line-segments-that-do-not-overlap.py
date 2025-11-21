n = int(input())

coords = []  # (x1, x2)
for _ in range(n):
    a, b = map(int, input().split())
    coords.append((a, b))

coords.sort()

left_x2_max = [0] * n  # left_x2_max[i] = 0~i까지 x2의 최댓값
right_x2_min = [0] * n  # right_x2_min[i] = i~n-1까지 x1의 최솟값

left_x2_max[0] = coords[0][1]
for i in range(1, n):
    left_x2_max[i] = max(left_x2_max[i - 1], coords[i][1])

right_x2_min[n - 1] = coords[n - 1][1]
for i in range(n - 2, -1, -1):
    right_x2_min[i] = min(right_x2_min[i + 1], coords[i][1])


ret = 0
for i in range(n):
    check_left = left_x2_max[i - 1] > coords[i][1] if i > 0 else False
    check_right = right_x2_min[i + 1] < coords[i][1] if i < n - 1 else False
    if not check_left and not check_right:
        ret += 1
print(ret)

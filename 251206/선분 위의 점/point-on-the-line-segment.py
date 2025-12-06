n, m = map(int, input().split())

coords = list(map(int, input().split()))
coords.sort()

coord_cnts = []
for _ in range(m):
    l, r = map(int, input().split())

    l_idx = -1  # l보다 같거나 큰 수 중 가장 작은 인덱스
    r_idx = -1  # r보다 같거나 큰 수 중 가장 작은 인덱스

    left = 0
    right = n - 1
    while left <= right:
        mid = (left + right) // 2
        if coords[mid] == l:
            l_idx = mid
            break
        if coords[mid] < l:
            left = mid + 1
        else:
            right = mid - 1
    if l_idx == -1:
        l_idx = left

    left = 0
    right = n - 1
    while left <= right:
        mid = (left + right) // 2
        if coords[mid] == r:
            r_idx = mid
            break
        if coords[mid] < r:
            left = mid + 1
        else:
            right = mid - 1
    if r_idx == -1:
        r_idx = left

    if l_idx == -1:
        l_idx = left
    if r_idx == -1:
        r_idx = right
    if r_idx < n and coords[r_idx] == r:
        r_idx += 1
    coord_cnts.append(r_idx - l_idx)

print("\n".join(map(str, coord_cnts)))

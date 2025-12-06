def get_moo_cnt(num):
    return num // 3 + num // 5 - num // 15


left = 1
right = 10**9

target = int(input())
while left <= right:
    mid = (left + right) // 2
    cnt = get_moo_cnt(mid)
    num_cnt = mid - cnt
    if num_cnt < target:
        left = mid + 1
    else:
        right = mid - 1
print(left)

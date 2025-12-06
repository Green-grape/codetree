n, m = map(int, input().split())

kernel_list = [int(input()) for _ in range(m)]

left = 1
right = 10**15

while left <= right:
    mid = (left + right) // 2
    cnt = 0
    for k in kernel_list:
        cnt += mid // k
    if cnt >= n:
        right = mid - 1
    else:
        left = mid + 1
print(left)

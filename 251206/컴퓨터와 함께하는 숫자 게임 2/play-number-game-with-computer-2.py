m = int(input())

start, end = map(int, input().split())

min_iter = m
max_iter = 0
for i in range(start, end + 1):
    left = 1
    right = m
    iter_count = 0
    while left <= right:
        mid = (left + right) // 2
        iter_count += 1
        if mid == i:
            break
        elif mid < i:
            left = mid + 1
        else:
            right = mid - 1
    min_iter = min(min_iter, iter_count)
    max_iter = max(max_iter, iter_count)
print(min_iter, max_iter)

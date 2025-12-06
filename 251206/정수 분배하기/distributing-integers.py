n, k = map(int, input().split())

nums = []

for _ in range(n):
    nums.append(int(input()))

left, right = 1, 100000
while left <= right:
    mid = (left + right) // 2
    count = 0
    for num in nums:
        count += num // mid

    if count >= k:
        left = mid + 1
    else:
        right = mid - 1
print(right)

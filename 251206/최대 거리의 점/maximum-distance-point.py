n, k = map(int, input().split())

nums = []
for _ in range(n):
    nums.append(int(input()))

nums.sort()


left = 1
right = nums[-1] - nums[0]

while left <= right:
    mid = (left + right) // 2
    # mid 간격으로 k개 이상의 공유기를 설치할 수 있는지 확인
    count = 1
    last = nums[0]
    for i in range(1, n):
        if nums[i] - last >= mid:
            count += 1
            last = nums[i]
    if count >= k:
        left = mid + 1
    else:
        right = mid - 1
print(right)

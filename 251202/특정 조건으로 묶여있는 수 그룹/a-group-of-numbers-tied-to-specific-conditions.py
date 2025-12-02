n, k = map(int, input().split())

nums = []
for _ in range(n):
    nums.append(int(input()))

nums.sort()

max_num = 0
i = 0
left_groups = [
    0
] * n  # left_groups[i]: 0~i까지 숫자를 모두 사용하여 그룹의 차가 k보다 작거나 같은 최대 그룹 수
for j in range(n):
    while nums[j] - nums[i] > k:
        i += 1
    max_num = max(max_num, j - i + 1)
    left_groups[j] = max_num

right_groups = [
    0
] * n  # right_groups[i]: i~n-1까지 숫자를 모두 사용하여 그룹의 차가 k보다 작거나 같은 최대 그룹 수
max_num = 0
j = n - 1
for i in range(n - 1, -1, -1):
    while nums[j] - nums[i] > k:
        j -= 1
    max_num = max(max_num, j - i + 1)
    right_groups[i] = max_num

ans = 0
for i in range(n - 1):
    ans = max(ans, left_groups[i] + right_groups[i + 1])
print(ans)

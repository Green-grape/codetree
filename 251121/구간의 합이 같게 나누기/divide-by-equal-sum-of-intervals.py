n = int(input())
nums = list(map(int, input().split()))

total = sum(nums)
if total % 4 != 0 or n < 4:
    print(0)
    exit()

target = total // 4

# prefix[i] = 0 ~ i 까지의 합
prefix = [0] * n
s = 0
for i in range(n):
    s += nums[i]
    prefix[i] = s

# left_cnt[i] = 0 ~ i 구간에서 prefix == target 인 위치 개수
left_cnt = [0] * n
for i in range(n):
    if prefix[i] == target:
        left_cnt[i] = (left_cnt[i - 1] if i > 0 else 0) + 1
    else:
        left_cnt[i] = left_cnt[i - 1] if i > 0 else 0

# right_cnt[i] = i ~ n-2 구간에서 prefix == 3*target 인 위치 개수
right_cnt = [0] * n
for i in range(n - 1, -1, -1):
    if i < n - 1 and prefix[i] == 3 * target:
        right_cnt[i] = right_cnt[i + 1] + 1
    else:
        right_cnt[i] = right_cnt[i + 1] if i < n - 1 else 0

# 두 번째 컷 j: 1 <= j <= n-3
result = 0
for j in range(1, n - 2):
    if prefix[j] == 2 * target:
        # 첫 번째 컷은 [0 .. j-1], 세 번째 컷은 [j+1 .. n-2]
        result += left_cnt[j - 1] * right_cnt[j + 1]

print(result)

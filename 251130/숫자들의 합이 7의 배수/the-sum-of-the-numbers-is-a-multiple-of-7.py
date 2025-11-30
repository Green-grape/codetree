n = int(input())

nums = []
for _ in range(n):
    nums.append(int(input()))

MOD = 7

prefix_sums = [0] * (n + 1)
for i in range(n):
    prefix_sums[i + 1] = ((prefix_sums[i] % MOD) + (nums[i] % MOD)) % MOD

remain_min_idx = [
    float("inf")
] * MOD  # remain_min_idx[i]: prefix_sums % MOD == i의 최소 인덱스
remain_max_idx = [-1] * MOD  # remain_max_idx[i]: prefix_sums % MOD == i의 최대 인덱스

for i in range(1, n + 1):
    remain = prefix_sums[i] % MOD
    remain_min_idx[remain] = min(remain_min_idx[remain], i)
    remain_max_idx[remain] = max(remain_max_idx[remain], i)

ans = 0
for i in range(MOD):
    if remain_max_idx[i] != -1:
        ans = max(ans, remain_max_idx[i] - remain_min_idx[i], 1) # 최소 1
print(ans)

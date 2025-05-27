n = int(input())

nums = [1, 2, 5]
MOD = 10007


def find_add_kind(n):
    dp = [-1] * (n + 1)
    dp[0] = 0
    for num in nums:
        dp[num] = 1
    for val in range(1, n + 1):
        for num in nums:
            if val < num or dp[val - num] == -1:
                continue
            if dp[val] == -1:
                dp[val] = 0
            dp[val] = (dp[val] % MOD + (dp[val - num]) % MOD) % MOD
    return dp[n]
print(find_add_kind(n))
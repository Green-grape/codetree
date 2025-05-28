import sys

input = sys.stdin.readline

n = int(input())

nums = list(map(int, input().split()))


def get_min_diff():
    # 현재 A그룹의 합이 a일때 이때 b의 값
    total_sum = sum(nums)
    dp = [False] * (total_sum + 1)
    dp[0] = True
    for num in nums:
        for val in range(total_sum, num - 1, -1):
            if dp[val - num]:
                dp[val] = True
    ret = len(dp)
    for val in range(1, len(dp)):
        if dp[val]:
            ret = min(ret, abs(total_sum - 2 * val))
    return ret


print(get_min_diff())

import sys

n = int(input())

nums = list(map(int, input().split()))

total_sum = sum(nums)

# i번째까지 다루었을때 A그룹의 총합은 j, B그룹의 총합은 k가 가능한가? --> X

# i번째까지 다루었을때 A그룹의 총합-B그룹의 총합 j일때 A의 그룹의 총합의 최대값
dp = [[-1] * (2 * total_sum + 1) for _ in range(n)]

dp[0][nums[0] + total_sum] = nums[0]  # 첫 번째 숫자를 그룹 A에 넣는 경우
dp[0][-nums[0] + total_sum] = 0  # 첫 번째 숫자를 그룹 B에 넣는 경우
dp[0][total_sum] = 0  # 첫 번째 숫자를 그룹 C에 넣는 경우 (그룹 A와 B에 넣지 않음)

for i, num in enumerate(nums[1:], start=1):
    for diff in range(-total_sum, total_sum + 1):
        # num을 그룹 A에 넣는 경우
        if diff + num + total_sum < len(dp[i]) and dp[i - 1][diff + total_sum] != -1:
            dp[i][diff + num + total_sum] = max(
                dp[i][diff + num + total_sum], dp[i - 1][diff + total_sum] + num
            )

        # num을 그룹 B에 넣는 경우
        if diff - num + total_sum >= 0 and dp[i - 1][diff + total_sum] != -1:
            dp[i][diff - num + total_sum] = max(
                dp[i][diff - num + total_sum], dp[i - 1][diff + total_sum]
            )

        # num을 그룹 C에 넣는 경우
        dp[i][diff + total_sum] = max(
            dp[i][diff + total_sum], dp[i - 1][diff + total_sum]
        )


print(dp[n - 1][total_sum])  # 그룹 A와 B의 합이 같을 때, 그룹 A의 최대 합

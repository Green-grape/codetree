import io
import os
import sys

sys.setrecursionlimit(10**6)

input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

n, div = map(int, input().split())

nums = list(map(int, input().split()))

# i: 이전 구간의 마지막 index, j 구간 넘버, 이전에 구간이 끊어졌는지 여부

dp = [[[-sys.maxsize] * 2 for _ in range(div + 1)] for _ in range(n)]

BEFORE_REMAIN = 0  # 앞에 이전 구간에 선택된 숫자가 있는 경우
BEFORE_FREE = 1  # 앞에 어떤 구간에도 속하지 않은 수가 있고 그 숫자가 선택 가능한 경우


def get_max_div_sum(i, j, k):
    # i번쨰 숫자를 확인해야하고 현재 j만큼의 구간이 나누어져있고 i번째에 숫자에 대한 상태에 k일때
    # div개의 구간을 선택해 얻을 수 있는 구간내에 얻을 수 있는 숫자의 최대합
    if i == n:
        if j < div:
            return -sys.maxsize + 1  # 구간이 충분히 나누어지지 않은 경우
        else:
            return 0
    if dp[i][j][k] >= -sys.maxsize + 1:
        return dp[i][j][k]

    if k == BEFORE_REMAIN:
        # 구간을 이어감
        cand = get_max_div_sum(i + 1, j, BEFORE_REMAIN)
        if cand != -sys.maxsize:
            dp[i][j][k] = max(dp[i][j][k], nums[i] + cand)

        # 구간을 끊는다.
        cand = get_max_div_sum(i + 1, j, BEFORE_FREE)
        if cand != -sys.maxsize:
            dp[i][j][k] = max(dp[i][j][k], cand)
    else:
        # 새로운 구간을 만듦
        if j < div:
            cand = get_max_div_sum(i + 1, j + 1, BEFORE_REMAIN)
            if cand != -sys.maxsize:
                dp[i][j][k] = max(dp[i][j][k], nums[i] + cand)

        # 그냥 지나침
        cand = get_max_div_sum(i + 1, j, BEFORE_FREE)
        if cand != -sys.maxsize:
            dp[i][j][k] = max(dp[i][j][k], cand)
    return dp[i][j][k]


print(get_max_div_sum(0, 0, BEFORE_FREE))

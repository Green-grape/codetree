import sys

input = sys.stdin.readline

la, lb = map(int, input().split())

arr_a = list(map(int, input().split()))
arr_b = list(map(int, input().split()))

dp = [[-1] * (lb + 1) for _ in range(la + 1)]
dp[0][0] = 0

for i in range(la + 1):
    for j in range(lb + 1):
        if dp[i][j] == -1:
            continue
        if i < la and j < lb and arr_a[i] == arr_b[j]:
            dp[i + 1][j + 1] = max(dp[i + 1][j + 1], 1 + dp[i][j])
        if i < la:
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
        if j < lb:
            dp[i][j + 1] = max(dp[i][j + 1], dp[i][j])


def dfs(i, j):
    if i == la or j == lb:
        return []
    if arr_a[i] == arr_b[j]:
        return [arr_a[i]] + dfs(i + 1, j + 1)
    if dp[i + 1][j] == dp[i][j + 1]:
        s1 = dfs(i + 1, j)
        s2 = dfs(i, j + 1)
        if len(s1) > len(s2):
            return s1
        elif len(s1) < len(s2):
            return s2
        else:
            return min(s1, s2)
    elif dp[i + 1][j] > dp[i][j + 1]:
        return dfs(i + 1, j)
    else:
        return dfs(i, j + 1)


ret = dfs(0, 0)
print(" ".join(map(str, ret)))

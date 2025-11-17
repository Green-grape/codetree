n, k = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

prefix_sum = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        prefix_sum[i][j] = (
            arr[i - 1][j - 1]
            + prefix_sum[i - 1][j]
            + prefix_sum[i][j - 1]
            - prefix_sum[i - 1][j - 1]
        )

ret = float("-inf")
for r in range(n):
    for c in range(n):
        total = 0
        for d in range(k + 1):
            up = r - d
            if up >= 0:
                left = max(0, c - (k - d))
                right = min(n - 1, c + (k - d))
                if left <= right:  # [up,left] ~ [up,right]
                    total += (
                        prefix_sum[up + 1][right + 1]
                        - prefix_sum[up + 1][left]
                        - prefix_sum[up][right + 1]
                        + prefix_sum[up][left]
                    )
            down = r + d
            if d > 0 and down < n:
                left = max(0, c - (k - d))
                right = min(n - 1, c + (k - d))
                if left <= right:  # [down,left] ~ [down,right]
                    total += (
                        prefix_sum[down + 1][right + 1]
                        - prefix_sum[down + 1][left]
                        - prefix_sum[down][right + 1]
                        + prefix_sum[down][left]
                    )

        ret = max(ret, total)
print(ret)

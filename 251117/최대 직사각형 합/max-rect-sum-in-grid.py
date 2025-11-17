import itertools

n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]

prefix_sums = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        prefix_sums[i][j] = (
            arr[i - 1][j - 1]
            + prefix_sums[i - 1][j]
            + prefix_sums[i][j - 1]
            - prefix_sums[i - 1][j - 1]
        )


def get_submatrix_sum(x1, y1, x2, y2):
    return (
        prefix_sums[x2 + 1][y2 + 1]
        - prefix_sums[x1][y2 + 1]
        - prefix_sums[x2 + 1][y1]
        + prefix_sums[x1][y1]
    )


def max_subarray_sum(sums):
    # 인덱스 i를 오른쪽 끝으로 갖는 구간의 최대 부분합
    cache = [float("-inf")] * len(sums)
    cache[0] = sums[0]
    for i in range(1, len(sums)):
        cache[i] = max(0, cache[i - 1]) + sums[i]
    return max(cache)


ret = float("-inf")
for row1 in range(n):
    for row2 in range(row1, n):
        sums = []
        for col in range(n):
            sums.append(get_submatrix_sum(row1, col, row2, col))

        # 최대 연속 부분합 계산
        result = max_subarray_sum(sums)
        ret = max(ret, result)
print(ret)

n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

arr_one_indexes = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(n):
    for j in range(n):
        arr_one_indexes[i + 1][j + 1] = arr[i][j]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        arr_one_indexes[i][j] = (
            arr_one_indexes[i][j - 1]
            + arr_one_indexes[i - 1][j]
            - arr_one_indexes[i - 1][j - 1]
            + arr_one_indexes[i][j]
        )
result = 0
for i in range(n - k + 1):
    for j in range(n - k + 1):
        total = (
            arr_one_indexes[i + k][j + k]
            - arr_one_indexes[i + k][j]
            - arr_one_indexes[i][j + k]
            + arr_one_indexes[i][j]
        )
        if total > result:
            result = total
print(result)

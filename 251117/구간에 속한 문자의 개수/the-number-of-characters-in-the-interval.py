n, m, k = map(int, input().split())

arr = [list(input()) for _ in range(n)]

prefix_sums_a = [[0] * (m + 1) for _ in range(n + 1)]
prefix_sums_b = [[0] * (m + 1) for _ in range(n + 1)]
prefix_sums_c = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        prefix_sums_a[i][j] = (
            prefix_sums_a[i - 1][j]
            + prefix_sums_a[i][j - 1]
            - prefix_sums_a[i - 1][j - 1]
        )
        prefix_sums_b[i][j] = (
            prefix_sums_b[i - 1][j]
            + prefix_sums_b[i][j - 1]
            - prefix_sums_b[i - 1][j - 1]
        )
        prefix_sums_c[i][j] = (
            prefix_sums_c[i - 1][j]
            + prefix_sums_c[i][j - 1]
            - prefix_sums_c[i - 1][j - 1]
        )

        if arr[i - 1][j - 1] == "a":
            prefix_sums_a[i][j] += 1
        elif arr[i - 1][j - 1] == "b":
            prefix_sums_b[i][j] += 1
        else:
            prefix_sums_c[i][j] += 1

ret = []
for _ in range(k):
    r1, c1, r2, c2 = map(int, input().split())
    count_a = (
        prefix_sums_a[r2][c2]
        - prefix_sums_a[r1 - 1][c2]
        - prefix_sums_a[r2][c1 - 1]
        + prefix_sums_a[r1 - 1][c1 - 1]
    )
    count_b = (
        prefix_sums_b[r2][c2]
        - prefix_sums_b[r1 - 1][c2]
        - prefix_sums_b[r2][c1 - 1]
        + prefix_sums_b[r1 - 1][c1 - 1]
    )
    count_c = (
        prefix_sums_c[r2][c2]
        - prefix_sums_c[r1 - 1][c2]
        - prefix_sums_c[r2][c1 - 1]
        + prefix_sums_c[r1 - 1][c1 - 1]
    )
    ret.append(f"{count_a} {count_b} {count_c}")
print("\n".join(ret))

n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

max_sum = 0
for i in range(n - k + 1):
    for j in range(n - k + 1):
        # i~i+k-1, j~j+k-1의 합 계산
        cur_sum = 0
        for x in range(i, i + k):
            for y in range(j, j + k):
                cur_sum += arr[x][y]
        max_sum = max(max_sum, cur_sum)
print(max_sum)

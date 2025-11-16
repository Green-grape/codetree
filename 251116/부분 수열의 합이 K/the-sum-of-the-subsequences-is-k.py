n, k = map(int, input().split())

arr = list(map(int, input().split()))

arr = [0] + arr

prefix_sum = [0] * (n + 1)

for i in range(1, n + 1):
    prefix_sum[i] = prefix_sum[i - 1] + arr[i]


count = 0
for i in range(1, n + 1):
    for j in range(i, n + 1):
        total = prefix_sum[j] - prefix_sum[i] + arr[i]
        if total == k:
            count += 1
print(count)

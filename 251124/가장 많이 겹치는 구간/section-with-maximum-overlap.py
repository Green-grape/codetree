n = int(input())

MAX_NUM = 200000

arr = [0] * (MAX_NUM + 1)

for _ in range(n):
    a, b = map(int, input().split())
    arr[a] += 1
    arr[b] -= 1

sum_val = 0
ret = 0
for i in range(MAX_NUM + 1):
    sum_val += arr[i]
    ret = max(ret, sum_val)
print(ret)

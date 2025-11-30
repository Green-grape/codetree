n, target_sum = map(int, input().split())

numbers = []
for _ in range(n):
    numbers.append(int(input()))

numbers.sort()

j = n - 1
ret = 0
for i in range(n):
    while j > i and numbers[i] + numbers[j] > target_sum:
        j -= 1
    if j <= i:
        break
    ret += j - i
print(ret)

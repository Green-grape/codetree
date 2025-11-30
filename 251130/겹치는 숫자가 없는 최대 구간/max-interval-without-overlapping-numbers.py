n = int(input())

numbers = list(map(int, input().split()))

cur_set = set()
j = 0
ans = 0
for i in range(n):
    while j < n and numbers[j] not in cur_set:
        cur_set.add(numbers[j])
        j += 1
    ans = max(ans, len(cur_set))
    cur_set.remove(numbers[i])

print(ans)

n = int(input())


arr = []

for i in range(n):
    a, b = map(int, input().split())
    arr.append((a, 1, i))
    arr.append((b, -1, i))

arr.sort()

ans = 0
remain_lines_cnt = 0
for x, v, idx in arr:
    if v == 1:
        if remain_lines_cnt == 0:
            ans += 1
        remain_lines_cnt += 1
    else:
        remain_lines_cnt -= 1

print(ans)

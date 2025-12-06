
n, m = map(int, input().split())

lines = [tuple(map(int, input().split())) for _ in range(m)]

lines.sort()

left = 0
right = 10**18

while left <= right:
    mid = (left + right) // 2

    count = 0
    prev = -1
    for a, b in lines:
        if count == 0:
            pos = a
        else:
            pos = max(a, prev + mid)

        if pos > b:
            continue
        cnt = (b - pos) // mid + 1
        count += cnt
        prev = pos + (cnt - 1) * mid

    if count >= n:
        left = mid + 1
    else:
        right = mid - 1
print(right)

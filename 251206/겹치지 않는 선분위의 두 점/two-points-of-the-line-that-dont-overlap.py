n, m = map(int, input().split())

lines = [tuple(map(int, input().split())) for _ in range(m)]

lines.sort()

left = 0
right = 10**18

while left <= right:
    mid = (left + right) // 2

    count = 1
    prev = lines[0][0]
    for a, b in lines:
        count += (b - prev) // mid
        if (b - prev) // mid > 0:
            prev += ((b - prev) // mid) * mid
    if count >= n:
        left = mid + 1
    else:
        right = mid - 1
print(right)

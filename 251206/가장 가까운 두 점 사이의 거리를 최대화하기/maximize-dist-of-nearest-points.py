n = int(input())

lines = [tuple(map(int, input().split())) for _ in range(n)]

lines.sort()

left = 0
right = 10**9

while left <= right:
    mid = (left + right) // 2

    prev = -1
    is_ok = True
    for a, b in lines:
        if prev == -1:
            pos = a
        else:
            pos = max(a, prev + mid)

        if pos > b:
            is_ok = False
            break
        prev = pos

    if is_ok:
        left = mid + 1
    else:
        right = mid - 1
print(right)

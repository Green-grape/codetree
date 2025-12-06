n, m = map(int, input().split())

nums_a = list(map(int, input().split()))
nums_b = list(map(int, input().split()))

left_contains = [
    -1
] * n  # left_contains[i]=nums_b[0~i]를 앞에서부터 맞출때 nums_b[i]가 대응 되는 nums_a의 최소 index
right_contains = [
    -1
] * n  # right_contains[i]=nums_b[i~m-1]를 뒤에서부터 맞출때 nums_b[i]가 대응 되는 nums_a의 최대 index

j = 0
for i in range(n):
    if j < m and nums_a[i] == nums_b[j]:
        left_contains[j] = i
        j += 1


j = m - 1
for i in range(n - 1, -1, -1):
    if j >= 0 and nums_a[i] == nums_b[j]:
        right_contains[j] = i
        j -= 1

ans = 0
for i in range(m):
    if i == 0:
        if right_contains[i + 1] != -1:
            ans += 1
    elif i == m - 1:
        if left_contains[i - 1] != -1:
            ans += 1
    else:
        if (
            left_contains[i - 1] != -1
            and right_contains[i + 1] != -1
            and left_contains[i - 1] < right_contains[i + 1]
        ):
            ans += 1
print(ans)

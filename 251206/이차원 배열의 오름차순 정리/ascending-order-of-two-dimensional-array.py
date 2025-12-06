n = int(input())

k = int(input())

# 1,2,3,...,n
# 2,4,6,...,2n
# ...
# n,2n,3n,...,n*n

left = 1
right = n * n
while left < right:
    mid = (left + right) // 2
    count = 0
    for i in range(1, n + 1):
        count += min(mid // i, n)
    if count < k:
        left = mid + 1
    else:
        right = mid
print(left)

n, m = map(int, input().split())

arr_a = list(map(int, input().split()))
arr_b = list(map(int, input().split()))


j = 0
ret = "No"
for i in range(n):
    if arr_a[i] == arr_b[j]:
        j += 1
    if j == m:
        ret = "Yes"
        break
print(ret)

import math

n = int(input())


def get_sum(num):
    return num * (num + 1) // 2


MAX_N = 10**18
left, right = 1, int((math.sqrt(2 * MAX_N)))

while left < right:
    mid = (left + right + 1) // 2
    if get_sum(mid) <= n:
        left = mid
    else:
        right = mid - 1
print(left)

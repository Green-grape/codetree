n, q = map(int, input().split())

MAX_POS = 1000000
pos = [0] * (MAX_POS + 1)

nums = list(map(int, input().split()))
for num in nums:
    pos[num] = 1

prefix_sum = [0] * (MAX_POS + 2)
for i in range(1, MAX_POS + 2):
    prefix_sum[i] = prefix_sum[i - 1] + pos[i - 1]

ret = []
for _ in range(q):
    l, r = map(int, input().split())
    result = prefix_sum[r + 1] - prefix_sum[l + 1] + pos[l]
    ret.append(str(result))
print("\n".join(ret))

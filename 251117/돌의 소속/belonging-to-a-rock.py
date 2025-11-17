n, q = map(int, input().split())

# i번 돌에 적힌수
stones = [0] * (n + 1)
for i in range(1, n + 1):
    num = int(input())
    stones[i] = num

# i번까지 몇개의 돌이 있는지
prefix_sum_1 = [0] * (n + 1)
prefix_sum_2 = [0] * (n + 1)
prefix_sum_3 = [0] * (n + 1)

for i in range(1, n + 1):
    prefix_sum_1[i] = prefix_sum_1[i - 1]
    prefix_sum_2[i] = prefix_sum_2[i - 1]
    prefix_sum_3[i] = prefix_sum_3[i - 1]

    if stones[i] % 3 == 0:
        prefix_sum_3[i] += 1
    elif stones[i] % 3 == 1:
        prefix_sum_1[i] += 1
    else:
        prefix_sum_2[i] += 1

ret = []
for _ in range(q):
    l, r = map(int, input().split())
    count_1 = prefix_sum_1[r] - prefix_sum_1[l - 1]
    count_2 = prefix_sum_2[r] - prefix_sum_2[l - 1]
    count_3 = prefix_sum_3[r] - prefix_sum_3[l - 1]
    ret.append(f"{count_1} {count_2} {count_3}")
print("\n".join(ret))

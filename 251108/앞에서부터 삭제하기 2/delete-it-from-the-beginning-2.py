n = int(input())

MAX_NUM = 10000

nums = list(map(int, input().split()))

# min_nums[i]=앞에서 부터 i개의 값을 삭제하고 난 후, 남아 있는 수들 중 최소값
min_nums = [MAX_NUM] * (n)
# sum_nums[i]=앞에서 부터 i개의 값을 삭제하고 난 후, 남아 있는 수들의 합
sum_nums = [0] * (n)

for i in range(n - 2, 0, -1):
    if i == n - 2:
        min_nums[i] = min(nums[i], nums[i + 1])
        sum_nums[i] = nums[i] + nums[i + 1]
    else:
        min_nums[i] = min(min_nums[i + 1], nums[i])
        sum_nums[i] = sum_nums[i + 1] + nums[i]
mean = 0
for k in range(1, n - 1):
    cur_mean = (sum_nums[k] - min_nums[k]) / (n - k - 1)
    mean = max(mean, cur_mean)
print(f"{mean:.2f}")

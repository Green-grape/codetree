n, m = map(int, input().split())

nums = list(map(int, input().split()))

left_min_subarr = [
    float("inf")
] * n  # left_min_subarr[i]: 0~i까지의 모든 수를 사용하였을때 1~M까지의 수를 모두 포함하는 가장 짧은 부분배열의 길이

count_dict = {}

j = 0
for i in range(n):
    while j < n and len(count_dict) < m:
        count_dict[nums[j]] = count_dict.get(nums[j], 0) + 1
        j += 1
    if len(count_dict) == m:
        left_min_subarr[i] = j - i
    count_dict[nums[i]] -= 1
    if count_dict[nums[i]] == 0:
        del count_dict[nums[i]]

ret = float("inf")
count_dict.clear()
for i in range(n):
    if i > 0:  # 구간을 벗어난것을 count
        count_dict[nums[i - 1]] = count_dict.get(nums[i - 1], 0) + 1
    j = i + left_min_subarr[i] - 1  # 구간의 끝 인덱스
    while j < n and len(count_dict) < m:
        count_dict[nums[j]] = count_dict.get(nums[j], 0) + 1
        j += 1
    if len(count_dict) == m:
        ret = min(ret, left_min_subarr[i])

print(ret if ret != float("inf") else -1)

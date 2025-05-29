import sys

input = sys.stdin.readline

n = int(input())

nums = [0] + list(map(int, input().split()))

cache = [[-1] * (4) for _ in range(n + 1)]


def get_max_coin(idx, one_jump_cnt):
    # 현재 idx 층이고 1계단 오르는 것을 one_jump_cnt만큼 수행하였을때 최대 코인 개수
    if idx > n:
        return -sys.maxsize
    if cache[idx][one_jump_cnt] != -1:
        return cache[idx][one_jump_cnt]
    if idx == n:
        return nums[idx]
    for jump in [1, 2]:
        if idx + jump > n:
            continue
        if jump == 1 and one_jump_cnt < 3:
            cand = get_max_coin(idx + jump, one_jump_cnt + 1)
            if cand != -1:
                cache[idx][one_jump_cnt] = max(
                    cache[idx][one_jump_cnt],
                    nums[idx] + get_max_coin(idx + jump, one_jump_cnt + 1),
                )
        if jump == 2:
            cand = get_max_coin(idx + jump, one_jump_cnt)
            if cand != -1:
                cache[idx][one_jump_cnt] = max(
                    cache[idx][one_jump_cnt],
                    nums[idx] + get_max_coin(idx + jump, one_jump_cnt),
                )
    return cache[idx][one_jump_cnt]


print(get_max_coin(0, 0))

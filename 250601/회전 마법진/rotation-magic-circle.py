import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

n = int(input())

before_state = [int(s) for s in input().strip()]
after_state = [int(s) for s in input().strip()]

dp = [[sys.maxsize] * 11 for _ in range(n)]


def get_min_rotate(idx, rev_rotate_cnt):
    # 지금 idx번째 마법진을 체크할 차례이고 지금까지 반시계로 회전한 횟수가 rev_rotate_cnt일때 원하는 state에 도달하기 위한
    # 최소 회전 횟수는?
    if idx == n:
        return 0
    if dp[idx][rev_rotate_cnt] < sys.maxsize:
        return dp[idx][rev_rotate_cnt]
    cur_diff = (before_state[idx] + rev_rotate_cnt) % 10 - after_state[idx]

    if cur_diff >= 0:
        # 시계 회전
        dp[idx][rev_rotate_cnt] = min(
            dp[idx][rev_rotate_cnt], cur_diff + get_min_rotate(idx + 1, rev_rotate_cnt)
        )

        # 반시계 회전
        dp[idx][rev_rotate_cnt] = min(
            dp[idx][rev_rotate_cnt],
            (10 - cur_diff)
            + get_min_rotate(idx + 1, (rev_rotate_cnt + (10 - cur_diff)) % 10),
        )
    else:
        # 시계 회전
        dp[idx][rev_rotate_cnt] = min(
            dp[idx][rev_rotate_cnt],
            (10 + cur_diff) + get_min_rotate(idx + 1, rev_rotate_cnt),
        )

        # 반시계 회전
        dp[idx][rev_rotate_cnt] = min(
            dp[idx][rev_rotate_cnt],
            -cur_diff + get_min_rotate(idx + 1, (rev_rotate_cnt - cur_diff) % 10),
        )
    return dp[idx][rev_rotate_cnt]


print(get_min_rotate(0, 0))

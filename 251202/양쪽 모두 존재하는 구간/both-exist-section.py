from collections import defaultdict

n, m = map(int, input().split())
nums = list(map(int, input().split()))

total = defaultdict(int)
for x in nums:
    total[x] += 1

# 애초에 전체 배열에 1..m이 다 없으면 답은 -1
if len(total) < m:
    print(-1)
    exit()

window = defaultdict(int)
distinct_in_window = 0            # 윈도우 안에 서로 다른 숫자 개수
full_in_window = 0               # 전체 등장 횟수를 전부 윈도우가 가지고 있는 숫자 개수
ans = float("inf")

r = 0
for l in range(n):
    # 윈도우 [l, r) 가 1..m을 모두 포함할 때까지 r을 오른쪽으로 확장
    while r < n and distinct_in_window < m:
        x = nums[r]
        r += 1

        prev = window[x]
        window[x] += 1

        # 새로 들어온 숫자라면 distinct 개수 증가
        if prev == 0:
            distinct_in_window += 1

        # 이 숫자의 모든 등장 위치가 윈도우 안으로 들어오게 되면 full_in_window++
        if window[x] == total[x]:
            full_in_window += 1

    # 이 시점에서:
    #   - distinct_in_window == m 이면 윈도우 안에 1..m 전부 있음
    #   - full_in_window == 0 이면 지워도 바깥에 각 숫자가 최소 1개는 남아 있음
    if distinct_in_window == m and full_in_window == 0:
        ans = min(ans, r - l)

    # 이제 l을 하나 오른쪽으로 옮기면서 nums[l]을 윈도우에서 제거
    x = nums[l]

    # 제거 전에 이 숫자가 "전체가 다 윈도우에 있었던 상태"였다면, 이제는 아니게 되므로 full_in_window 감소
    if window[x] == total[x]:
        full_in_window -= 1

    window[x] -= 1
    if window[x] == 0:
        distinct_in_window -= 1
        del window[x]

print(ans if ans != float("inf") else -1)

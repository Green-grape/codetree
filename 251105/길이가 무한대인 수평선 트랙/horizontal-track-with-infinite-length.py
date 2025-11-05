from sortedcontainers import SortedSet

n, t = map(int, input().split())

s = SortedSet()

for _ in range(n):
    start_pos, v = map(int, input().split())
    end_pos = start_pos + v * t
    if (
        len(s) == 0 or end_pos > s[-1][0]
    ):  # 더 나중에 들어왔는데 속도도 빠르면 그냥 추가
        s.add((end_pos, start_pos))
    else:
        # 나중에 들어왔는데 속도가 느림 -> 기존애들 중에 겹치면서 더 빠른 애들 제거
        while True:
            last_end_pos, last_start_pos = s[-1]
            if last_end_pos >= end_pos and last_start_pos <= start_pos:
                s.pop()
            else:
                break
        s.add((end_pos, start_pos))

print(len(s))


# 0->3
# 1->7

# 2->11
# 3->9 => # 3->9
# 6->9

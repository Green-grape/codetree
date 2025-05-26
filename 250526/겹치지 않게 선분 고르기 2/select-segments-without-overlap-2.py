import sys

input=sys.stdin.readline

n=int(input())

lines=[]

for _ in range(n):
    lines.append(tuple(map(int, input().split())))

lines.sort(lambda x: (x[0], x[1]))

dp=[[-1]*1001 for _ in range(1001)]

def get_max_not_intersect_lines_cnt(i, cur_max):
    # 현재까지 고른 선분의 최대값이 cur_max이고 i번째부터 선택해서 겹치지 않게 가장 많은 선분의 수를 고르는 방법이 개수는?
    if dp[i][cur_max]!=-1:
        return dp[i][cur_max]
    if i==(n-1):
        return 1 if lines[i][0]>cur_max else 0
    for idx in range(i, n):
        if lines[idx][0]>cur_max:
            dp[i][cur_max]=max(dp[i][cur_max], 1+get_max_not_intersect_lines_cnt(idx, max(cur_max, lines[idx][1])))
    return dp[i][cur_max]

ret=0;
for idx in range(n):
    ret=max(ret, get_max_not_intersect_lines_cnt(idx, 0))
print(ret)
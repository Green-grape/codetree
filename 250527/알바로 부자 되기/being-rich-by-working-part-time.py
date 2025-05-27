import sys

n=int(input())

jobs=[tuple(map(int, input().split())) for _ in range(n)]

jobs.sort(lambda x: (x[0], x[1], -x[2]))

dp=[[-1]*1001 for _ in range(n)]

def find_max_pay(i,cur_end):
    # 현재 i번째까지 알바를 채워서 현재의 마지막 알바일이 cur_end일때 이후에 오는 알바를 통해 얻을 수 있는 최대 금액을 반환
    if dp[i][cur_end]!=-1:
        return dp[i][cur_end]
    if i==(n-1):
        return jobs[i][2] if cur_end<jobs[i][0] else 0
    dp[i][cur_end]=0
    for idx in range(i+1, n):
        if cur_end<jobs[idx][0]:
            dp[i][cur_end]=max(dp[i][cur_end], jobs[idx][2]+find_max_pay(idx, jobs[idx][1]))
    return dp[i][cur_end]

ret=0
for i in range(n):
    ret=max(ret, find_max_pay(i, jobs[i][1])+jobs[i][2])
print(ret)
    
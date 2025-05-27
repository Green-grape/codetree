import sys

n=int(input())

jobs=[tuple(map(int, input().split())) for _ in range(n)]

jobs.sort(lambda x: (x[0], x[1], -x[2]))

dp=[[-1]*n for _ in range(n)]

def find_max_pay(i,cur_end):
    if dp[i][cur_end]!=-1:
        return dp[i][cur_end]
    if i==(n-1):
        return jobs[i][2] if jobs[cur_end][1]<jobs[i][0] else 0
    dp[i][cur_end]=0
    for idx in range(i+1, n):
        if jobs[cur_end][1]<jobs[idx][0]:
            dp[i][cur_end]=max(dp[i][cur_end], jobs[idx][2]+find_max_pay(idx, idx))
    return dp[i][cur_end]

ret=0
for i in range(n):
    ret=max(ret, find_max_pay(i, i)+jobs[i][2])
print(ret)
    
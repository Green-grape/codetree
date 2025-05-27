import sys

n=int(input())

jobs=[tuple(map(int, input().split())) for _ in range(n)]

jobs.sort(lambda x: (x[0], x[1], -x[2]))

def find_max_pay(i,cur_end):
    if i==(n-1):
        return jobs[i][2] if cur_end<jobs[i][0] else 0
    ret=0
    for idx in range(i+1, n):
        if cur_end<jobs[idx][0]:
            ret=max(ret, jobs[idx][2]+find_max_pay(idx, jobs[idx][1]))
    return ret

ret=0
for i in range(n):
    ret=max(ret, find_max_pay(i, jobs[i][1])+jobs[i][2])
print(ret)
    
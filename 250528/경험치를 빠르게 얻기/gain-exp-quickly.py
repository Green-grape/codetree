import sys

input=sys.stdin.readline

n, m=map(int, input().split())

quests=[tuple(map(int, input().split())) for _ in range(n)]

dp=[-1]*(10001) # i시간에 대하여 얻을 수 있는 최대 경험치
dp[0]=0
for quest in quests:
    for t in range(len(dp), 0, -1):
        if t-quest[1]>=0 and dp[t-quest[1]]!=-1:
            dp[t]=max(dp[t], dp[t-quest[1]]+quest[0])

ret=-1
for i in range(len(dp)):
    if dp[i]>=m:
        ret=i
        break
print(ret)


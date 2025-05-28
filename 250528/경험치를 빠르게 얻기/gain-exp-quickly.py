import sys

input=sys.stdin.readline

n, m=map(int, input().split())

quests=[tuple(map(int, input().split())) for _ in range(n)]

dp=[100*n]*(2*m+1)
dp[0]=0
for quest in quests:
    for exp in range(2*m, 0, -1):
        if exp-quest[0]>=0 and dp[exp-quest[0]]!=100*n:
            dp[exp]=min(dp[exp], dp[exp-quest[0]]+quest[1])

ret=min(dp[m:])
print(ret if ret!=100*n else -1)


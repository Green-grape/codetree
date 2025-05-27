import sys

input=sys.stdin.readline

n=int(input())

earns=list(map(int, input().split()))

def find_max_earning(length):
    dp=[-1]*(length+1)
    dp[0]=0
    for cur_len in range(1, length+1):
        for i, earn in enumerate(earns):
                if (cur_len>=i+1) and dp[cur_len-i-1]!=-1:
                    dp[cur_len]=max(dp[cur_len], dp[cur_len-i-1]+earn)
    return dp[length]


print(find_max_earning(n))

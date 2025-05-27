import sys

input=sys.stdin.readline

n, m=map(int, input().split())

num_list=list(map(int, input().split()))

def get_find_min_length(m):
    dp=[10001]*(m+1)
    dp[0]=0
    for num in num_list:
        for cur_val in range(m, num-1, -1):
            dp[cur_val]=min(dp[cur_val], dp[cur_val-num]+1)
    return dp[m] if dp[m]!=10001 else -1

print(get_find_min_length(m))


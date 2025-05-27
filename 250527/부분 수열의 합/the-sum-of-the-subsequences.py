import sys

num_cnt, total_val=map(int, input().split())

num_list=list(map(int, input().split()))

def is_exist_sublist(m):
    dp=[False]*(m+1)
    dp[0]=True
    for num in num_list:
        for val in range(m, num-1, -1):
            dp[val]|=dp[val-num]
    return 'Yes' if dp[m] else 'No'

print(is_exist_sublist(total_val))
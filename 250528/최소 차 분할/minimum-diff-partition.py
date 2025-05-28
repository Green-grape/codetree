import sys

input=sys.stdin.readline

n=int(input())

nums=list(map(int, input().split()))

def get_min_diff():
    # 현재 A그룹의 합이 a일때 이때 b의 값
    dp=[-1]*(1000*n+1)
    total_sum=sum(nums)
    for num in nums:
        dp[num]=total_sum-num
    for val in range(1, len(dp)):
        for num in nums:
            if val>num and dp[val-num]!=-1:
                dp[val]=total_sum-val
    ret=len(dp)
    for val in range(1, len(dp)):
        if dp[val]!=-1:
            ret=min(ret, abs(dp[val]-val))
    return ret

print(get_min_diff())

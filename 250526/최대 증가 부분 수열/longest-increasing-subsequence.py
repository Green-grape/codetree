import sys

input=sys.stdin.readline

n=int(input())

nums=list(map(int, input().split()))

dp=[-1]*n

def find_max_length_of_increasing_list(i):
    # 현재 i번째부터 끝까지 가장 긴 증가부분 수율의 길이를 반환
    if dp[i]!=-1:
        return dp[i]
    if i==(n-1):
        return 1
    dp[i]=1
    for idx in range(i+1, n):
        if nums[i]<nums[idx]:
            dp[i]=max(dp[i], find_max_length_of_increasing_list(idx)+1)
    return dp[i]


print(find_max_length_of_increasing_list(0))
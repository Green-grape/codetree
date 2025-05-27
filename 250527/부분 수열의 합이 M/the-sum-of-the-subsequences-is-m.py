import sys

input=sys.stdin.readline

n, m=map(int, input().split())

num_list=list(map(int, input().split()))

dp=[[10001]*(m+1) for _ in range(n)]

def get_find_min_length(i, cur_val):
    # i+1번째부터 선택해서 부분 수열의 원소의 합이 cur_val이 되는 부분수열의 최소 길이 반환
    if dp[i][cur_val]!=10001:
        return dp[i][cur_val]
    if cur_val==0:
        return 0
    for idx in range(i+1, n):
        if cur_val>=num_list[idx]:
            cand=get_find_min_length(idx, cur_val-num_list[idx])
            if cand!=10001:
                dp[i][cur_val]=min(dp[i][cur_val], cand+1)
    return dp[i][cur_val]

ret=10001
for i, num in enumerate(num_list):
    if m>=num:
        ret=min(ret, 1+get_find_min_length(i, m-num))
print(ret if ret!=10001 else -1)
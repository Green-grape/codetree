n=int(input())

boards=[list(map(int, input().split())) for _ in range(n)]

visit=[0]*n

ret=-1
def find_min_value_of_selected_col(idx, cur_val):
    global ret
    if sum(visit)==n:
        ret=max(ret, cur_val)
        return
    for i in range(n):
        if visit[i]==0:
            visit[i]=1
            find_min_value_of_selected_col(idx+1, min(cur_val, boards[idx][i]))
            visit[i]=0

find_min_value_of_selected_col(0, 10001)
print(ret)
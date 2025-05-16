n=int(input())

boards=[list(map(int, input().split())) for _ in range(n)]

selected_cols=[]
ret=0

def find_max_value(idx, cur_val):
    global ret
    if idx==n:
        ret=max(ret, cur_val)
        return;
    for i in range(n):
        if i not in selected_cols:
            selected_cols.append(i)
            find_max_value(idx+1, cur_val+boards[idx][i])
            selected_cols.pop()

find_max_value(0, 0)
print(ret)

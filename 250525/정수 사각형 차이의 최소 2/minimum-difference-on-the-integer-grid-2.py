import sys

input=sys.stdin.readline

n=int(input())

boards=[list(map(int, input().split())) for _ in range(n)]

dp=[[None]*n for _ in range(n)]

move_dirs=[(-1, 0), (0, -1)]
def find_min_max_in_path(i, j):
    # i, j까지의 경로까지의 (최소, 최대) 쌍을 저장
    if dp[i][j]!=None:
        return dp[i][j]
    if i==0 and j==0:
        return [(boards[i][j], boards[i][j])]
    cand=[]
    for dy, dx in move_dirs:
        y=i+dy
        x=j+dx
        if 0<=x<n and 0<=y<n:
            path_list=find_min_max_in_path(y, x)
            temp_list=[]
            for path in path_list:
                before_min, before_max=path
                cur_min, cur_max=(min(before_min, boards[i][j]), max(before_max, boards[i][j]))
                temp_list.append((cur_min, cur_max))
            temp_list.sort(lambda x: (x[0], x[1]))
            cur_list=[]
            for temp in temp_list:
                if len(cur_list)==0:
                    cur_list.append(temp)
                elif cur_list[-1][0]!=temp_list[0]:
                   cur_list.append(temp)
            cand.extend(cur_list)
    dp[i][j]=cand
    return dp[i][j]

cand_list=find_min_max_in_path(n-1, n-1)
ret=100
for cur_min, cur_max in cand_list:
    ret=min(ret, cur_max-cur_min)
print(ret)
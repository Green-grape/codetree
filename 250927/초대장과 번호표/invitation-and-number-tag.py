# 사람 -> 그룹 리스트 맵핑 (dict)
# 그룹 -> 사람 리스트 맵핑 (dict) -> check용으로 초대권 O, X 따로 관리 -> set이 좋을듯

from collections import defaultdict

n, g=map(int, input().split())

p_to_g=defaultdict(list)
g_to_p={}

next_p=[1]
for i in range(g):
    p_list=list(map(int, input().split()))[1:]
    for p in p_list:
        p_to_g[p].append(i)
    if len(p_list)==1 and p_list[0]!=1:
        next_p.append(p_list[0])
    g_to_p[i]=set(p_list)
        
ret=0
while True:
    cand_p=[]
    for tar_p in next_p:
        tar_g_list=p_to_g[tar_p]
        for tar_g in tar_g_list:
            tar_g_set=g_to_p[tar_g]
            tar_g_set.remove(tar_p)
            if len(tar_g_set)==1 and not (list(tar_g_set)[0] in next_p):
                cand_p.append(list(tar_g_set)[0])
    ret+=len(next_p)
    if len(cand_p)==0: break
    next_p=cand_p.copy()

print(ret)

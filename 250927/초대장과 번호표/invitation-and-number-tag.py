from collections import defaultdict

n, g = map(int, input().split())

p_to_g = defaultdict(list)
g_to_p = {}

next_p = [1]
for i in range(g):
    p_list = list(map(int, input().split()))[1:]
    for p in p_list:
        p_to_g[p].append(i)
    if len(p_list) == 1 and p_list[0] != 1:
        next_p.append(p_list[0])
    g_to_p[i] = set(p_list)

ret = 0
checked_p = set()
while True:
    cand_p = []
    for tar_p in next_p:
        tar_g_list = p_to_g[tar_p]
        for tar_g in tar_g_list:
            tar_g_set = g_to_p[tar_g]
            tar_g_set.remove(tar_p)
            if len(tar_g_set) == 1 and not (list(tar_g_set)[0] in checked_p):
                cand_p.append(list(tar_g_set)[0])
                checked_p.add(list(tar_g_set)[0])
    ret += len(next_p)
    if len(cand_p) == 0:
        break
    next_p = cand_p.copy()

print(ret)
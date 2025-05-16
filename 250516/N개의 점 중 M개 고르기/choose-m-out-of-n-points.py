n, m=map(int, input().split())

cords=[tuple(map(int, input().split())) for _ in range(n)]

dist=[[0]*n for _ in range(n)]

ret=0
for i in range(n):
    for j in range(n):
        dist[i][j]=(cords[i][0]-cords[j][0])**2+(cords[i][1]-cords[j][1])**2
        ret=max(ret, dist[i][j])

cur_cord_indices=[]
def find_min_dist(idx, cur_val):
    global ret
    if len(cur_cord_indices)==m:
        ret=min(ret, cur_val)
        return
    if idx>=n:
        return
    cand_val=cur_val
    for cur_cord_idx in cur_cord_indices:
        cand_val=max(cand_val, dist[idx][cur_cord_idx])
    cur_cord_indices.append(idx)
    find_min_dist(idx+1, cand_val)
    cur_cord_indices.pop()
    find_min_dist(idx+1, cur_val)

find_min_dist(0, 0)
print(ret)
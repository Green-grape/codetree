import os

data=os.read(0, os.fstat(0).st_size).splitlines()
ptr=0

n, m=map(int, data[ptr].decode().split())
ptr+=1

visit=[False]*n
edges=[[] for _ in range(n)]

for i in range(m):
    node1, node2=map(int, data[ptr].decode().split())
    ptr+=1
    edges[node1-1].append(node2-1)
    edges[node2-1].append(node1-1)


def dfs(i):
    if visit[i]:
        return
    visit[i]=True
    for next_node in edges[i]:
        dfs(next_node)

dfs(0)
print(sum(visit)-1)
    
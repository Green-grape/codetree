n=int(input())

d={}
MAX=1e9
for _ in range(n):
    x, y=map(int, input().split())
    d[x]=min(d.get(x, MAX), y)

print(sum(list(d.values())))
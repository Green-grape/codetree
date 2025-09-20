num=int(input())
d={}
for _ in range(num):
    s=input()
    if s in d:
        d[s]+=1
    else:
        d[s]=1

print(max(list(d.values())))
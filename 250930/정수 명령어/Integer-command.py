from sortedcontainers import SortedSet

t=int(input())

for _ in range(t):
    k=int(input())
    s=SortedSet()
    for _ in range(k):
        inputs=input().split()
        cmd, val=inputs[0], int(inputs[1])
        if cmd=='I': s.add(val)
        else:
            if len(s)==0:
                continue
            if val==1:
                s.remove(s[-1])
            else:
                s.remove(s[0])

    if len(s)==0:
        print('EMPTY')
    else:
        print(f"{s[-1]} {s[0]}")

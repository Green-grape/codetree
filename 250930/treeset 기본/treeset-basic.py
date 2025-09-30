from sortedcontainers import SortedSet

s=SortedSet()

n=int(input())

for _ in range(n):
    inputs=input().split()
    if len(inputs)==2:
        cmd, val=inputs[0], int(inputs[1])
    else:
        cmd=inputs[0]

    if cmd=="add":
        s.add(val)
    elif cmd=='remove':
        s.remove(val)
    elif cmd=='find':
        print(str(val in s).lower())
    elif cmd=='lower_bound':
        idx=s.bisect_left(val)
        print(s[idx] if idx<len(s) and s[idx]>=val else 'None')
    elif cmd=="upper_bound":
        idx=s.bisect_right(val)
        print(s[idx] if idx<len(s) and s[idx]>val else 'None')
    elif cmd=='largest':
        print(s[-1] if len(s)>0 else 'None')
    else:
        print(s[0] if len(s)>0 else 'None')    

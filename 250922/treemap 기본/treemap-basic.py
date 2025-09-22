n=int(input())

d={}
for _ in range(n):
    inputs=input().split()
    if len(inputs)==3: # add
        d[int(inputs[1])]=inputs[2]
    elif len(inputs)==2: # find or remove
        if inputs[0]=='remove': 
            d.pop(int(inputs[1]))
        else:
            print(d.get(int(inputs[1]), 'None'))
    else:
        if len(d)==0: print('None')
        else: print(' '.join([d[k] for k in sorted(d.keys())]))


import itertools

n, m=map(int, input().split())

a_group_list=[input() for _ in range(n)]
b_group_list=[input() for _ in range(n)]

ret=0
for (i1, i2, i3) in itertools.combinations(range(m), 3):
    a_set=set()
    b_set=set()
    con=False
    for i in range(n):
        a_key=a_group_list[i][i1]+a_group_list[i][i2]+a_group_list[i][i3]
        b_key=b_group_list[i][i1]+b_group_list[i][i2]+b_group_list[i][i3]
        a_set.add(a_key)
        b_set.add(b_key)
        if b_key in a_set or a_key in b_set:
            con=True
            break
    if con:
        continue
    ret+=1

print(ret)
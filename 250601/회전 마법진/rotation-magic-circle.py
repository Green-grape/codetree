import sys

input=sys.stdin.readline

n=int(input())

before_state=[int(s) for s in input()[:-1]]
after_state=[int(s) for s in input()[:-1]]

ret=sys.maxsize
for rev in range(10):
    temp=rev
    for i in range(n):
        temp+=abs((before_state[i]+rev)%10-after_state[i])
    ret=min(ret, temp)
print(ret)
        


# 0 1 2...9
# 1 2 ... 9 0
# 9 0 1 2 ...8

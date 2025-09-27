na, nb=map(int, input().split())

set_a=set(list(map(int, input().split())))
set_b=set(list(map(int, input().split())))

print(len((set_a-set_b) | (set_b-set_a)))
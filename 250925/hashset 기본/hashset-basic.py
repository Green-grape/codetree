n=int(input())

my_set=set()

for _ in range(n):
    com, num=map(str, input().split())
    if com=='add':
        my_set.add(num)
    elif com=='remove':
        my_set.remove(num)
    else:
        print(str(num in my_set).lower())    
n=int(input())

cache=[0]*(n+1)
def find_fill_rectangle(n):
    if cache[n]!=0:
        return cache[n]
    if n==1:
        cache[n]=1
    elif n==2:
        cache[n]=2
    else:
        cache[n]=((find_fill_rectangle(n-1)%10007)+(find_fill_rectangle(n-2)%10007))%10007
    return cache[n]

print(find_fill_rectangle(n))
    
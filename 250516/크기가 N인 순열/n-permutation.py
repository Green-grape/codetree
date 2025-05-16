n=int(input())

cur_nums=[]

def permutation():
    if len(cur_nums)==n:
        print(" ".join([str(cur_num) for cur_num in cur_nums]))
        return;
    for i in range(1, n+1):
        if i not in cur_nums:
            cur_nums.append(i)
            permutation()
            cur_nums.pop()

permutation()
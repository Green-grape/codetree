n=int(input())

cache=[[0]*(n+2) for _ in range(n+2)]
def find_bst_cnt(start_num, end_num):
    # [start_num, end_num]로 만들수 있는 Binary Search Tree의 개수를 반환한다.
    if cache[start_num][end_num]!=0:
        return cache[start_num][end_num]
    if start_num>=end_num:
        return 1
    for i in range(start_num, end_num+1):
        # i를 기준으로 split
        cache[start_num][end_num]+=find_bst_cnt(start_num, i-1)*find_bst_cnt(i+1, end_num)
    return cache[start_num][end_num]

print(find_bst_cnt(1, n))
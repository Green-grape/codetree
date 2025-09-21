import gc
n=int(input())

arr1=map(int, input().split())
arr2=map(int, input().split())
arr3=map(int, input().split())
arr4=map(int, input().split())

def make_cnt_dict(arr):
    ret={}
    for num in arr:
        if num in ret: ret[num]=1+ret[num]
        else: ret[num]=1
    return ret

arr1_cnt_dict=make_cnt_dict(arr1)
del arr1
arr2_cnt_dict=make_cnt_dict(arr2)
del arr2
arr3_cnt_dict=make_cnt_dict(arr3)
del arr3
arr4_cnt_dict=make_cnt_dict(arr4)
del arr4
gc.collect()

def merge_cnt_dict(d1, d2):
    ret={}
    for k1, v1 in d1.items():
        for k2, v2 in d2.items():
            if k1+k2 in ret:
                ret[k1+k2]+=v1*v2
            else:
                ret[k1+k2]=v1*v2
    return ret


ret=merge_cnt_dict(arr1_cnt_dict, arr2_cnt_dict)
del arr1_cnt_dict
del arr2_cnt_dict
gc.collect()
ret=merge_cnt_dict(ret, arr3_cnt_dict)
del arr3_cnt_dict 
gc.collect()
ret=merge_cnt_dict(ret, arr4_cnt_dict)
print(ret[0])


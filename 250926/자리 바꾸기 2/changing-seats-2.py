n, k = map(int, input().split())

pos_record = [set([i]) for i in range(n)]  # idx번째 사람의 앉은 기록
cur_pos = [i for i in range(n)]  # i번째 자리에 있는 사람의 idx

change_seq = []
for _ in range(k):
    a, b = map(int, input().split())
    change_seq.append((a - 1, b - 1))


for i in range(3 * k):
    a, b = change_seq[i % k]
    temp = cur_pos[a]
    cur_pos[a] = cur_pos[b]
    cur_pos[b] = temp
    pos_record[cur_pos[a]].add(b)
    pos_record[cur_pos[b]].add(a)

ret = "\n".join([str(len(c)) for c in pos_record])
print(ret)

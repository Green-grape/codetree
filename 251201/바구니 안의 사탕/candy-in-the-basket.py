# Please write your code here.
n, k = map(int, input().split())

candy_pos = []
for _ in range(n):
    x, y = map(int, input().split())  # 사탕 개수, 좌표
    candy_pos.append((y, x))  # (y, x) 형태로 저장

candy_pos.sort()  # y좌표 기준으로 정렬
compressed_candy_pos = []  # 중복된 y좌표의 경우 하나로 압축
prev_y = -1
prev_candy_sum = 0
for y, x in candy_pos:
    if y == prev_y:
        prev_candy_sum += x
        compressed_candy_pos[-1] = (prev_y, prev_candy_sum)
    else:
        compressed_candy_pos.append((y, x))
        prev_y = y
        prev_candy_sum = x

MAX_POS = 1000000
cur_candy_sum = 0
j = 0
i = 0
max_candy_sum = 0
for center in range(1, MAX_POS + 1):
    while j < len(compressed_candy_pos) and compressed_candy_pos[j][0] <= center + k:
        if compressed_candy_pos[j][0] >= center - k:
            cur_candy_sum += compressed_candy_pos[j][1]
        j += 1
    max_candy_sum = max(max_candy_sum, cur_candy_sum)
    while i < len(compressed_candy_pos) and compressed_candy_pos[i][0] == center - k:
        cur_candy_sum -= compressed_candy_pos[i][1]
        i += 1
print(max_candy_sum)

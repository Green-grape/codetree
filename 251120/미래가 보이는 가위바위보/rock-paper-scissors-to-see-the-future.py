n = int(input())

target_cards = []
for _ in range(n):
    target_cards.append(input().strip())


def is_win(c1, c2):
    if (
        (c1 == "H" and c2 == "S")
        or (c1 == "S" and c2 == "P")
        or (c1 == "P" and c2 == "H")
    ):
        return True
    return False


# 주먹을 내는 경우의 수
h_left_sums = [0] * n
h_right_sums = [0] * n

s_left_sums = [0] * n
s_right_sums = [0] * n

p_left_sums = [0] * n
p_right_sums = [0] * n


h_left_sum = 0
s_left_sum = 0
p_left_sum = 0
for i in range(n):
    card = target_cards[i]
    h_left_sum += 1 if is_win("H", card) else 0
    s_left_sum += 1 if is_win("S", card) else 0
    p_left_sum += 1 if is_win("P", card) else 0

    h_left_sums[i] = h_left_sum
    s_left_sums[i] = s_left_sum
    p_left_sums[i] = p_left_sum

h_right_sum = 0
s_right_sum = 0
p_right_sum = 0
for i in range(n - 1, -1, -1):
    card = target_cards[i]
    h_right_sum += 1 if is_win("H", card) else 0
    s_right_sum += 1 if is_win("S", card) else 0
    p_right_sum += 1 if is_win("P", card) else 0

    h_right_sums[i] = h_right_sum
    s_right_sums[i] = s_right_sum
    p_right_sums[i] = p_right_sum

max_win_count = 0
for c in range(1, n):
    max_win_count = max(
        max_win_count,
        h_left_sums[c - 1] + h_right_sums[c],
        h_left_sums[c - 1] + s_right_sums[c],
        h_left_sums[c - 1] + p_right_sums[c],
        s_left_sums[c - 1] + h_right_sums[c],
        s_left_sums[c - 1] + s_right_sums[c],
        s_left_sums[c - 1] + p_right_sums[c],
        p_left_sums[c - 1] + h_right_sums[c],
        p_left_sums[c - 1] + s_right_sums[c],
        p_left_sums[c - 1] + p_right_sums[c],
    )
print(max_win_count)

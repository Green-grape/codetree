s, k = input().split()

count_dict = {}
for c in range(26):
    count_dict[chr(c + ord("a"))] = 0

k = int(k)

j = 0


def get_diff_char():
    ret = 0
    for k, v in count_dict.items():
        if v > 0:
            ret += 1
    return ret


max_substr_len = 0
for i in range(len(s)):
    while j < len(s) and get_diff_char() <= k:
        count_dict[s[j]] += 1
        if get_diff_char() > k:
            count_dict[s[j]] -= 1
            break
        j += 1
    max_substr_len = max(max_substr_len, j - i)
    count_dict[s[i]] -= 1
print(max_substr_len)

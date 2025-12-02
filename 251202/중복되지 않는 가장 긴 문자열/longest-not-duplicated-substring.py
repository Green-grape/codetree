s = input()

j = 0
isvisited = [0] * 26
max_non_dup_len = 0
for i in range(len(s)):
    while j < len(s) and isvisited[ord(s[j]) - ord("a")] == 0:
        isvisited[ord(s[j]) - ord("a")] = 1
        j += 1
    max_non_dup_len = max(max_non_dup_len, j - i)
    isvisited[ord(s[i]) - ord("a")] = 0
print(max_non_dup_len)

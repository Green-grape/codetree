s = input()

# suc_left_brackets = [0] * len(s)  # suc_left_brackets[i]=0~i까지 (( 의 개수
suc_right_brackets = [0] * len(s)  # suc_right_brackets[i]=i~끝까지 )) 의 개수

for i in range(len(s) - 2, -1, -1):
    if s[i : i + 2] == "))":
        suc_right_brackets[i] = suc_right_brackets[i + 1] + 1
    else:
        suc_right_brackets[i] = suc_right_brackets[i + 1]

ret = 0
for i in range(1, len(s)):
    if s[i - 1 : i + 1] == "((":
        ret += suc_right_brackets[i]
print(ret)

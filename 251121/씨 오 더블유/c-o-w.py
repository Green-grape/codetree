n = int(input())

s = input()

c_count_left = [0] * n
w_count_right = [0] * n

for i in range(n):
    c_count_left[i] = (
        c_count_left[i - 1] + (1 if s[i] == "C" else 0)
        if i > 0
        else (1 if s[i] == "C" else 0)
    )

for i in range(n - 1, -1, -1):
    w_count_right[i] = (
        w_count_right[i + 1] + (1 if s[i] == "W" else 0)
        if i < n - 1
        else (1 if s[i] == "W" else 0)
    )

ret = 0
for i in range(n):
    if s[i] == "O":
        ret += c_count_left[i] * w_count_right[i]
print(ret)

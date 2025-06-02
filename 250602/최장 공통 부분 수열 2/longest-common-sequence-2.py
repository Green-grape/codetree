str_a = input()
str_b = input()


la = len(str_a)
lb = len(str_b)


dp = [[-1] * (lb + 1) for _ in range(la + 1)]
dp[0][0] = 0

for i in range(la + 1):
    for j in range(lb + 1):
        if dp[i][j] == -1:
            continue
        if i < la and j < lb and str_a[i] == str_b[j]:
            dp[i + 1][j + 1] = max(dp[i + 1][j + 1], 1 + dp[i][j])

        if i < la:
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
        if j < lb:
            dp[i][j + 1] = max(dp[i][j + 1], dp[i][j])

visit = [[False] * (lb + 1) for _ in range(la + 1)]
moves = [[-1, -1], [-1, 0], [0, -1]]
queue = [(la, lb)]
visit[la][lb] = True

ret = []
i, j = la, lb
while i > 0 and j > 0:
    if str_a[i - 1] == str_b[j - 1]:
        ret.append(str_a[i - 1])
        i -= 1
        j -= 1
    elif dp[i - 1][j] >= dp[i][j - 1]:
        i -= 1
    else:
        j -= 1

print("".join(ret[::-1]))

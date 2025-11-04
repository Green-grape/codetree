from sortedcontainers import SortedSet

n = int(input())
s = SortedSet()

for _ in range(n):
    num, score = map(int, input().split())
    s.add((score, num))

m = int(input())
for _ in range(m):
    input_list = input().split()
    if input_list[0] == "rc":
        x = int(input_list[1])
        if x == 1:
            print(s[-1][1])
        else:
            print(s[0][1])
    else:
        cmd, num, score = input_list
        if cmd == "ad":
            s.add((int(score), int(num)))
        elif cmd == "sv":
            s.discard((int(score), int(num)))

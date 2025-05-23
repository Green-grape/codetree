n = int(input())

cache = [-1] * (n + 1)


def get_move_cnt(n):
    if cache[n] != -1:
        return cache[n]
    if n <= 1:
        return 0
    if n == 2 or n == 3:
        return 1
    cache[n] = (get_move_cnt(n - 2) % 10007 + get_move_cnt(n - 3) % 10007) % 10007
    return cache[n]


print(get_move_cnt(n) % 10007)

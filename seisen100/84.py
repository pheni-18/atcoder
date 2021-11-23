# https://atcoder.jp/contests/joi2012ho/tasks/joi2012ho4

# 累積和


def inp(to_int=True):
    if not type(to_int) == bool:
        raise Exception()
    l = input().split()
    return list(map(lambda x: int(x), l)) if to_int else l


def inp_one(to_int=True):
    if not type(to_int) == bool:
        raise Exception()
    s = input()
    return int(s) if to_int else s


def main():
    N, M = inp()
    abxl = []
    for _ in range(M):
        a, b, x = inp()
        a -= 1
        b -= 1
        abxl.append([a, b, x])

    map_ = [[0] * (N + 2) for _ in range(N + 2)]
    for a, b, x in abxl:
        map_[a][b] += 1
        map_[a][b + 1] -= 1
        map_[a + x + 1][b] -= 1
        map_[a + x + 1][b + x + 2] += 1
        map_[a + x + 2][b + 1] += 1
        map_[a + x + 2][b + x + 2] -= 1

    # left -> right
    for i in range(N + 2):
        for j in range(1, N + 2):
            map_[i][j] += map_[i][j - 1]

    # upper right -> bottom left
    for i in range(1, N + 2):
        for j in reversed(range(N + 1)):
            map_[i][j] += map_[i - 1][j]

    # upper left -> bottom right
    for i in range(1, N + 2):
        for j in range(1, N + 2):
            map_[i][j] += map_[i - 1][j - 1]

    ans = 0
    for i in range(N + 2):
        for j in range(N + 2):
            if map_[i][j] > 0:
                ans += 1

    print(ans)
            

if __name__ == '__main__':
    main()

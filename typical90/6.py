# ☆5

# 辞書順、貪欲法


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
    N, K = inp()
    S = inp_one(False)

    map_s2i = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}
    map_i2s = {}
    for k, v in map_s2i.items():
        map_i2s[v] = k

    ll = [[-1] * 26 for _ in range(N + 1)]
    for i in range(N):
        c = S[N - i - 1]
        for j in range(26):
            if map_s2i[c] == j:
                ll[N - i - 1][j] = N - i
            else:
                ll[N - i - 1][j] = ll[N - i][j]

    ansl = []
    prev = -1
    for i in range(K):
        for j in range(26):
            idx = ll[prev + 1][j]
            if idx == -1:
                continue
            if N - (idx - 1) >= K - i:
                ansl.append(map_i2s[j])
                prev = idx - 1
                break

    print(''.join(ansl))


if __name__ == '__main__':
    main()

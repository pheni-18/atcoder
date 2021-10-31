# https://atcoder.jp/contests/joi2014yo/submissions/8689705

# ダイクストラ法

# TODO

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
    cubs = [[]]
    for i in range(N):
        cubs.append(inp())

    to = [[] for _ in range(N + 1)]
    for _ in range(K):
        a, b = inp()
        to[a].append(b)
        to[b].append(a)


if __name__ == '__main__':
    main()

# https://atcoder.jp/contests/joi2008yo/tasks/joi2008yo_f

# ダイクストラ法


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
    info_l = [inp() for _ in range(K)]

    to = [[] for _ in range(N + 1)]
    for info in info_l:
        if info[0] == 1:
            c, d, e = info[1:]
            to[c].append([d, e])
            to[d].append([c, e])
            continue

        a, b = info[1:]
        dist = [float('inf')] * (N + 1)
        used = [False] * (N + 1)
        dist[a] = 0
        for _ in range(N):
            min_d = float('inf')
            min_u = -1
            for i in range(1, N + 1):
                if not used[i] and dist[i] < min_d:
                    min_u = i
                    min_d = dist[i]

            if min_u == -1:
                continue

            for v, d in to[min_u]:
                dist[v] = min(dist[v], dist[min_u] + d)

            used[min_u] = True

        if dist[b] == float('inf'):
            print(-1)
        else:
            print(dist[b])


if __name__ == '__main__':
    main()

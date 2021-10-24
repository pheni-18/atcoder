# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_1_A&lang=ja

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
    import heapq

    V, E, r = inp()
    to = [[] for _ in range(V)]
    for _ in range(E):
        s, t, d = inp()
        to[s].append((t, d))

    dist = [float('inf')] * V
    used = [False] * V
    q = []
    heapq.heappush(q, [0, r])
    dist[r] = 0

    while len(q) > 0:
        d, u = heapq.heappop(q)
        if used[u]:
            continue

        dist[u] = d

        for t, d_ in to[u]:
            heapq.heappush(q, [d + d_, t])

        used[u] = True

    for d in dist:
        if d == float('inf'):
            print('INF')
        else:
            print(d)


if __name__ == '__main__':
    main()

# https://atcoder.jp/contests/joi2016yo/tasks/joi2016yo_e

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
    from collections import deque
    import heapq

    N, M, K, S = inp()
    P, Q = inp()
    cl = [inp_one() for _ in range(K)]
    cs = set(cl)

    to = [[] for _ in range(N + 1)]
    for _ in range(M):
        a, b = inp()
        to[a].append(b)
        to[b].append(a)

    dq = deque(cl)
    dist = [-1] * (N + 1)
    for v in cl:
        dist[v] = 0
    while dq:
        u = dq.popleft()
        for v in to[u]:
            if not dist[v] == -1:
                continue

            dist[v] = dist[u] + 1
            dq.append(v)

    cost = [P] * (N + 1)
    for v in range(1, N + 1):
        if dist[v] <= S:
            cost[v] = Q
        if v in cs:
            cost[v] = float('inf')
        if v == 1 or v == N:
            cost[v] = 0

    used = [False] * (N + 1)
    q = []
    heapq.heappush(q, [0, 1])

    total_cost = [float('inf')] * (N + 1)

    while len(q) > 0:
        d, u = heapq.heappop(q)
        if used[u]:
            continue

        total_cost[u] = d

        for v in to[u]:
            if v in cs:
                continue

            heapq.heappush(q, [d + cost[v], v])

        used[u] = True

    print(total_cost[-1])


if __name__ == '__main__':
    main()

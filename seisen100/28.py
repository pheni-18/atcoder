# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_11_C&lang=ja

# BFS


def inp(to_int=True):
    if not type(to_int) == bool:
        raise Exception()
    l = input().split()
    return list(map(lambda x: int(x), l)) if to_int else l


def main():
    from collections import deque

    n = inp()[0]
    to = [[] for _ in range(n)]
    for i in range(n):
        l = inp()
        if l[1] == 0:
            continue
        to_ = list(map(lambda x: x - 1, l[2:]))
        to[i].extend(to_)

    dist = [-1] * n
    dist[0] = 0

    dq = deque()
    dq.append(0)
    while dq:
        u = dq.popleft()
        for v in to[u]:
            if not dist[v] == -1:
                continue

            dist[v] = dist[u] + 1
            dq.append(v)

    for i in range(n):
        print(i + 1, dist[i])


if __name__ == '__main__':
    main()

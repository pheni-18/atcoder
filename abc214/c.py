def inp(to_int=True):
    if not type(to_int) == bool:
        raise Exception()
    l = input().split()
    return list(map(lambda x: int(x), l)) if to_int else l


def main():
    import heapq
    n = inp()[0]
    s = inp()
    t = inp()
    h = []
    for i in range(n):
        heapq.heappush(h, (t[i], i))

    checked = [False] * n
    ansl = [v for v in t]
    cnt = 0

    while True:
        v, i = heapq.heappop(h)

        if not checked[i]:
            checked[i] = True
            cnt += 1

        ne = i + 1
        if ne == n:
            ne = 0

        if v + s[i] < ansl[ne]:
            ansl[ne] = v + s[i]
            heapq.heappush(h, (v + s[i], ne))

        if cnt == n:
            break

    for ans in ansl:
        print(ans)


if __name__ == '__main__':
    main()

def inp(to_int=True):
    if not type(to_int) == bool:
        raise Exception()
    l = input().split()
    return list(map(lambda x: int(x), l)) if to_int else l


def main():
    n, k = inp()
    cl = inp()

    l = []
    colors = {}
    for i in range(k):
        l.append(cl[i])
        try:
            colors[cl[i]] += 1
        except KeyError as e:
            colors[cl[i]] = 1

    cnt = len(set(l))
    ans = cnt

    for i in range(1, n - k + 1):
        a = cl[i - 1]
        colors[a] -= 1
        if colors[a] == 0:
            cnt -= 1

        b = cl[i + k - 1]
        try:
            colors[b] += 1
            if colors[b] == 1:
                cnt += 1
        except KeyError as e:
            cnt += 1
            colors[b] = 1

        ans = max(ans, cnt)

    print(ans)


if __name__ == '__main__':
    main()

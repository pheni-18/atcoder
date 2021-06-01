def inp(to_int=True):
    if not type(to_int) == bool:
        raise Exception()
    l = input().split()
    return list(map(lambda x: int(x), l)) if to_int else l


def inps(n, to_int=True):
    if not type(n) == int:
        raise Exception()
    return [inp(to_int) for _ in [0] * n]


def main():
    n = inp()[0]
    h = inp()

    ans = 'Yes'
    for i in range(n):
        if i == 0:
            if h[i] >= 2:
                h[i] -= 1
            continue

        if h[i] > h[i - 1]:
            h[i] -= 1

        if h[i - 1] > h[i]:
            ans = 'No'
            break

    print(ans)

if __name__ == '__main__':
    main()

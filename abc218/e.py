def inp(to_int=True):
    if not type(to_int) == bool:
        raise Exception()
    l = input().split()
    return list(map(lambda x: int(x), l)) if to_int else l


def main():
    n, m = inp()
    abcl = []
    stock = [0] * (n + 1)
    for _ in range(m):
        a, b, c = inp()
        abcl.append([a, b, c])
        stock[a] += 1
        stock[b] += 1

    ans = 0
    abcl = sorted(abcl, key=lambda x: x[2], reverse=True)
    for a, b, c in abcl:
        if c <= 0:
            break

        if stock[a] > 1 and stock[b] > 1:
            ans += c
            stock[a] -= 1
            stock[b] -= 1

    print(ans)


if __name__ == '__main__':
    main()

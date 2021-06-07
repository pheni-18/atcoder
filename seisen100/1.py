# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_7_B&lang=ja

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
    inputl = []
    while True:
        n, x = inp()
        if n == 0 and x == 0:
            break
        inputl.append([n, x])

    for n, x in inputl:
        ans = 0
        for i in range(1, n + 1):
            for j in range(i + 1, n + 1):
                for k in range(j + 1, n + 1):
                    if i + j + k == x:
                        ans += 1

        print(ans)


if __name__ == '__main__':
    main()

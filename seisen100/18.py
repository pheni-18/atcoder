# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_4_B&lang=ja

# 二分探索

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
    s = inp()
    t = inp()[0]
    q = inp()

    s.append(1001001001)
    ans = 0
    for i in range(t):
        x = q[i]
        left = 0
        right = n
        while left + 1 < right:
            cur = (left + right) // 2
            if x >= s[cur]:
                left = cur
            else:
                right = cur

        if s[left] == x:
            ans += 1

    print(ans)


if __name__ == '__main__':
    main()

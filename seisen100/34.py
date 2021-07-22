# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_10_A&lang=ja

# ナップサック DP

def inp(to_int=True):
    if not type(to_int) == bool:
        raise Exception()
    l = input().split()
    return list(map(lambda x: int(x), l)) if to_int else l


def main():
    n = inp()[0]

    memos = [-1 for _ in range(n + 1)]
    memos[0] = 1
    memos[1] = 1

    def dfs(u):
        if u > n:
            return

        v = memos[u - 1] + memos[u - 2]
        memos[u] = v
        dfs(u + 1)

    dfs(2)

    print(memos[n])


if __name__ == '__main__':
    main()

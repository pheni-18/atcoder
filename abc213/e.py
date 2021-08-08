def inp(to_int=True):
    if not type(to_int) == bool:
        raise Exception()
    l = input().split()
    return list(map(lambda x: int(x), l)) if to_int else l


def main():
    h, w = inp()
    sll = []
    for _ in range(h):
        sll.append(list(inp(False)[0]))

    dp = [[3 * (10 ** 5)] * w for _ in range(h)]
    dp[0][0] = 0

    for i in range(h):
        for j in range(w):


if __name__ == '__main__':
    main()

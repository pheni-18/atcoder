# https://atcoder.jp/contests/joi2013ho/tasks/joi2013ho1

# 連長圧縮


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
    N = inp_one()
    lights = inp()

    counts = [1]
    prev = lights[0]
    for i in range(1, N):
        if prev == lights[i]:
            counts.append(1)
        else:
            counts[-1] += 1
        prev = lights[i]

    len_counts = len(counts)
    if len_counts <= 2:
        print(sum(counts))
        return

    ans = 0
    for i in range(2, len_counts):
        ans = max(ans, sum(counts[i-2:i+1]))

    print(ans)


if __name__ == '__main__':
    main()

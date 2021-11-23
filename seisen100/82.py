# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=2013

# 累積和


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
    nl = []
    trainsl = []
    while True:
        n = inp_one()
        if n == 0:
            break

        nl.append(n)
        trains = []
        for _ in range(n):
            train = inp(False)
            trains.append(train)

        trainsl.append(trains)

    for i in range(len(nl)):
        n = nl[i]
        trains = trainsl[i]

        S = 86400 + 1
        map_ = [0] * S
        for train in trains:
            start, end = train
            h, m, s = start.split(':')
            s_sec = int(h) * 3600 + int(m) * 60 + int(s)
            h, m, s = end.split(':')
            e_sec = int(h) * 3600 + int(m) * 60 + int(s)
            map_[s_sec] += 1
            map_[e_sec] -= 1

        for i in range(1, S):
            map_[i] += map_[i - 1]

        print(max(map_))


if __name__ == '__main__':
    main()

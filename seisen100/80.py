# https://atcoder.jp/contests/gigacode-2019/tasks/gigacode_2019_d

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
    H, W, K, V = inp()
    all = [[0] * (W + 1)]
    for _ in range(H):
        al = inp()
        all.append([0] + al)

    map_ = [[0] * (W + 1) for _ in range(H + 1)]
    for i in range(1, H + 1):
        for j in range(1, W + 1):
            a = all[i][j]
            map_[i][j] = map_[i - 1][j] + map_[i][j - 1] - map_[i - 1][j - 1] + a
    
    ans = 0
    for p1 in range(1, H + 1):
        for q1 in range(1, W + 1):
            for p2 in range(p1, H + 1):
                for q2 in range(q1, W + 1):
                    area = (p2 - p1 + 1) * (q2 - q1 + 1)
                    if area <= ans:
                        continue
                
                    cost = area * K
                    cost += map_[p2][q2] - map_[p1 - 1][q2] - map_[p2][q1 - 1] + map_[p1 - 1][q1 - 1]
                    if cost <= V:
                        ans = area
    
    print(ans)


if __name__ == '__main__':
    main()

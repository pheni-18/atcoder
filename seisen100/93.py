# https://atcoder.jp/contests/s8pc-3/tasks/s8pc_3_b

# 実装問題


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
    import copy

    H, W, K = inp()
    cll_ = []
    for _ in range(H):
        cs = inp_one(False)
        cl = list(map(lambda x: int(x), list(cs)))
        cll_.append(cl)

    ans = 0
    for h in range(H):
        for w in range(W):
            cll = copy.deepcopy(cll_)
            for i in reversed(range(h)):
                cll[i + 1][w] = cll[i][w]
                cll[i][w] = 0

            total = 0
            for n in range(900):
                pt = 0
                dll = [[] for _ in range(W)]
                for i in range(H):
                    cnt = 1
                    prev = -1
                    for j in range(W):
                        v = cll[i][j]
                        if v == prev:
                            cnt += 1
                            if cnt == K:
                                pt += v * K
                                for k in range(K):
                                    cll[i][j - k] = 0
                                    dll[j - k].append(i)
                            if cnt > K:
                                pt += v
                                cll[i][j] = 0
                                dll[j].append(i)
                        else:
                            cnt = 1
                        prev = v

                if pt == 0:
                    break

                total += (2 ** n) * pt
                for j in range(W):
                    for i in reversed(range(H)):
                        l = [d for d in dll[j] if d > i]
                        cnt = len(l)
                        if cnt == 0:
                            continue
                        cll[i + cnt][j] = cll[i][j]
                        cll[i][j] = 0

            ans = max(ans, total)
    
    print(ans)


if __name__ == '__main__':
    main()

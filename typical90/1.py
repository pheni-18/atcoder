# ☆4

# 


from re import A


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
    from bisect import bisect_left

    N, L = inp()
    K = inp_one()
    al = [0] + inp()

    ok = 0
    ng = L
    while ok + 1 < ng:
        wj = (ok + ng) // 2
        
        cnt = 0
        prev = 0
        flg = False
        for a in al:
            if a >= prev + wj:
                cnt += 1
                prev = a
            if cnt == K:
                if L - prev >= wj:
                    flg = True
                break
            
        if flg:
            ok = wj
        else:
            ng = wj

    print(ok)


if __name__ == '__main__':
    main()

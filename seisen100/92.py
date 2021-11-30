# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=1193&lang=jp

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
    hl = []
    slll = []
    while True:
        h = inp_one()
        if h == 0:
            break

        hl.append(h)
            
        sll = [inp() for _ in range(h)]
        slll.append(sll)

    for h, sll in zip(hl, slll):
        ans = 0
        while True:
            pt = 0
            dll = [[] for _ in range(5)]
            for i in range(h):
                cnt = 1
                e = -1
                prev = -1
                for j in range(5):
                    v = sll[i][j]
                    if v == prev:
                        cnt += 1
                        if cnt >= 3:
                            e = j
                    else:
                        if cnt >= 3:
                            break
                        cnt = 1
                    prev = v

                if e == -1:
                    continue

                for k in range(e - cnt + 1, e + 1):
                    pt += sll[i][k]
                    sll[i][k] = 0
                    dll[k].append(i)

            if pt == 0:
                break

            ans += pt
            for j in range(5):
                for i in reversed(range(h)):
                    l = [d for d in dll[j] if d > i]
                    cnt = len(l)
                    if cnt == 0:
                        continue
                    sll[i + cnt][j] = sll[i][j]
                    sll[i][j] = 0
        
        print(ans)


if __name__ == '__main__':
    main()

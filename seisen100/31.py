# https://atcoder.jp/contests/joi2012yo/tasks/joi2012yo_e

# BFS


def inp(to_int=True):
    if not type(to_int) == bool:
        raise Exception()
    l = input().split()
    return list(map(lambda x: int(x), l)) if to_int else l


def main():
    from collections import deque
    w, h = inp()
    g = [[0] * (w + 2)]
    for i in range(h):
        g.append([0] + inp() + [0])

    g.append([0] * (w + 2))

    ans = 0
    dq = deque()
    dq.append((0, 0))
    visited = [[False] * (w + 2) for _ in range(h + 2)]
    while dq:
        y, x = dq.popleft()
        if visited[y][x]:
            continue

        visited[y][x] = True

        dxl = [0, -1, 0, -1, 1, -1] if y % 2 == 0 else [1, 0, 1, 0, 1, -1]
        for dy, dx in zip([1, 1, -1, -1, 0, 0], dxl):
            vy = y + dy
            vx = x + dx
            if not ((0 <= vy < h + 2) and (0 <= vx < w + 2)):
                continue

            if g[vy][vx] == 1:
                ans += 1
                continue

            dq.append((vy, vx))

    print(ans)


if __name__ == '__main__':
    main()

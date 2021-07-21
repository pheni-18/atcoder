# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=1166&lang=jp

# BFS


def inp(to_int=True):
    if not type(to_int) == bool:
        raise Exception()
    l = input().split()
    return list(map(lambda x: int(x), l)) if to_int else l


def main():
    from collections import deque
    whl = []
    walls_xl = []
    walls_yl = []
    while True:
        w, h = inp()
        if w == 0 and h == 0:
            break

        whl.append([w, h])
        walls_x = []
        walls_y = []
        for i in range(h * 2 - 1):
            walls = inp()
            if i % 2 == 0:
                walls_x.append(walls)
            else:
                walls_y.append(walls)

        walls_xl.append(walls_x)
        walls_yl.append(walls_y)

    for i in range(len(whl)):
        w, h = whl[i]
        walls_x = walls_xl[i]
        walls_y = walls_yl[i]

        dq = deque()
        dq.append((0, 0))
        dist = [[-1] * w for _ in range(h)]
        dist[0][0] = 1
        while dq:
            y, x = dq.popleft()

            for dy, dx in zip([1, -1, 0, 0], [0, 0, 1, -1]):
                vy = y + dy
                vx = x + dx
                if not ((0 <= vy < h) and (0 <= vx < w)):
                    continue

                if dy == 1 and walls_y[y][x] == 1:
                    continue

                if dy == -1 and walls_y[y - 1][x] == 1:
                    continue

                if dx == 1 and walls_x[y][x] == 1:
                    continue

                if dx == -1 and walls_x[y][x - 1] == 1:
                    continue

                if not dist[vy][vx] == -1:
                    continue

                dist[vy][vx] = dist[y][x] + 1
                dq.append((vy, vx))

        goal_dist = dist[h - 1][w - 1]
        if goal_dist == -1:
            print(0)
            continue

        print(goal_dist)


if __name__ == '__main__':
    main()

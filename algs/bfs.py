from icecream import ic
# 幅優先探索

from collections import deque

n = 4
to = [
    [1, 3],
    [3],
    [],
    [2],
]

dist = [-1] * n
dist[0] = 0

dq = deque()
dq.append(0)
while dq:
    u = dq.popleft()
    for v in to[u]:
        if not dist[v] == -1:
            continue

        dist[v] = dist[u] + 1
        dq.append(v)

for i in range(n):
    ic(i, dist[i])

# ic| i: 0, dist[i]: 0
# ic| i: 1, dist[i]: 1
# ic| i: 2, dist[i]: 2
# ic| i: 3, dist[i]: 1

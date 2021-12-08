from icecream import ic
# 深さ優先探索

import sys
sys.setrecursionlimit(10 ** 5 + 1)

n = 4
to = [
    [1],
    [3],
    [],
    [2],
]

time = 0
times = [[0, 0] for _ in range(n)]


def dfs(u):
    global time
    time += 1

    times[u][0] = time
    for v in to[u]:
        if times[v][0] != 0:
            continue

        dfs(v)

    time += 1
    times[u][1] = time


for i in range(n):
    if times[i][0] == 0:
        dfs(i)

ic('t[0]: start_time, t[1]: end_time')
for i in range(n):
    t = times[i]
    ic(i, t[0], t[1])

# ic| 't[0]: start_time, t[1]: end_time'
# ic| i: 0, t[0]: 1, t[1]: 8
# ic| i: 1, t[0]: 2, t[1]: 7
# ic| i: 2, t[0]: 4, t[1]: 5
# ic| i: 3, t[0]: 3, t[1]: 6

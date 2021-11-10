# 二分探索

from bisect import bisect_left

l = [1, 2, 2, 3, 4, 4, 5]


from icecream import ic

ic(bisect_left(l, 0))
# ic| bisect_left(l, 0): 0

ic(bisect_left(l, 2))
# ic| bisect_left(l, 2): 1

ic(bisect_left(l, 3))
# ic| bisect_left(l, 3): 3

ic(bisect_left(l, 6))
# ic| bisect_left(l, 6): 7

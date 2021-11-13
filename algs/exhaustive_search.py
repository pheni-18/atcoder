from icecream import ic
# bit全探索

from itertools import product

N = 4
for _bit in product((True, False), repeat=N):
    # type(_bit) -> tuple
    ic(_bit)

# ic| _bit: (True, True, True, True)
# ic| _bit: (True, True, True, False)
# ic| _bit: (True, True, False, True)
# ic| _bit: (True, True, False, False)
# ic| _bit: (True, False, True, True)
# ic| _bit: (True, False, True, False)
# ic| _bit: (True, False, False, True)
# ic| _bit: (True, False, False, False)
# ic| _bit: (False, True, True, True)
# ic| _bit: (False, True, True, False)
# ic| _bit: (False, True, False, True)
# ic| _bit: (False, True, False, False)
# ic| _bit: (False, False, True, True)
# ic| _bit: (False, False, True, False)
# ic| _bit: (False, False, False, True)
# ic| _bit: (False, False, False, False)

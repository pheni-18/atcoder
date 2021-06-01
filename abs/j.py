row = 1
inp = [input() for _ in range(row)]

def sl2il(l):
    return list(map(lambda x: int(x), l))

"""
inp[]
int(inp[])
inp[].split()
sl2il(inp[].split())
"""

s = inp[0]
t = ""
l = ["dream", "dreamer", "erase", "eraser"]

ans = "NO"
i = len(s)

s = s.replace(l[3], "")
s = s.replace(l[2], "")
s = s.replace(l[1], "")
s = s.replace(l[0], "")
if s == "":
    ans = "YES"
print(ans)

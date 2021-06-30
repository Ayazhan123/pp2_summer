import sys 
sys.setrecursionlimit(10**6)

n = int(input())
d = {}
all = set()
childs = set()

# if n == 1:
#     exit()

for i in range(n - 1):
    ch, par = input().split()
    all.add(ch)
    all.add(par)
    childs.add(ch)
    if d.get(par, []) != []: d[par].append(ch)
    else: d[par] = [ch]

c = {}
def dfs(current):
    cur = 1
    for child in d.get(current, []):
        cur += dfs(child)
    c[current] = cur - 1
    return cur

main_parent = all.difference(childs).pop()
dfs(main_parent)
for item in sorted(c.items()):
    print(item[0], item[1])
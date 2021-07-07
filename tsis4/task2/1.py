import re
a = list()
for x in range(int(input())):
    a.append(bool(re.match('^[+-]?[0-9]*\.[0-9]+$', input())))
for x in a:
    print(x)
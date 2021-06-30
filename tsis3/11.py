d = dict()
# key - word, value - number of rep-s

try:
    while True:
        line = input()
        words = line.split()
        for word in words:
            if d.get(word, 0) != 0: d[word] += 1
            else: d[word] = 1
except:
    pass

def f(pair):
    return (-pair[1], pair[0])

for item in sorted(d.items(), key=f):
    print(item[0])
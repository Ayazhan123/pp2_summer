x = input().split()
for i in range(len(x)):
    if x[i]=="0":
        x.remove(x[i])
        x.append("0")

print(*x)
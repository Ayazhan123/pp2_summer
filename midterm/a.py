x = input().split()
res = 0
for i in x:
    if len(i)%2==0:
        res+=1
print(res)

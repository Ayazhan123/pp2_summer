x = input().split()
mini = 1000
for i in x:
    if int(i)>0 and int(i)<mini:
        mini=int(i)
print(mini)
l1 = input().split()
l2 = input().split()
my_set = set()
answer = list()

for i in l1:
    for j in l2:
        if i==j:
            my_set.add(i)

for i in my_set:
    answer.append(int(i))

print(sorted(answer))

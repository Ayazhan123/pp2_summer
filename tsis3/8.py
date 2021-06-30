l1 = set(input().split())
l2 = set(input().split())
print(*sorted(l1&l2,key=str))
x = input().split()
n = int(input())
for i in range(n-1, len(x)):
    print(x[i], end=" ")
for i in range(n):
    print(x[i], end=" ")
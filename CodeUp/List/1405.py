n = int(input())
k = list(map(int, input().split()))

for i in range(n):
    for j in range(n):
        print(k[i + j - n], end = ' ')
    print()
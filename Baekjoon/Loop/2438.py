N = int(input())

# 0으로 시작되면 안 되는 이유는 뭘 곱하든 0은 0만 나옴
for i in range(1, N + 1):
    print('*' * i)
print()
X = int(input()) # 영수증에 적힌 총 금액
N = int(input()) # 구매한 물건의 종류 수

for _ in range(N):
    a, b = map(int, input().split())

    X -= a * b # 총 금액에서 물건 가격, 개수 곱한 값 누적하여 빼주기

# 계속 빼주면 결국 총금액은 0원이 된다.
if(X == 0):
    print('Yes')
else:
    print('No')
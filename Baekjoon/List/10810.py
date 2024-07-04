N, M = map(int, input().split())
basket = [0] * N # 모든 바구니 0으로 지정(0으로 초기화)

for _ in range(M):
    i, j, k = map(int, input().split())
    for index in range(i, j + 1):
        basket[index - 1] = k 
        # 1번부터 넣는데 인덱스의 시작은 0이기 때문에 1 빼기
        # k번호가 적혀있는 공을 대입하면 기존의 숫자 없어짐

for index in range(N):
    print(basket[index], end = ' ')
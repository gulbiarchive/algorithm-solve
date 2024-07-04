# try ~ except 구문
# 입력이 얼마나 들어올지 모르는 상황, 끝나는 시점의 조건도 걸려있지 않음

while(True):
    try:
        a, b = map(int, input().split())
        print(a + b)
    except:
        break
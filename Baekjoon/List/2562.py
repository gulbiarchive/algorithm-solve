num = []

for _ in range(9):
    i = int(input())
    num.append(i)

print(max(num))
print(num.index(max(num))+1)

'''
index() 메서드
리스트, 튜플, 메서드 등과 같은 시퀀스(반복 가능한) 자료형에서
지정된 값의 첫 번쨰 인덱스를 반환

형식
시퀀스자료형.index(찾으려는 값, 시작위치, 끝위치)
시작 위치의 기본 값 : 
끝위치 : 선택 사항, 이 인덱스 이전까지만 검색

예시
my_list = [10, 20, 30, 40, 50]
index = my_list.index(30)
print(index)  # 출력: 2
'''
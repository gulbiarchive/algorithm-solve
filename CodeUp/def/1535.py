def find_max_position(data):
    max_value = max(data)
    max_index = data.index(max_value)
    return max_index + 1

n = int(input())
data = list(map(int, input().split()))  
# 입력된 문자열을 공백으로 분리하여 각각을 정수로 변환하여 리스트로 저장

print(find_max_position(data))
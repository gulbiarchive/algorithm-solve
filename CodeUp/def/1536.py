def find_min(data):
    min_value = min(data)
    return min_value

n = int(input())
data = list(map(int, input().split()))
print(find_min(data))
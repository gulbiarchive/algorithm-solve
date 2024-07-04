hour, score = map(int, input().split())

for _ in range(hour, 90, 5):
    score += 1
print(score)
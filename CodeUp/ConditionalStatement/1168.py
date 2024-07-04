birth, gender = map(str, input().split())

if int(gender) == 1 or int(gender) == 2:
    new_b = "19" + birth[:2]
elif int(gender) == 3 or int(gender) == 4:
    new_b = "20" + birth[:2]

print(2012 - int(new_b) + 1)
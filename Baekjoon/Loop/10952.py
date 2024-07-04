while(True):
    A, B = map(int, input().split())

    if(A == 1 and B == 1):
        break
    else:
        print(A + B)
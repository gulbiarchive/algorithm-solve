def find_prime_composite(n):
    result = 0

    for i in range(2, n + 1):
        if n % i == 0:
            result += 1

    if result == 1:
        print('prime')
    else:
        print('composite')

n = int(input())
find_prime_composite(n)
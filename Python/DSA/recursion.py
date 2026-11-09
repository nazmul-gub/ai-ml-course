def factorialn(n):

    if n <= 1:
        return 1

    return n * factorialn(n-1)

print(factorialn(5))
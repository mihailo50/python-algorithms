import math

def is_prime(n):

    if n == 1 or n == 2 or n == 3:
        return True

    half = round(n/2) + 1

    for i in range(2, half, 1):
        if n%i == 0:
            return False
        return True

print(is_prime(10))

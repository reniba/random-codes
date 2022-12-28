import math
def isprime(num):
    """return True if the number called is prime"""
    for a in range(2,math.floor(num**0.5)+1):
        if num % a == 0:
            return False
    return True


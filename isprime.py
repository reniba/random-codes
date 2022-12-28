import math
def isprime(num):
    for a in range(2,math.floor(num**0.5)+1):
        if num % a == 0:
            return False
    return True

for n in range(3,500,2):
    if isprime(n):
        print(n)

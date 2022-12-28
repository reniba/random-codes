
def divisors(num):
    """return a list with the positive divisors of the called-number"""
    divisores = []
    for a in range(1,num//2+1):
        if num % a == 0:
            divisores.append(a)
    divisores.append(num)
    return divisores



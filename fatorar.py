#fatorador
def fatorar(num):
    divisores = []
    for a in range(1,num//2+1):
        if num % a == 0:
            divisores.append(a)
    divisores.append(num)
    return divisores



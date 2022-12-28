def fatorador(num):
    '''return a list with the prime fatoration of the number called'''
    lista = []
    a = num
    n = 1
    while num != 1:
        n += 1
        if num % n == 0:
            lista.append(n)
            num /= n
            n -= 1
    return lista


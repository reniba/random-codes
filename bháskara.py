from math import isqrt
from math import fabs
#equacao quadratica
#ax^2 + bx + c
while True:
    print('-='*20)
    a = int(input('Escolha o coeficiente "a" (diferente de 0): '))
    b = int(input('Escolha o coeficiente "b": '))
    c = int(input('Escolha o coeficiente "c": '))
    delta = b**2 - 4*a*c

#determinando se as solucoes sao reais ou nao    
    if delta >= 0:
        if isqrt(delta) == fabs(delta**0.5):
            print(f'''
        Delta positivo inteiro e as raízes são:
        Raíz 1: {(-b + delta**0.5)/(a*2)}
        Raíz 2: {(-b - delta**0.5)/(a*2)}
            ''')
        else:
            print(f'''
        Delta positivo real e as raizes são:
        Raízes: {-b} +/- sqrt({delta})
                ---------------
                     {2*a}      
            ''')
    else:
        if isqrt(-delta) == (-delta)**0.5: 
            print(f'''
        Delta negativo e soluções:
        Raízes: {-b} +/- {((-delta)**0.5):.0f} i
                ---------------
                       {2*a}
        ''')
        else:
            print(f"""
        Delta negativo e soluções:
        Raízes: {-b} +/- sqrt{-delta} i
                ----------------
                    {2*a}
            """)
    print('-='*20)

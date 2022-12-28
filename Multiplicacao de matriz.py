#multiplicacao de matriz
import sys

#definindo a matriz 1:
colunaelinha1 = list(map(int,input('Quantidade de linhas e colunas da matriz A: ').split()))
matrizA = []
for l in range(1,colunaelinha1[0]+1):
    while True:
        linha = list(map(int,input(f'Elemento da {l} linha: ').split()))
        if len(linha) == colunaelinha1[1]:
            matrizA.append(linha[:])
            break
        else:
            pass


#definindo a matriz 2:
colunaelinha2 = list(map(int,input('Quantidade de linhas e colunas da matriz B: ').split()))
matrizB = []
for li in range(1,colunaelinha2[0]+1):
    while True:
        linha2 = list(map(int,input(f'Elemento da {li} linha: ').split()))
        if len(linha2) == colunaelinha2[1]:
            matrizB.append(linha2[:])
            break
        else:
            pass


#condicoes para multiplicação
if colunaelinha1[1] != colunaelinha2[0]:
    print('Não tem como multiplicá-las.  =( ')
    sys.exit()

#multiplicando
matriz = []
for q in range(0,colunaelinha1[0]):
    linha = []
    for l in range(0,colunaelinha2[1]):
        c = 0
        for p in range(0,colunaelinha1[1]):
            c += (matrizA[q][p]*matrizB[p][l])
        linha.append(c)
    matriz.append(linha[:])
print(f'a matriz resultante é: {matriz}.')

#determinante 4x4 por laplace
import funcaodeterminante as fd
import copy

def cofator(mat,num):
    matrizaux = copy.deepcopy(mat)
    matrizaux.pop(0)
    for linha in matrizaux:
        linha.pop(num)
    return float((mat[0][num])*(fd.determinante(matrizaux))*((-1)**(num)))


matriz = []
n = int(input('Deseja o determinante de uma matriz quanto por quanto? '))
for a in range(1,n+1):
    linha = []
    linha = list(map(float,input(f'Escolha a linha {a} da matriz: ').split()))
    matriz.append(linha[:])

det = 0
for n in range(0,len(matriz)):
    det += cofator(matriz,n)    
print(det)

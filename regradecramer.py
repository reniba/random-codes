import funcaodeterminante as fd

def PedirEquação(linha):
    string = input('Digite a equação na forma ax + by + ...= c. ').split('=')
    intermediario = ''
    final = []
    for n in string[0]:
        if not n.isalpha():
            intermediario += n
    iteravel = intermediario.split()
    final.append(float(iteravel[0]))
    for m in range(1,len(iteravel),2):
        if iteravel[m] == '+':
            final.append(float(iteravel[m+1]))
        else:
            final.append(-float(iteravel[m+1]))
    return final,float(string[1])


#determinando o sistema de equações
matriz = []
matrizCOMP = []
n = int(input('Deseja calcular um sistema de equações de quantas incógnitas? '))
for m in range(1,n+1):
    linha = PedirEquação(m)
    matriz.append(linha[0][:])
    matrizCOMP.append(linha[1])

#determinante da raiz primaria
determinantegeral = float(fd.determinante(matriz))
print(determinantegeral)
#calculando o determinante das matrizes secundarias
for incognita in range(len(matriz)):
    matrizaux = []
    for line in matriz:
        matrizaux.append(line[:])
    for popi in range(len(matriz)):
        matrizaux[popi][incognita] = matrizCOMP[popi]
    print(matrizaux)
    print(fd.determinante(matrizaux),determinantegeral)
    try:
        print(fd.determinante(matrizaux)/determinantegeral)
    except:
        print('erro')
    


    

    

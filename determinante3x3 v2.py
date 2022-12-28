#determinando qual a matriz nxn e a sua matriz relacionada a qual é feita 
#recolocando, à direita, (as n-1) primeiras colunas para facilitar o calculo
#determinante
matriz = []
matrizreal = []
n = int(input('Deseja o determinante de uma matriz quanto por quanto? '))
for a in range(1,n+1):
    linha = []
    linhareal = []
    for b in range (1,n+1):
        x = int(input(f'Escolha o elemento A{a}{b} da matriz: '))
        linha.append(x)
        linhareal.append(x)
    for c in range(0,n-1):
        linhareal.append(linha[c])
    matriz.append(linha[:])
    matrizreal.append(linhareal[:])
#determinante


#lista das diagonais positivas
diagpos = []
diag = 1
for k in range(0,n):
    for s in range(0,n):
        diag *= matrizreal[s][s+k]
    diagpos.append(diag)
    diag = 1


#lista das diagonais negativas
diagneg = []
diag2 = 1
for l in range(0,n):
    for p in range(0,n):
        diag2 *= matrizreal[p][len(matrizreal[0])-1-p-l]
    diagneg.append(diag2)
    diag2 = 1
print(sum(diagpos) - sum(diagneg))
    

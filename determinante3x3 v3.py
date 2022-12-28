#determinante 2
matriz = []
matrizreal = []
n = int(input('Deseja o determinante de uma matriz quanto por quanto? '))
for a in range(1,n+1):
    linha = list(map(int,input(f'Digite a linha {a}: ').split()))
    linhareal = linha[:]
    for b in range(n-1):
        linhareal.append(linha[b])
    matriz.append(linha[:])
    matrizreal.append(linhareal[:])


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

def determinante(matriz):
    """return the determinant of an array with dimensions 1x1,2x2,3x3"""
    if len(matriz) == 1:
        return matriz[0][0]
    elif len(matriz) == 2:
        return matriz[0][0]*matriz[1][1]-matriz[1][0]*matriz[0][1]
    else:
        matrizreal = []
        for linha in matriz:
            linhareal = []
            for elemento in linha:
                linhareal.append(elemento)
            for m in range(len(linha)-1):
                linhareal.append(linha[m])
            matrizreal.append(linhareal[:])
        diagpos = []
        diag = 1
        for k in range(0,len(matriz)):
            for s in range(0,len(matriz)):
                diag *= matrizreal[s][s+k]
            diagpos.append(diag)
            diag = 1
        diagneg = []
        diag2 = 1
        for l in range(0,len(matriz)):
            for p in range(0,len(matriz)):
                diag2 *= matrizreal[p][len(matrizreal[0])-1-p-l]
            diagneg.append(diag2)
            diag2 = 1
        return (sum(diagpos)-sum(diagneg))



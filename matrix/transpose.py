def transpose(matrix):
    if matrix == None or len(matrix) == 0:
        raise ValueError("no puede ser vacia")
    aux=[[None for i in range(len(matrix))] for j in range(len(matrix[0]))]
    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            aux[i][j] = matrix[j][i]
    return aux

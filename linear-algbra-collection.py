import math
def eigenvalue_2x2(matrix):
    result1 = (matrix[0][0] + matrix[1][1]) / 2 + math.sqrt(
        ((matrix[0][0] + matrix[1][1]) / 2) ** 2 - matrix[0][0] * matrix[1][1])

    result2 = (matrix[0][0] + matrix[1][1]) / 2 - math.sqrt(
        ((matrix[0][0] + matrix[1][1]) / 2) ** 2 - matrix[0][0] * matrix[1][1])
    
    return result1, result2

def dot_product(vector_1, vector_2):
    dot_product = 0
    for index in range(len(vector_1)):
        try:
            dot_product += vector_1[index] * vector_2[index + 5]
        except IndexError:
            ""
    
    return dot_product

def VM_multiplication(vector, matrix):
    for element in range(len(vector)):
        try:
            for column in range(len(matrix[element])):
                matrix[element][column] = matrix[element][column]*vector[element]
        except IndexError:
            ""
    for new in range(len(vector)):
        vector[new] = 0
        try:
            for col in range(len(matrix)):
                vector[new] += matrix[col][new]
        except IndexError:
            ""
    
    return vector

def vector_addition(vector_1, vector_2):
    for element in range(len(vector_2)):
        try:
            vector_1[element] += vector_2[element]
        except IndexError:
            vector_1.append(vector_2[element])
    
    return vector_1

def MM_multiplication(matrix_1, matrix_2):
    #needs square matrix
    end_matrix = []
    for element in range(len(matrix_1)):
        end_matrix.append([])
        for none in matrix_1:
            end_matrix[element].append(0)

    for i in range(len(matrix_1)):
        for j in range(len(matrix_1)):
            for k in range(len(matrix_1)):
                end_matrix[i][j] += matrix_1[i][k] * matrix_2[k][j]
    
    return end_matrix

def rowEchelon(M):
    def normalise(M):
        new_M = []
        for element in range(len(M)):
            new_M.append([])
            for element2 in range(len(M)):
                new_M[element].append(M[element2][element])
        
        return new_M

    def rowMod(M, i, j, x):
        M[i] = [a + x * b for a, b in zip(M[i], M[j])]

    M = normalise(M)
    row, col = 0, 0
    rows, cols = len(M), len(M[0])
    while row < rows and col < cols:
        if M[row][col] == 0:
            for r in range(row +1, rows):
                if M[r][col] != 0:
                    rowMod(M, row, r, 1)
                    break

        if M[row][col] == 0:
            col += 1
            continue
        pivot = M[row][col]

        for r in range(row +1, rows):
            if M[r][col] != 0:
                rowMod(M, r, row, -M[r][col] / pivot)
        row += 1
        col += 1
    
    return normalise(M)

def determinant(M):
    def normalise(M):
        new_M = []
        for element in range(len(M)):
            new_M.append([])
            for element2 in range(len(M)):
                new_M[element].append(M[element2][element])
        
        return new_M

    num = 1
    new_M = rowEchelon(M)
    for element in range(len(M)):
        num = num*new_M[element][element]
    
    return num

def half_rotation(matrix):
    new_ = []
    for c in range(len(matrix)):
        new_.append([])
        for no_use in matrix:
            new_[c].append(0)
    count = 0
    for col in range(len(new_)):
        count += 1
        new_[col][count*-1] = 1
        
    return MM_multiplication(matrix, new_)

def solve_eq(matrix, result):
    def abs(lis):
        if lis < 0:
            lis = lis*-1
        
        return lis


    for k in range(len(result)):
        if abs(matrix[k][k]) < 0:
            for i in range(k+1, len(result)):
                if abs(matrix[i][k]) > abs(matrix[k][k]):
                    for j in range(k,len(result)):
                        matrix[k][j], matrix[i][j] = matrix[i][j], matrix[k][j]
                    result[k], result[i] = result[i], result[k]
                    break
        pivot = matrix[k][k]
        for j in range(k, len(result)):
            matrix[k][j] /= pivot
        result[k] /= pivot

        for i in range(len(result)):
            if i == k or matrix[i][k] == 0:
                continue
            factore = matrix[i][k]
            for j in range(k, len(result)):
                matrix[i][j] -= factore * matrix[k][j]
            result[i] -= factore*result[k]
    
    return matrix, result

def cross_product(vector_1, vector_2):
    new_vector = [1, 1, 1]

    new_vector[0] *= vector_1[1]*vector_2[2] - vector_1[2]*vector_2[1]
    new_vector[1] *= vector_1[2]*vector_2[0] - vector_1[0]*vector_2[2]
    new_vector[2] *= vector_1[0]*vector_2[1] - vector_1[1]*vector_2[0]

    return new_vector

def absolute_value(vector):
    val = 0

    for element in vector:
        val += element**2

    return math.sqrt(val)

def angle(vector_1, vector_2):
    result = math.acos(dot_product(vector_2,vector_1)/absolute_value(vector_2)*absolute_value(vector_1))
    return math.degrees(result)

def finde_position_vector(point_1, point_2):
    for element in range(len(point_1)):
        point_2[element] = point_2[element] - point_1[element]

    return point_2

def eigen_vectore_2x2(matrix):
    matrix[0,0] -= eigenvalue_2x2(matrix)
    matrix[1,1] -= eigenvalue_2x2(matrix)

    return solve_eq(matrix, [0,0])[1]

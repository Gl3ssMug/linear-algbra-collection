def determinant(M):
    from web_app_tool import string_matrix
    M = string_matrix(M)
    def normalise(M):
        new_M = []
        for element in range(len(M)):
            new_M.append([])
            for element2 in range(len(M)):
                new_M[element].append(M[element2][element])
        return new_M

    def rowMod(M, i, j, x):
        M[i] = [a + x * b for a, b in zip(M[i], M[j])]

    def rowEchelon(M):
        M = normalise(M)
        row, col = 0, 0
        rows, cols = len(M), len(M[0])
        while row < rows and col < cols:
            if M[row][col] == 0:
                for r in range(row + 1, rows):
                    if M[r][col] != 0:
                        rowMod(M, row, r, 1)
                        break

            if M[row][col] == 0:
                col += 1
                continue
            pivot = M[row][col]

            for r in range(row + 1, rows):
                if M[r][col] != 0:
                    rowMod(M, r, row, -M[r][col] / pivot)

            row += 1
            col += 1

        return normalise(M)

    num = 1
    new_M = rowEchelon(M)
    for element in range(len(M)):
        num = num*new_M[element][element]
    return num


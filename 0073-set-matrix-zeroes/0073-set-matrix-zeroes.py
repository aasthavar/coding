# class Solution:
#     def setZeroes(self, matrix: list[list[int]]) -> None:
#         """
#         Do not return anything, modify matrix in-place instead.
#         """
#         rows, cols = len(matrix), len(matrix[0])
#         zero_rows, zero_cols = set(), set()

#         for i in range(rows):
#             for j in range(cols):
#                 if matrix[i][j] == 0:
#                     print(i, j)
#                     zero_rows.add(i)
#                     zero_cols.add(j)
        
#         # print(zero_rows, zero_cols)

#         for i in zero_rows:
#             matrix[i] = [0] * cols
        
#         for j in zero_cols:
#             for i in range(rows):
#                 matrix[i][j] = 0

class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        col0 = False   # "column 0 must be zeroed" â kept outside the matrix

        # Pass 1: only drop flags
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0          # flag row i (column 0 = row flags)
                    if j == 0:
                        col0 = True           # corner is taken, so use the boolean
                    else:
                        matrix[0][j] = 0      # flag column j (row 0 = column flags)

        # Pass 2: inner cells, one at a time, reading the flags
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Pass 3: row 0, using the corner
        if matrix[0][0] == 0:
            for j in range(n):
                matrix[0][j] = 0

        # Pass 4: column 0, using col0
        if col0:
            for i in range(m):
                matrix[i][0] = 0
        
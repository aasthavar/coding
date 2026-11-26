class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        rows, cols = len(matrix), len(matrix[0])

        top, bottom = 0, rows - 1
        left, right = 0, cols - 1

        result = []

        while top <= bottom and left <= right:

            # 1. Left â Right (top row)
            for j in range(left, right + 1):
                result.append(matrix[top][j])
            top += 1

            # 2. Top â Bottom (right column)
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1

            # 3. Right â Left (bottom row)
            if top <= bottom:
                for j in range(right, left - 1, -1):
                    result.append(matrix[bottom][j])
                bottom -= 1

            # 4. Bottom â Top (left column)
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1

        return result
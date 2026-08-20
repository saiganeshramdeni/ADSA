'''#867 transpose Matrix
def transpose(matrix: list[list[int]]) -> list[list[int]]:
    rows,cols = len(matrix),len(matrix[0])
    res = [[0] * rows for _ in range(cols)]
    for i in range(rows):
        for j in range(cols):
            res[j][i] = matrix[i][j]
    return res

matrix = [[1,2,3],[4,5,6],[7,8,9]]
transposed = transpose(matrix)
print(transposed)


#method 2
def transpose(matrix: list[list[int]]) -> list[list[int]]:
    return [list(row) for row in zip(*matrix)]

matrix = [[1,2,3],[4,5,6],[7,8,9]]
transposed = transpose(matrix)
print(transposed)
'''

'''
#566 Reshape the Matrix
def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
    m,n = len(mat),len(mat[0])
    if m*n != r*c:
        return mat
    reshaped = [[0] * c for _ in range(r)]
    for i in range(m*n):
        orig_row =i // n
        orig_col = i % n
        new_row = i // c
        new_col = i % c
        reshaped[new_row][new_col] = mat[orig_row][orig_col]
    return reshaped
        
        

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m,n = len(matrix),len(matrix[0])
        left,right = 0,m*n-1

        while left <= right:
            mid = (left + right) // 2
            row,col = mid // n,mid % n
            if target == matrix[row][col]:
                return True
            elif target < matrix[row][col]:
                right = mid -1
            else:
                left =mid + 1
        return False
        '''


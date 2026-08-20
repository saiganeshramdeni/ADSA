'''#1572. Matrix Diagonal Sum

# traditional approach
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        s = 0
        for i in range(n):
            for j in range(n):
                if i  == j:
                    s += mat[i][j]
                if i + j == n -1:
                    s += mat[i][j]
        if n % 2 == 1:
            s -= mat[n // 2][n // 2]
        return s
mat = =[[1,2,3][4,5,6][7,8,9]]
print(diagonalsum_brute(mat))

        
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        s = 0
        for i in range(n):
            for j in range(n):
                if i  == j:
                    s += mat[i][i]
                    s += mat[i][n-1-i]  #if i + j == n -1: j = n -1-i
        if n % 2 == 1:
            s -= mat[n // 2][n // 2]
        return s



#498. Diagonal Traverse

class solution:
    def findDiagonalOrder(self,mat:list[list[int]]) -> list[int]:
        rows,cols = len(mat),len(mat[0])
        res = []
        fro d in range(rows + cols - 1):
        Diagonal = []
        r = 0 if d < cols else d - cols + 1
        c = d if d < cols else cols - 1
        while r < rows and c >=0:
            Diagonal.append(mat[r][c])
            r = 1
            c = 1
        if d % 2 == 0:
            Diagonal.reverse()
        res += Diagonal
    return res 
    
        
        '''
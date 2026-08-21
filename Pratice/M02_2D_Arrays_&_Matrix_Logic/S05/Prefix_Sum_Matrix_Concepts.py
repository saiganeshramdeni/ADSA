'''#1314. Matrix Block Sum
class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m,n = len(mat),len(mat[0])
        res = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                r_s = max(0,i-k)
                c_s = max(0,j-k)
                r_end = min(i+k,m-1)
                c_end = min(j+k,n-1)
                for r in range(r_s,r_end+1):
                    for c in range(c_s,c_end+1):
                        res[i][j] += mat[r][c]
        return res


        '''
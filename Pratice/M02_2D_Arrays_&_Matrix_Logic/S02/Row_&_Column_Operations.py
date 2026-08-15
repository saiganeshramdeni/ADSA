'''
#1351. Count Negative Numbers in a Sorted Matrix
#traditional approach
from typing import list 

class solution:
    def countNegatives_brute(self, grid: List[List[int]]) -> int:
        count = 0
        for row in grid:
            for element in row:
                if element < 0:
                    count += 1
        return count
grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
print(countNegatives_brute(grid))

'''
#2 method

from typing import List
def countNegatives_brute(grid: List[List[int]]) -> int:
    rows,cols = len(grid),len(grid[0])  # count the number of rows and columns in the matrix,every time it would be chaged the matrix may not be 4X4
    s = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] < 0:
                s += (cols - j)
                break
    return s
grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
print(countNegatives_brute(grid))



'''
#832. Flipping an Image

def flipAndInvertImage(image: List[List[int]]) -> List[List[int]]:
    for row in image:
        row.reverse()
        for j in range(len(row)):  #row[j] = 1 if row[j] == 0 else 0  or row[j] =1 - row[j] 
            if row[j] == 0:
                row[j] = 1
            else:
                row[j] = 0
    return image        '''
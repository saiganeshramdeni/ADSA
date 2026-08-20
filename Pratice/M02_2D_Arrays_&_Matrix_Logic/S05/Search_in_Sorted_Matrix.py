#74. Search a 2D Matrix



'''class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        arr = [] 
        for row in matrix:
            arr += row
        left,right = 0,len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if traget == arr[mid]:
                return True
            elif traget < arr[mid]:
                right = mid -1
            else:
                left =mid + 1
        return false
        
	 
'''


#240. Search a 2D Matrix II
'''class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
             False

        row = 0
        col = len(matrix[0]) - 1
        while row < len(matrix) and col >= 0:
            current_value = matrix[row][col]
            if current_value == target:
                return True
            elif current_value > target:
                col -= 1  
            else:
                row += 1   
        return False
        '''

378
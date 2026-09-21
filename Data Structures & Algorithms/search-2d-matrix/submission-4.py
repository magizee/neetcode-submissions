class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        h = len(matrix) * len(matrix[0]) - 1

        while l <= h:
            m = l + (h - l) // 2
            r = (m) // len(matrix[0])
            c = m - len(matrix[0])*r 
       


            if matrix[r][c] < target:
                l = m + 1
            elif matrix[r][c] > target:
                h = m - 1
            else:
                return True
        return False
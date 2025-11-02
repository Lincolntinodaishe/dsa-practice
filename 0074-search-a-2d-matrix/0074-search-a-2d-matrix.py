class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #bRUTE 
        # for row in matrix:
        #     for col in row:
        #         if col == target:
        #             return True
        # return False

        if not matrix:
            return False
        #assign pointers and the begining and the end
        m = len(matrix)  #rows
        n = len(matrix[0]) #columns
        l = 0
        r = m*n -1

        while l <= r:
            mid = (l+r)//2 #MID OF THE 2D ARRAY
            row = mid//n  #ROW INDEX
            col = mid%n   #COL INDEX

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                r = mid-1
            else:
                l = mid+1
        return False 
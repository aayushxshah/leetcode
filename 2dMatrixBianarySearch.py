#https://leetcode.com/problems/search-a-2d-matrix/

import math
def searchMatrix(matrix: list[list[int]], target: int) -> bool:


        #search column
        right = len(matrix)-1
        left = 0
        m = int()

        while left < right:
            
            m = math.floor((left+right)/2)
            value = matrix[m][0]

            if target == matrix[m][0]:
                return True
            elif target > matrix[m][0]:
                left = m + 1
            elif target < matrix[m][0]:
                right = m - 1

        m -= 1


        #search row
        right1 = len(matrix[m])-1
        left1 = 0
        m1 = int()

        while left1 <= right1:
            
            m1 = math.floor((left1+right1)/2)
            value = matrix[m][m1]

            if target == matrix[m][m1]:
                return True
            elif target > matrix[m][m1]:
                left1 = m1 + 1
            elif target < matrix[m][m1]:
                right1 = m1 - 1
        
        return False
        


        

val = searchMatrix(matrix=[[1,3,5,7],[10,11,16,20],[23,30,34,50]], target= 23)
print(val)
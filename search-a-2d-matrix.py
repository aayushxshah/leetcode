#https://leetcode.com/problems/search-a-2d-matrix/
class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:

        right = (len(matrix[0])*len(matrix))-1
        left = 0

        while left <= right:
        
            if target == matrix[int(int((left+right)/2)/len(matrix[0]))][int((left+right)/2)%len(matrix[0]) ]:
                return True
            elif target > matrix[int(int((left+right)/2)/len(matrix[0]))][int((left+right)/2)%len(matrix[0]) ]:
                left = int((left+right)/2) + 1
            elif target < matrix[int(int((left+right)/2)/len(matrix[0]))][int((left+right)/2)%len(matrix[0]) ]:
                right = int((left+right)/2) - 1

        return False
        

s = Solution()   

val = s.searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3)
print(val)
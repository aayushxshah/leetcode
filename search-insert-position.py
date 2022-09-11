#https://leetcode.com/problems/search-insert-position/submissions/

class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        
        l = list(range(len(nums)))
        if l == []:
            l = [0]
        
        for i in l:
            if nums[i] >= target:
                return i
        
        return len(nums)  

s = Solution()
print(s.searchInsert(nums=[1],target=0))
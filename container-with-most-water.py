#https://leetcode.com/problems/container-with-most-water/
class Solution:
    def maxArea(self, height: list[int]) -> int:
        max = 0
        s = 0
        e = len(height)-1
        while e>s:
            sh = height[s]
            eh = height[e]
            area = min(sh,eh)*(e-s)
            if area > max:
                max = area
            if sh >= eh:
                while height[e]<=eh and s<e:
                    e -= 1
            else:
                while height[s]<=sh and s<e:
                    s += 1
        return max
       

s = Solution()
s.maxArea(height = [1,8,6,2,5,4,8,3,7])
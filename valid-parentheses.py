#https://leetcode.com/problems/valid-parentheses/
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        chardict = {')':'(' , '}':'{' , ']':'['}
        for char in s:
            if char in chardict.values():
                stack.append(char)
            elif char in chardict.keys():
                if stack == [] or chardict[char] != stack.pop():
                    return False
        
        if stack == []:
            return True
        else: return False

s = Solution()
print(s.isValid(s = "({})[]"))
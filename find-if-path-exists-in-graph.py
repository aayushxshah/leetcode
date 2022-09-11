#https://leetcode.com/problems/find-if-path-exists-in-graph/
class Solution:
    def __init__(self) -> None:
        self.return_value = False

    def findPath(self, start, finish, path=[]):
        
        path.append(start)

        if start == finish:
            self.return_value = True
            
        
        for vector in self.edges_dict[start]:
            if vector not in path and self.return_value != True:
                self.findPath(vector, finish, path)


    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:

        if 0 > source > n-1 or 0 > destination > n-1:
            return False

        self.edges_dict = {}

        for a,b in edges:
            
            if a in self.edges_dict:
                self.edges_dict[a].append(b)
            else:
                self.edges_dict[a] = [b]
        
        self.findPath(source,destination)

        return self.return_value
        

s = Solution()
print(s.validPath(
    n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination = 5
))
        

    
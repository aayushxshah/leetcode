#https://leetcode.com/problems/find-center-of-star-graph/submissions/

def findCenter(edges: list[list[int]]) -> int:

    if edges[0][0] == edges[1][0] or edges[0][0] == edges[1][1]: return edges[0][0]
    return edges [0][1]
    
x = [[1,2],[2,3],[4,2]]
y = [[1,2],[5,1],[1,3],[1,4]]

print(findCenter(edges = y))
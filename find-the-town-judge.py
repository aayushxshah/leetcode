#https://leetcode.com/problems/find-the-town-judge/

def findJudge(n: int, trust: list[list[int]]) -> int:

    if n == 1:
        return 1

    trusted_by = {}
    for item in trust:
        if item[1] in trusted_by:
            trusted_by[item[1]].append(item[0])
        else:
            trusted_by[item[1]] = [item[0]]
    
    judges = []

    for trusted in trusted_by:
        if len(trusted_by[trusted]) == n-1:
            judges.append(trusted)
    
    i = 0

    for judge in judges:
        for connection in trust:
            if connection[0] == judge:
                judges[i] = None

        i += 1
    
    judges = list(filter(None, judges))
    
    if len(judges) == 1:
        return judges[0]
    else: return -1



print(findJudge(
    n = 2, trust = [[1,2],[2,1]]
    ))
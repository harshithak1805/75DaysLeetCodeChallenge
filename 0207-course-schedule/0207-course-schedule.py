class Solution:
    def canFinish(self, nc: int, pr: List[List[int]]) -> bool:
        g=[[] for i in range(nc)]
        for x,y in pr:
            g[y].append(x) 
        v=[0]*nc
        def dfs(c):
            if v[c]==1:
                return False
            if v[c]==2:
                return True
            v[c]=1
            for k in g[c]:
                if not dfs(k):
                    return False
                
            v[c]=2
            return True
    
        for i in range(nc):
            if not dfs(i):
                return False
        return True
        
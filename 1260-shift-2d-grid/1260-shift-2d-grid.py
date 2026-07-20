class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        arr=[]
        n=len(grid)
        m=len(grid[0])
        for i in range(n):
            for j in range(m):
                arr.append(grid[i][j])
        k%=len(arr)
        res=[]
        idx=0
        arr=arr[-k:]+arr[:-k]
        for i in range(n):
            r=[]
            for j in range(m):
                r.append(arr[idx])
                idx+=1
            res.append(r)
        return res
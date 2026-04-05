class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n=len(matrix)
        m=len(matrix[0])
        i=0
        j=m-1
        while j>=0 and i<n:
            if target==matrix[i][j]:
                return True
            elif target>matrix[i][j]:
                i+=1
            else:
                j-=1
        return False
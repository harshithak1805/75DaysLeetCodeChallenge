class Solution:
    def canJump(self, arr: List[int]) -> bool:
        maxidx=0
        for i in range(len(arr)):
            if maxidx>=i:
                if (arr[i]+i) > maxidx:
                    maxidx=arr[i]+i
            else:
                    return False
                    break
        else:
            return True
        
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        i=0
        nums=[]
        while i<n:
            x=start+2*(i)
            nums.append(x)
            i+=1
        res=nums[0]
        for i in range(1,len(nums)):
            res=res^nums[i]
        return res
            

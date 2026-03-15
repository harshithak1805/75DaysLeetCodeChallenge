class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
            n=len(nums)
            res=[]
            s=set(nums)
            for i in range(1,n+1):
                if i not in s:
                    res.append(i)
            return res

            

            
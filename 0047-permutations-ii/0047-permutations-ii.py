from itertools import permutations
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res=[]
        for p in permutations(nums):
            if p in res:
                pass
            else:
                res.append(p)
        return res

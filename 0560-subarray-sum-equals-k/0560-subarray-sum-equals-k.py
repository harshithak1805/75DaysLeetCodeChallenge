class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n=len(nums)
        c=0
        ps=0
        hm={0:1}
        for i in nums:
            ps+=i
            if ps-k in hm:
                c+=hm[ps-k]
            hm[ps]=hm.get(ps,0)+1
        return c
            
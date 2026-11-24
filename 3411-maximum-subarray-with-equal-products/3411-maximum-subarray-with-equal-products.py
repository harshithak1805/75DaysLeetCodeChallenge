class Solution:
    def maxLength(self, nums: List[int]) -> int:
        maxi=0
        n=len(nums)
        for i in range(n):
            pro=1
            g=0
            l=1
            for j in range(i,n):
                pro*=nums[j]
                g=math.gcd(g,nums[j])
                l=math.lcm(l,nums[j])
                if pro==l*g:
                    maxi=max(maxi,j-i+1)
        return maxi 
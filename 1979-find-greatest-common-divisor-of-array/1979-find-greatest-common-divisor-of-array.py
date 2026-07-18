class Solution:
    def findGCD(self, nums: List[int]) -> int:
        s=min(nums)
        l=max(nums)
        return math.gcd(s,l)
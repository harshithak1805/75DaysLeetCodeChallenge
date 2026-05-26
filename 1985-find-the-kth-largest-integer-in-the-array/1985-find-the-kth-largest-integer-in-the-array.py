class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
            x=[]
            for i in nums:
                x.append(int(i))
            return str(sorted(x)[len(nums)-k])
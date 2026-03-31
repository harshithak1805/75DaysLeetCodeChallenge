class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        wsum = 0
        min_len = float('inf')

        for right in range(len(nums)):
            wsum += nums[right]

            while wsum >= target:
                min_len = min(min_len, right - left + 1)
                wsum -= nums[left]
                left += 1

        return 0 if min_len == float('inf') else min_len
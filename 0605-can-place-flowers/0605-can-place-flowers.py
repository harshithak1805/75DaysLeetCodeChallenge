class Solution:
    def canPlaceFlowers(self, nums: List[int], n: int) -> bool:
        count = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                left = 0 if i == 0 else nums[i - 1]
                right = 0 if i == len(nums) - 1 else nums[i + 1]

                if left == 0 and right == 0:
                    nums[i] = 1
                    count += 1

            if count >= n:
                return True

        return count >= n
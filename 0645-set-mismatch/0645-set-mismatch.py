from collections import Counter

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)

        duplicate = 0
        missing = 0

        n = len(nums)

        for i in range(1, n + 1):
            if freq[i] == 2:
                duplicate = i
            elif freq[i] == 0:
                missing = i

        return [duplicate, missing]
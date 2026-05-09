class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        r=start^goal
        return str(bin(r)[2:]).count("1")
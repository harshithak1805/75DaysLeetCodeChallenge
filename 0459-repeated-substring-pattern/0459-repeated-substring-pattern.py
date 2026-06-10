class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        x=s+s
        return True if s in x[1:-1] else False
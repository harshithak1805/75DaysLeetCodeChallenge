from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s=sorted(s)
        t=sorted(t)
        c1=Counter(s)
        c2=Counter(t)
        return s==t
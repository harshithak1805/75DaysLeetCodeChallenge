class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        found=True
        if len(s)==len(t):
            for i in set(s):
                if s.count(i)==t.count(i):
                    pass
                else:
                    found=False
            for i in set(t):
                if s.count(i)==t.count(i):
                    pass
                else:
                    found=False
        else:
            found=False
        return found

                
            

